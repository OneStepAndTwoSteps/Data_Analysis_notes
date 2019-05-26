#author py chen
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import matplotlib.pyplot  as plt
import seaborn as sns

# 加载数据
data=pd.read_csv('UCI_Credit_Card.csv',encoding='utf-8')

# 查看数据的形状
print(data.shape)

# 取出下个月信用卡是否违约的数据，进行一个可视化展示，展示违约人数和未违约人数 (如果数据不平均可以使用一：下采样策略 二：过采样策略，这里不展开)
# 取出 default.payment.next.month 下面的行，并且按照 值 进行排序
next_mouth=data['default.payment.next.month'].value_counts()
print(next_mouth)

# 构建一个dataframe里面存储 违约的和 守约的数据
'''
Name: default.payment.next.month, dtype: int64
   default.payment.next.month_index  values
0                                 0   23364
1                                 1    6636
'''
df2=pd.DataFrame({'default.payment.next.month_index':next_mouth.index,'values':next_mouth.values})
print(df2)

# 使得画出来的图的标签支持中文标签
plt.rcParams['font.sans-serif']=['SimHei']
# 设置图像大小
plt.figure(figsize=(6,6))
# 标题
plt.title('信用卡违约客户\n (0:违约 1:守约)')
# seaborn调色板
sns.set_color_codes('pastel')
# 设置画图格式
sns.barplot(x=df2['default.payment.next.month_index'],y=df2['values'],data=df2)
# 获取当前位置和标签：
loc,labels=plt.xticks()
plt.show()

# 开始进行正式内容
# 去除没有必要的特征 如数据中的ID字段
data.drop(columns=['ID'],inplace=True)

# 提取出target，作为标签
target=data['default.payment.next.month'].values

# 删除数据中的 default.payment.next.month_index 标签，其余字段作为我们的训练数据
data.drop(columns=['default.payment.next.month'],inplace=True)
# columns=data.columns.values.tolist()
# columns.remove('default.payment.next.month')
# features=data[columns].values
print(data.values)
# print(features)

# 数据集的划分 参数stratify： 依据标签target，按原数据target中各类比例，分配给train和test，使得train和test中各类数据的比例与原数据集一样。
x_train,x_test,y_train,y_test=train_test_split(data.values,target,test_size=0.3,stratify=target,random_state=1)

# 创建各种分类器
classifier=[
    SVC(random_state=1,kernel='rbf'),
    DecisionTreeClassifier(random_state=1,criterion='gini'),
    RandomForestClassifier(random_state=1, criterion='gini'),
    KNeighborsClassifier(metric='minkowski')
]

# 创建分类器的名字
classifier_name=['svc','decisiontreeclassifier','randomforestclassifier','kneighborsclassifier']

# 设置需要调节的参数
classifier_params_grid=[
    {'svc__C':[1],'svc__gamma':[0.01]},
    {'decisiontreeclassifier__max_depth':[5,7,9,10]},
    {'randomforestclassifier__max_depth':[5,7,9,10]},
    {'kneighborsclassifier__n_neighbors':[4,6,8,10]}
]

# 对分类器进行参数调优
def GridSeachCV_params_work(pipeline,x_train,x_test,y_train,y_test,param_grid,score='accuracy'):
    response={}
    gridsearch=GridSearchCV(estimator=pipeline,param_grid=param_grid,scoring=score)
    # 开始寻找最优参数
    search=gridsearch.fit(x_train,y_train)
    print("最优分数： %.4lf" %search.best_score_)
    print("最优参数： %s" %search.best_params_)
    # 使用最优参数进行分类
    predicted=gridsearch.predict(x_test)
    print('准确率：%.4lf' %accuracy_score(y_test,predicted))

    # 填充返回的response
    response['predicted']=predicted
    response['accuracy_score']=accuracy_score(y_test,predicted)
    return response

# 构造pipeline
for model_name,model,model_params_grid in zip(classifier_name,classifier,classifier_params_grid):
    pipeline=Pipeline([
        ('scaler',StandardScaler()),
        (model_name,model)
    ])
    result=GridSeachCV_params_work(pipeline,x_train,x_test,y_train,y_test,model_params_grid,score='accuracy')


# 结果：
# svm分类器
# 最优分数： 0.8174
# 最优参数： {'svc__C': 1, 'svc__gamma': 0.01}
# 准确率：0.8172

# 决策树分类器
# 最优分数： 0.8189
# 最优参数： {'decisiontreeclassifier__max_depth': 5}
# 准确率：0.8170

# 随机森林
# 最优分数： 0.8206
# 最优参数： {'randomforestclassifier__max_depth': 5}
# 准确率：0.8177

# KNN分类器
# 最优分数： 0.8043
# 最优参数： {'kneighborsclassifier__n_neighbors': 10}
# 准确率：0.8067


