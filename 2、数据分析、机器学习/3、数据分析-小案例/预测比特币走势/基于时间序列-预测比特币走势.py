#author py chen

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARMA
import numpy as np
from datetime import datetime
import warnings
from itertools import  product

# 过滤warning
warnings.filterwarnings('ignore')

# 读取数据
data=pd.read_csv('bitcoin_2012-01-01_to_2018-10-31.csv',encoding='utf-8')
print(data.head())

# 将时间作为data的index，之后使用resample来进行数据压缩时需要用到
# pd.to_datetime 将参数转换为datetime。
data.index=pd.to_datetime(data.Timestamp)

#使用resample对时间序列进行重采样，根据时间粒度的变大或者变小分为降采样和升采样
# 按月
data_month=data.resample('M',how='mean')
# 按季度
data_Q=data.resample('Q-DEC',how='mean')
# 按年
data_year=data.resample('A-DEC',how='mean')


# 可视化按天、月、季度、年的历史比特币走势
fig=plt.figure(figsize=[15,7])
# fig,ax1=plt.subplots(2,2,figsize=(15,7))
plt.rcParams['font.sans-serif']=['SimHei']
plt.suptitle('比特币金额(美金)',fontsize=20)
plt.subplot(2,2,1)
# 前面如果定义了子图和子图的大小，这里的figsize=[15,7]会失效
data['Weighted_Price'].plot(kind = "line",style='-',label='按天',figsize=[15,7],legend=True)
# plt.plot(data['Weighted_Price'],'-',label='按天')
plt.subplot(2,2,2)
plt.plot(data_month['Weighted_Price'],'-',label='按月')
# 设置图例位置，不带参数调用 legend 会自动获取图例句柄及相关标签，这里加上legend表示显示label
plt.legend()
plt.subplot(2,2,3)
plt.plot(data_Q['Weighted_Price'],'-',label='按季')
plt.legend()
plt.subplot(2,2,4)
plt.plot(data_year['Weighted_Price'],'-',label='按年')
plt.legend()
plt.show()

# 设置p和q的参数范围
p=range(0,3)
q=range(0,3)

# 使用itertools的product模块，轮询p和q的参数
parameters=product(p,q)
print(parameters)
parameters_list=list(parameters)

# 寻找最优ARMA模型即best_aic最小
results=[]
# 设置best_aic大小为正无穷
best_aic=float('inf')

# 开始训练模型，寻找最优参数
for param in parameters_list:
    try :
        arma=ARMA(data_month['Weighted_Price'],order=(param[0],param[1])).fit()

    except:
        print("参数错误：",param)
        continue

    aic=arma.aic
    if aic < best_aic:
        best_arma=arma
        best_aic=aic
        best_param=param

    results.append([param,aic])

# 输出最优模型
# 将results转化成DataFrame
result_table=pd.DataFrame(results)
result_table.columns=['parameters','aic']
print(result_table.head())
print("最优模型：" ,best_arma.summary())

# 比特币预测,主要这里用的是[[]]
data_month2=data_month[['Weighted_Price']]
print(data_month2)
# 预测的时间
date_list=[datetime(2018, 11, 30), datetime(2018, 12, 31), datetime(2019, 1, 31), datetime(2019, 2, 28), datetime(2019, 3, 31),
             datetime(2019, 4, 30), datetime(2019, 5, 31), datetime(2019, 6, 30)]
# 将date_list作为index和data_month.columns做为列进行组合成一个新的DataFrame 这里没有使用columns.values只是取列名
feature=pd.DataFrame(index=date_list,columns=data_month.columns)
print("feature: ",feature)
# 将data_month2和feature进行拼接
data_month2=pd.concat([data_month2,feature])
print("data_month2: ",data_month2)
data_month2['forecast']=best_arma.predict(start=0,end=91)

# 预测结果可视化显示
plt.figure(figsize=(15,7))
plt.plot(data_month['Weighted_Price'],label="真实金额")
plt.plot(data_month2['forecast'],'r--',label="预测金额")
# 将标签显示出来
plt.legend()
plt.title('比特币金额(美金)/月')
plt.xlabel('时间')
plt.ylabel('金额')
plt.show()


# best_arma.summary()输出结果：
# 最优模型：                               ARMA Model Results                              
# ==============================================================================
# Dep. Variable:         Weighted_Price   No. Observations:                   83
# Model:                     ARMA(1, 1)   Log Likelihood                -688.761
# Method:                       css-mle   S.D. of innovations            957.767
# Date:                Sun, 09 Jun 2019   AIC                           1385.522
# Time:                        16:11:05   BIC                           1395.198
# Sample:                    12-31-2011   HQIC                          1389.409
#                          - 10-31-2018                                         
# ========================================================================================
#                            coef    std err          z      P>|z|      [0.025      0.975]
# ----------------------------------------------------------------------------------------
# const                 2086.7482   1565.424      1.333      0.186    -981.427    5154.923
# ar.L1.Weighted_Price     0.9251      0.042     22.046      0.000       0.843       1.007
# ma.L1.Weighted_Price     0.2681      0.116      2.311      0.023       0.041       0.495
#                                     Roots                                    
# =============================================================================
#                   Real          Imaginary           Modulus         Frequency
# -----------------------------------------------------------------------------
# AR.1            1.0810           +0.0000j            1.0810            0.0000
# MA.1           -3.7296           +0.0000j            3.7296            0.5000
# -----------------------------------------------------------------------------



