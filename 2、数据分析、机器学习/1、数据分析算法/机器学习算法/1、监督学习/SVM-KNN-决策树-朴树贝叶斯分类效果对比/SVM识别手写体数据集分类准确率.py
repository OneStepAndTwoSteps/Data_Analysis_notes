
#author py chen

from sklearn.svm import SVC,LinearSVC
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
# 提取数据信息
digits=load_digits()
data=digits.data

# 划分数据
x_train,x_test,y_train,y_test=train_test_split(data,digits.target,test_size=0.3)

# 数据归一化Z-score
ss=StandardScaler()
train_x_ss=ss.fit_transform(x_train)
test_x_ss=ss.transform(x_test)

# 建立模型 默认SVC是高斯核函数
model_svc=SVC()
model_svc.fit(train_x_ss,y_train)

# 建立模型 线性svm
model_linersvc=LinearSVC()
model_linersvc.fit(train_x_ss,y_train)


# 预测模型
predicted=model_svc.predict(test_x_ss)
predicted2=model_linersvc.predict(test_x_ss)

# 查看预测准确率
print('高斯核函数的准确率：%.4lf'%accuracy_score(predicted,y_test))
print('线性SVM的准确率：%.4lf'%accuracy_score(predicted2,y_test))

# 高斯核函数的准确率：0.9778
# 线性SVM的准确率：0.9500









