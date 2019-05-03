#author py chen

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC,SVC
from sklearn import metrics

content=pd.read_csv('data.csv')
# print(pd.set_option('display.max_columns',None,'display.width',10))
pd.set_option('display.max_columns',None)
print(content.columns)
print('-'*30)
# print(len(content.columns))
# print(content.describe())
# print('-'*30)
# print(content.head())
# print('-'*30)

features_mean=content.columns[2:12]
features_se=content.columns[12:22]
features_worst=content.columns[22:32]

content.drop('id',axis=1,inplace=True)
content['diagnosis']=content['diagnosis'].map({'M':1,'B':0})


#可视化 content['diagnosis']
# sns.countplot(content['diagnosis'],label='count')
# plt.show()


# 热力图可视化特征之间的关系 corr函数建立content[features_mean]特征中的关系值
# 热力图中对角线上的为单变量自身的相关系数是 1。颜色越浅代表相关性越大。所以你能看出来 radius_mean、perimeter_mean 和 area_mean 相关性非常大，
# compactness_mean、concavity_mean、concave_points_mean 这三个字段也是相关的，因此我们可以取其中的一个作为代表。
# corr=content[features_mean].corr()
# plt.figure(figsize=(14,14))
# print(corr)
# sns.heatmap(corr,annot=True)
# plt.show()


# 特征选择的目的是降维，用少量的特征代表数据的特性，这样也可以增强分类器的泛化能力，避免数据过拟合。
# 我们能看到 mean、se 和 worst 这三组特征是对同一组内容的不同度量方式，我们可以保留 mean 这组特征，在特征选择中忽略掉 se 和 worst。
# 同时我们能看到 mean 这组特征中，radius_mean、perimeter_mean、area_mean 这三个属性相关性大，compactness_mean、daconcavity_mean、concave points_mean 这三个属性相关性大。
# 我们分别从这 2 类中选择 1 个属性作为代表，比如 radius_mean 和 compactness_mean。

# 特征选择 这样就将原来的10个特征变为了6个特征
features_remain = ['radius_mean','texture_mean', 'smoothness_mean','compactness_mean','symmetry_mean', 'fractal_dimension_mean']

# 保留所有特征 确实会提高准确率，但是这里提升准确率并不代表提取所有特征会比较好,如果特征数量很多的时候，容易过拟合
# features_remain = ['radius_mean', 'texture_mean', 'perimeter_mean',
#        'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
#        'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',]


# 准备训练集和测试集
x_train,x_test,y_train,y_test=train_test_split(content[features_mean],content['diagnosis'],test_size=0.3)

# 数据规范化
# 采用 Z-Score 规范化数据，保证每个特征维度的数据均值为 0，方差为 1
ss=StandardScaler()
train_x=ss.fit_transform(x_train)
test_x=ss.transform(x_test)

# 创建SVM分类器，默认kernel为高斯核函数rbf
model=SVC(kernel='rbf',C=2.0,gamma='auto')

# 使用线性核函数
# model=LinearSVC()

# 训练数据
model.fit(train_x,y_train)

# 测试数据集做预测
prediction=model.predict(test_x)

# 打印准确率
print("准确率：" ,metrics.accuracy_score(prediction,y_test))


# 输出结果：

  高斯核函数 SVM准确率 ： 0.9649122807017544
  线性核函数 SVM准确率 ： 0.9005847953216374
 


