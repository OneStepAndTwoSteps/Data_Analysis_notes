#author py chen

from sklearn.tree import  DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits


# 获取我们的数据
digits=load_digits()
data=digits.data

# 切分数据
x_train,x_test,y_train,y_test=train_test_split(data,digits.target,test_size=0.3)

# 数据归一化Z-score
ss=StandardScaler()
train_x_ss=ss.fit_transform(x_train)
test_x_ss=ss.transform(x_test)

# 建立决策树模型
model=DecisionTreeClassifier()
model.fit(train_x_ss,y_train)

# 模型预测
predicted=model.predict(test_x_ss)

# 输出准确率
print("决策树的准确率：%.4lf"%accuracy_score(predicted,y_test))

# 决策树的准确率：0.8611










