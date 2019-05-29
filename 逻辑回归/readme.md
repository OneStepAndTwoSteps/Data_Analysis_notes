### sklearn中的逻辑回归

from sklearn.liner_model import LogisticRegression

### 主要参数介绍：

__penalty:__ 惩罚项，取值为l1或者l2，默认为l2。当模型满足高斯分布时，使用l2，当模型参数满足拉普拉斯分布时，使用l1。

__solver:__ 代表的是逻辑回归损失函数的优化方法。有五个参数可选，分别为liblinear、lbfgs、newton-cg、sag和saga。默认为liblinear，适用于数据量小的数据集，当数据量很大时可以选用sag或者saga方法。

__max_iter:__ 算法收敛的最大迭代次数，默认为10。

__n_jobs:__ 拟合和预测的时候cpu的核数，默认是1，也可以是整数，如果是-1表示使用机器所有的cpu核数。




