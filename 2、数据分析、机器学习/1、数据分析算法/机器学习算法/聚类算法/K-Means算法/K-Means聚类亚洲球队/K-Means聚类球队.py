#author py chen
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler,StandardScaler
import pandas as pd
import numpy as np

# 取出数据
data=pd.read_csv('data.csv',encoding='gbk')
# print(data.head())
train_x=data[['2019年国际排名','2018世界杯','2015亚洲杯']]
# print(train_x)

# 数据归一化
ss=StandardScaler()
mm=MinMaxScaler()
train_x_mm=mm.fit_transform(train_x)
train_x_ss=ss.fit_transform(train_x)
# a=pd.concat((data['国家'],pd.DataFrame(train_x_mm)),axis=1)
# print(a)

# 创建K-Means
km1=KMeans(n_clusters=3)
km2=KMeans(n_clusters=5)

km1.fit(train_x_mm)
km2.fit(train_x_ss)
predicted1=km1.predict(train_x_mm)
predicted2=km2.predict(train_x_ss)

# 合并聚类结果到原数据中
result1=pd.concat((data,pd.DataFrame(predicted1)),axis=1)
result2=pd.concat((data,pd.DataFrame(predicted2)),axis=1)
result1.rename({0:'聚类'},axis=1,inplace=True)
result2.rename({0:'聚类'},axis=1,inplace=True)
print(result1)
print(result2)

