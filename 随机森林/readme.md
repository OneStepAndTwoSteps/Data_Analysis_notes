### 随机森林模型的基本参数：
__模块：__

from sklearn.ensemble import RandomForestClassifier

__n_estimators:__   随机森林里决策树的个数 默认为10
__criterion:__      决策树分裂标准，默认是基尼系数(CART算法)，也可以选择entropy(ID3算法)
__max_depath:__     决策树的最大深度，默认是None，也就是不限制决策树的深度，也可以设置一个整数限制决策树的最大深度。
__n_jobs:__         拟合和预测的时候CPU的核数，默认是1，也可以是整数，-1表示CPU有多少个核心，就启动多少job
