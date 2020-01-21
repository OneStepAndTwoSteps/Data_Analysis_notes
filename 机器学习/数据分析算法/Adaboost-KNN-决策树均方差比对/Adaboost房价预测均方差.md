
#author py chen
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import AdaBoostRegressor
from sklearn.datasets import load_boston

# 加载房价数据
data=load_boston()
print(data.keys())

# 数据划分 训练集合测试集
X_train,X_test,Y_train,Y_test=train_test_split(data.data,data.target,test_size=0.3)

# 使用Adaboost回归模型：
regressor=AdaBoostRegressor()
regressor.fit(X_train,Y_train)

# 开始预测
predicted=regressor.predict(X_test)

# 计算均方误差
mse=mean_squared_error(Y_test,predicted)

print("房价预测结果：",predicted)
# 打印均方误差，保留两位
print("Adaboost算法均方误差为：",round(mse,2))

# Adaboost算法均方误差为： 16.42


