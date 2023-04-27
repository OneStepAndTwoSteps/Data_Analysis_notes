#author py chen

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import  DecisionTreeClassifier
from  sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import accuracy_score

train_data=pd.read_csv('Titanic_Data-master/train.csv')

print("数据处理前train_data的信息: \n")
print(train_data.info())
print('-'*30)


train_data['Age'].fillna(round(train_data['Age'].mean(),0),inplace=True)
age_mean=round(train_data['Age'].mean(),0)
print(round(train_data['Age'].mean(),0))

train_data['Embarked'].fillna('S', inplace=True)

print("数据处理后train_data的信息: \n")
print(train_data.info())
print('-'*30)

features=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
train_features=train_data[features]
train_label=train_data['Survived']


# 通常情况下，特征值不都是数值类型，可以使用 DictVectorizer 类进行转化；
dvec=DictVectorizer(sparse=False)

# 打印一下将特征转化为字典之后的数据
print(train_features.to_dict(orient='record'))

# 将 train_features 转化为列表套字典格式进行训练 如 [{},{},{}.....]
new_train_features=dvec.fit_transform(train_features.to_dict(orient='record'))

# feature_names_: 一个包含所有特征名称的，长度为特征名称个数的列表。
# print(dvec.feature_names_)

# 特征名称和特征列索引的映射字典。
# print(dvec.vocabulary_)

np.set_printoptions(threshold=np.inf)

# 此时已然将特征值映射为矩阵了
# print(new_train_features)

# inverse_transform可以将特征矩阵还原成原始数据 可以对比一下 print(train_features.to_dict(orient='record')) 和下面的输出，有些区别，但是几乎一致。
# 如果数据像下面的D应该就没问题了。
print(dvec.inverse_transform(new_train_features))

# 可以查看是否完全还原正确
# print(dvec.inverse_transform(new_train_features) == train_features.to_dict(orient='record'))

'''
v = DictVectorizer(sparse=False)
D = [{"foo": 1, "bar": 2}, {"foo": 3, "baz": 1}]

# 对字典列表D进行转换，转换成特征矩阵
X = v.fit_transform(D)
# 特征矩阵的行代表数据，列代表特征，0表示该数据没有该特征
print(X)

# inverse_transform可以将特征矩阵还原成原始数据
print(v.inverse_transform(X) == D)

'''