#author py chen

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv("creditcard.csv")
data.head()


count_classes = pd.value_counts(data['Class'], sort = True).sort_index()
print(count_classes)
count_classes.plot(kind = 'bar')
plt.title("Fraud class histogram")
plt.xlabel("Class")
plt.ylabel("Frequency")

from sklearn.preprocessing import StandardScaler

data['normAmount'] = StandardScaler().fit_transform(data['Amount'].values.reshape(-1, 1))
data = data.drop(['Time','Amount'],axis=1)
data.head()

# 下采样方法:
# 将列名不为Class的数据取出作为我们的特征数据
X = data.ix[:, data.columns != 'Class']
# 将列名为Class的数据取出作为我们的标签
y = data.ix[:, data.columns == 'Class']


# 计算出欺骗信息的样本有多少个
number_records_fraud = len(data[data.Class == 1])
# 得到欺骗信息的样本的索引 
fraud_indices = np.array(data[data.Class == 1].index)
# print("fraud_indices: ",fraud_indices)

# 正常交易样本的index
normal_indices = data[data.Class == 0].index


# 通过随机选择的方法来对我们的数据进行随机选择 choice(对什么数据进行随机选择，随机的选择多少个，replace是否进行代替)
random_normal_indices = np.random.choice(normal_indices, number_records_fraud, replace = False)
random_normal_indices = np.array(random_normal_indices)
# print("random_normal_indices: ",random_normal_indices)

# index进行合并
under_sample_indices = np.concatenate([fraud_indices,random_normal_indices])
# print("under_sample_indices: ",under_sample_indices)

# Under sample dataset 就是我们下采样的数据了
# iloc基于索引或者列索引进行匹配，下面这一行代码最终取出的就是我们所以中的所有数据(可以看loc和iloc的用法)
under_sample_data = data.iloc[under_sample_indices,:]
print("data.iloc[under_sample_indices,:]: ",len(data.iloc[under_sample_indices,:]))

# ix是结合loc和iloc的混合所以，可以使用行/列标签进行定位也可以通过行/列的index进行定位
X_undersample = under_sample_data.ix[:, under_sample_data.columns != 'Class']
y_undersample = under_sample_data.ix[:, under_sample_data.columns == 'Class']

# Showing ratio
print("Percentage of normal transactions: ", len(under_sample_data[under_sample_data.Class == 0])/len(under_sample_data))
print("Percentage of fraud transactions: ", len(under_sample_data[under_sample_data.Class == 1])/len(under_sample_data))
print("Total number of transactions in resampled data: ", len(under_sample_data))


# 输出结果：

data.iloc[under_sample_indices,:]:  984
Percentage of normal transactions:  0.5
Percentage of fraud transactions:  0.5
Total number of transactions in resampled data:  984

# 此时我们已经将我们数据量大的类别进行裁剪，使得我们的两种类别数量一致



