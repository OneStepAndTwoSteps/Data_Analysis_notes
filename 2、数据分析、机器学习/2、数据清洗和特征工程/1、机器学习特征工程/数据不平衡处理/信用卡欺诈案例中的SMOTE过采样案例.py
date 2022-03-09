#author py chen

import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

# 读取数据
credit_cards=pd.read_csv('creditcard.csv')

# 获取columns的列对象
columns=credit_cards.columns

# 使用delete函数指定删除列对象中的最后一列，也就是class标签
features_columns=columns.delete(len(columns)-1)
print("features_columns: ",features_columns)

# features就是出去class标签之外的数据
features=credit_cards[features_columns]

# label存储class标签
labels=credit_cards['Class']
print("label0: ",len(credit_cards[credit_cards['Class']==0]))
print("label1: ",len(credit_cards[credit_cards['Class']==1]))

# label0:  284315  此时的label0标签 正常交易数
# label1:  492     此时的label1标签 欺诈交易数


# 数据划分
features_train, features_test, labels_train, labels_test = train_test_split(features, 
                                                                            labels, 
                                                                            test_size=0.2, 
                                                                            random_state=0)
# 实例化 SMOTE
oversampler=SMOTE(random_state=0)
# 开始人工合成数据
os_features,os_labels=oversampler.fit_sample(features_train,labels_train)

# 查看生成结果
print("label1: ",len(os_labels[os_labels==1]))
print("label0: ",len(os_labels[os_labels==0]))

# label1:  227454 标签1：欺诈交易数 (欺骗标签也已经具备了和正常交易标签相同的数据量)
# label0:  227454 标签0：正常交易数   




