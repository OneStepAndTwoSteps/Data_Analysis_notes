#author py chen
from sklearn.metrics import zero_one_loss
from sklearn.ensemble import AdaBoostClassifier
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import matplotlib.pyplot as plt

# 设置Adaboost的迭代次数(同时也是分类器的个数，每次迭代都会新生成一个分类器)
n_estimators=200

# 使用sklearn中的make_hastie_10_2函数生成二分类数据集,数据集中样本个数为n_samples指定个数
x,y=datasets.make_hastie_10_2(n_samples=12000,random_state=1)

# 从数据集中提取前2000行作为测试集，其余作为训练集
train_x,train_y=x[:2000],y[:2000]
test_x,test_y=x[2000:],y[2000:]

#创建弱分类器
dt_stump=DecisionTreeClassifier(max_depth=1,min_samples_leaf=1)
dt_stump.fit(train_x,train_y)
dt_stump_err=1.0-dt_stump.score(test_x,test_y)

# 决策树分类
dt=DecisionTreeClassifier()
dt.fit(train_x,train_y)
dt_err=1.0-dt.score(test_x,test_y)

# Adaboost分类器,指定弱分类器为 dt_stump，迭代次数为n_estimators
adaboost=AdaBoostClassifier(base_estimator=dt_stump,n_estimators=n_estimators)
adaboost.fit(train_x,train_y)

# 可视化三个分类器的错误率
fig=plt.figure()
# 设置plt正确显示中文
plt.rcParams['font.sans-serif']=['SimHei']
ax=fig.add_subplot(111)
ax.plot([1,n_estimators],[dt_stump_err]*2,'k-',label='决策树弱分类器错误率')
ax.plot([1,n_estimators],[dt_err]*2,'k--',label='决策树分类器错误率')
adaboost_err=np.zeros((n_estimators,))
# 遍历每次迭代结果 i为迭代次数，y为预测结果
for i,y in enumerate(adaboost.staged_predict(test_x)):
    # 统计错误率
    adaboost_err[i]=zero_one_loss(y,test_y)

# 绘制每次迭代的Adaboost错误率
ax.plot(np.arange(n_estimators)+1,adaboost_err,label='Adaboost错误率',color='red')
ax.set_xlabel('迭代次数')
ax.set_ylabel('错误率')
leg=ax.legend(loc='upper right',fancybox=True)
plt.show()




