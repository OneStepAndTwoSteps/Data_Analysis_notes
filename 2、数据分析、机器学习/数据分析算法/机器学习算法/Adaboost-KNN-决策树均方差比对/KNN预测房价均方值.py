#author py chen
# 载入KNN分类器模块
from sklearn.neighbors import KNeighborsRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 加载房价数据
data=load_boston()
print(data.keys())

# 数据划分 训练集合测试集
X_train,X_test,Y_train,Y_test=train_test_split(data.data,data.target,test_size=0.3)

# 使用Adaboost回归模型：
regressor=KNeighborsRegressor()
regressor.fit(X_train,Y_train)

# 开始预测
predicted=regressor.predict(X_test)
mse=mean_squared_error(Y_test,predicted)

print("房价预测结果：",predicted)
# 打印均方误差，保留两位
print("KNN均方误差为：",round(mse,2))

#KNN均方误差为： 42.01
