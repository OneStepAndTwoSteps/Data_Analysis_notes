#author py chen

from sklearn.metrics import confusion_matrix,precision_recall_curve
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import itertools
import numpy as np

# cmp=plt.cm.Blues 为定义绘图图谱的颜色
def plot_confusion_matrix(cm,classes,normalize=False,title='confusion matrix',cmap=plt.cm.Blues):
    # 创建图
    plt.figure()
    # 这里指不指定 interpolation 都一样，如果将interpolation='bilinear'或者其他格式，我们可以看到图像变虚化，各自之间的相隔不明显
    plt.imshow(cm,interpolation='nearest',cmap=cmap)
    plt.title(title)
    # 图像最终画出来的右侧的那个渐变条
    plt.colorbar()
    # rotation用于用户定义的旋转演示自定义刻度标签，下面这样定义和不定义相同，如果想旋转刻度可使用rotation='vertical'
    plt.xticks(classes,classes)
    plt.yticks(classes,classes)

    # 设置一个阈值
    thresh=cm.max()/2.

    #迭代器循环，将值分别赋给i和j
    for i,j in itertools.product(range(cm.shape[0]),range(cm.shape[1])):
        # 这里注意x=j和y=i分别表示坐标轴上的值，我们要保持cm中原本的顺序，cm[i,j]对应参数s表示说明文字，horizontalaligment表示水平对齐方式，color为字体颜色，下面if else定义如果超过阈值字体为黑
        plt.text(j,i,cm[i,j],horizontalalignment='center',color='white' if cm[i,j] >thresh else 'black')

    # tight_layout自动调整子图参数，以便子图符合图形区域
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()

# 定义正类负类，然后得出精确度，召回率
# 我们在进行模型的预测得到混淆矩阵之后，其实计算出来的矩阵是不管正类和负类的，正类和负类需要我们去定义
# 我们对得出来的图进行分析，纵坐标表示实际上的分类，横坐标表示我们预测的分类，这样我们就可以先判断出左上角和右下角的方格为T(分类正确)，右上角和左下角为f(分类错误)。
# 之后我们就可以对内容进行一个正负类的一个分类，我们将欺骗判断为正类，这样我们可以得出右下角的方格[1,1]为tp，右上角的方格因为原先是负类(正常交易)所以属于n(负类)为fn。
# 按照上面的思路我们就可以有以下定义
def show_metrics():
    tp = cm[1, 1]
    fn = cm[1, 0]
    fp = cm[0, 1]
    tn = cm[0, 0]
    print('精确率: {:.3f}'.format(tp / (tp + fp)))
    print('召回率: {:.3f}'.format(tp / (tp + fn)))
    print('F1 值: {:.3f}'.format(2 * (((tp / (tp + fp)) * (tp / (tp + fn))) / ((tp / (tp + fp)) + (tp / (tp + fn))))))

def plot_precision_recall():
    # 步长图
    plt.step(recall,precision,color='b',alpha=0.2,where='post')
    # 填充线内部的区域
    plt.fill_between(recall,precision,color='b',step='post',alpha=0.2)
    # 将线画粗
    plt.plot(recall,precision,linewidth=2)
    # 获取或设置当前轴的x限制。
    plt.xlim([0.0,1])
    plt.ylim([0.0,1.05])
    plt.xlabel('召回率')
    plt.ylabel('精确率')
    plt.title('精确率 - 召回率 曲线')
    plt.show()

# 加载数据
data=pd.read_csv('./creditcard.csv',encoding='utf-8')

# 数据探索
print(data.describe())

# 画类别分类图
# 设置plt支持中文格式
plt.rcParams['font.sans-serif']=['SimHei']

# 绘制类别分布
plt.figure()
ax=sns.countplot(x='Class',data=data)
plt.title('类别分布 \n 0表示正常交易数，1表示诈骗交易数' )
plt.show()

# 统计总交易笔数
num=len(data)
# 统计欺诈交易笔数
num_fraud=len(data[data['Class']==1])
print("诈骗交易笔数",num_fraud)
print("总交易笔数",num)
print("诈骗交易比例 %.6lf"%(num_fraud/num) )

# 正常交易和欺诈交易 时间和次数 可视化
# sharex 控制x(sharex)或y(sharey)轴之间的属性共享：
#  1.True或者'all'：x或y轴属性将在所有子图(subplots)中共享.
#  2.False或'none'：每个子图的x或y轴都是独立的部分
#  3.'row'：每个子图在一个x或y轴共享行(row)
#  4.'col':每个子图在一个x或y轴共享列(column)
# ax1 ax2 分别表示子图1和子图2
f,(ax1,ax2)=plt.subplots(2,1,sharex=True,figsize=(16,8))
# 显示50条柱状条
bins=50
# 画子图1的柱状图
ax1.hist(data['Time'][data['Class']==1],bins=bins,color='deeppink')
ax1.set_title('诈骗交易')
# 画子图1的柱状图
ax2.hist(data['Time'][data['Class']==0],bins=bins,color='green')
ax1.set_title('正常交易')
# 因为坐标共享，我们直接这样定义即可
plt.xlabel('时间')
plt.ylabel('交易次数')
# 画图
plt.show()

# 对交易金额进行特征规范化
ss=StandardScaler()
data['Amount_Nor']=ss.fit_transform(data['Amount'].values.reshape(-1,1))

# 特征选择
y=data['Class'].values
data=data.drop(['Time', 'Amount', 'Class'], axis=1)
# y = np.array(data.Class.tolist())
# data = data.drop(['Time', 'Amount', 'Class'], axis=1)
# X = np.array(data.as_matrix())

# 进行数据切分
x_train,x_text,y_train,y_test=train_test_split(data,y,test_size=0.1,random_state=33)

# 逻辑回归模型创建
lg=LogisticRegression()
lg.fit(x_train,y_train)
predicted=lg.predict(x_text)

# 预测样本的置信分数
score_y=lg.decision_function(x_text)

# 计算混淆矩阵
cm=confusion_matrix(y_test,predicted)
class_name=[0,1]

# 显示混淆矩阵
plot_confusion_matrix(cm,classes=class_name,title='逻辑回归 混淆矩阵')

# 显示模型评估分数
show_metrics()

# 通过实际值和置信分数，计算精确值，召回率，阈值用于可视化，precision_recall_curve 函数会计算在不同概率阈值情况下的精确率和召回率，最后定义 plot_precision_recall 函数，绘制曲线
precision,recall,thresholds=precision_recall_curve(y_test,score_y)
print("precision: ",precision)
print("recall: ",recall)
# 绘制曲线
plot_precision_recall()


