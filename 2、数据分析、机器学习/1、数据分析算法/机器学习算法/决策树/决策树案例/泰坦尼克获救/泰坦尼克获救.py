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
# test_data=pd.read_csv('Titanic_Data-master/test.csv')
# df1.rename(columns={'PassengerId':'	乘客编号','Survived	':'是否幸存','Pclass':'船票等级','Name':'乘客姓名','Sex':'乘客性别','SibSp':'亲戚数量（兄妹、配偶数）','Parch':'亲戚数量（父母、子女数）','Ticket':'船票号码','Fare	':'船票价格','Cabin	':'船舱','Embarked':'登录港口'},inplace=True)

print("数据处理前train_data的信息: \n")
print(train_data.info())
print('-'*30)
#
# print("数据处理前test_data的信息: \n")
# print(test_data.info())
# print('-'*30)

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
# test_features=train_features[features]

# 特征值里有一些是字符串，这样不方便后续的运算，需要转成数值类型，比如 Sex 字段，有 male 和 female 两种取值。我们可以把它变成 Sex=male 和 Sex=female 两个字段，数值用 0 或 1 来表示。
# 通常情况下，特征值不都是数值类型，可以使用 DictVectorizer 类进行转化
dvec=DictVectorizer(sparse=False)
train_features=dvec.fit_transform(train_features.to_dict(orient='record'))

# 建立決策樹模型
data_train,data_test,label_train,label_test=train_test_split(train_features,train_label,test_size=0.1,random_state=42)

clf=DecisionTreeClassifier(criterion='entropy',random_state=42)

clf.fit(data_train,label_train)
print(clf.score(data_test, label_test))
# 用 CART 分类树做预测
test_predict = clf.predict(data_test)
score = accuracy_score(label_test, test_predict)
print("CART 分类树准确率 %.4lf" % score)

