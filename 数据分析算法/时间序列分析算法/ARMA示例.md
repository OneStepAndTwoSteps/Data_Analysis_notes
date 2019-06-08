#author py chen
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARMA
import matplotlib.pyplot as plt
import warnings

# 过滤warning
warnings.filterwarnings('ignore')

# 创建数据，每一个数据对应到一个年份
data = [5922, 5308, 5546, 5975, 2704, 1767, 4111, 5542, 4726, 5866, 6183, 3199, 1471, 1325, 6618, 6644, 5337, 7064, 2912, 1456, 4705, 4579, 4990, 4331, 4481, 1813, 1258, 4383, 5451, 5169, 5362, 6259, 3743, 2268, 5397, 5821, 6115, 6631, 6474, 4134, 2728, 5753, 7130, 7860, 6991, 7499, 5301, 2808, 6755, 6658, 7644, 6472, 8680, 6366, 5252, 8223, 8181, 10548, 11823, 14640, 9873, 6613, 14415, 13204, 14982, 9690, 10693, 8276, 4519, 7865, 8137, 10022, 7646, 8749, 5246, 4736, 9705, 7501, 9587, 10078, 9732, 6986, 4385, 8451, 9815, 10894, 10287, 9666, 6072, 5418]

# 转化成series格式 index values
data=pd.Series(data)

# sm.tsa.datetools.dates_from_range 转换日期字符串序列并返回日期时间列表(返回格式为列表)。参数 开始(str:1901) 结束(str:1990) 长度(None)
data_index=sm.tsa.datetools.dates_from_range('1901','1990')
# 返回的 datetime.datetime(1901, 12, 31, 0, 0) 表示1901年12月31号0点0分
print(data_index)

# 从series对象中找到某元素（行）对应的索引,将pd.Index(data_index)设置为data的index
print(pd.Index(data_index))
data.index=pd.Index(data_index)
print(data)

# 绘制数据图
data.plot(figsize=(12,8))
plt.show()

# 创建ARMA模型,(7,0) 代表 (p,q) 的阶数。
arma=ARMA(data,(7,0)).fit()
# AIC 准则，也叫作赤池消息准则，它是衡量统计模型拟合好坏的一个标准，数值越小代表模型拟合得越好。
print('AIC: %0.4lf'%arma.aic)

# 模型预测,预测1990-2000年的走势
predicted=arma.predict('1990','2000')

# 预测结果绘图
fig, ax = plt.subplots(figsize=(12, 8))
# ax = ax表示在ax这个子图上画图形
ax = data.ix['1901':].plot(ax=ax)
# 同理在ax这个子图上画图
predicted.plot(ax=ax)
plt.show()

''' 还不清楚的话可以借鉴这段被注释的代码
fig,(ax1,ax2)=plt.subplots(2,1,figsize=(12,9))
ax1=data.ix['1901':].plot(ax=ax1)
predicted.plot(ax=ax1)
plt.show()
'''


#out: AIC: 1619.6323






