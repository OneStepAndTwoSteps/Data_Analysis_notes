#author py chen

# 使用load_digits数据集进行一个训练分类和预测分类结果显示

# 载入KNN分类器模块
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.preprocessing  import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

digits=load_digits()
data=digits.data
# print(digits.data[1])
# print(data.shape)

# 查看数据集中的key
# print(digits.keys())

# print(digits.images[0])
# print(digits.target)

# 切分数据
x_train,x_test,y_train,y_test=train_test_split(digits.data,digits.target,test_size=0.3,random_state=10)

# 数据规范化 Z-score
ss=StandardScaler()
train_x_ss=ss.fit_transform(x_train)
# print('train_x_ss: ',train_x_ss)
test_x_ss=ss.transform(x_test)
print(test_x_ss.shape)
print(test_x_ss[-1])
predict_data=test_x_ss[-1].reshape(1,64)
# exit()
# 绘图
# plt.gray()
# plt.imshow(digits.images[0])
# plt.show()


# 实例化KNN分类器
knn=KNeighborsClassifier()
knn.fit(train_x_ss,y_train)
# predicted=knn.predict(test_x_ss)
predicted=knn.predict(predict_data)
print(predicted)

# print("KNN的分类准确率：%.4lf"%accuracy_score(predicted,y_test))



# KNN的分类准确率：0.9667


# 预测结果 
# [5]

