## GridSearchCV的主要参数

### GridSearchCV(estimator, param_grid, cv=None, scoring=None) 

### estimator:
代表我们想要采用的分类器，如决策树，随机森林，SVM,kNN，朴素贝叶斯等等

### param_grid:
代表我们想要优化的参数和取值，输入的是字典或者列表形式

### cv：
交叉验证的折数，默认为None，代表使用三折交叉验证，也可以为整数代表的是交叉验证的折数。

### scoring：
准确度的评价标准，默认为None，也就是需要使用Score函数，可以设置具体的评价标准，比如accurary，f1等


### PS：

__我们在进行参数调优时，如果计算出来最优参数会发生变化，我们可以查看他的最优分数，如果最优分数相差不大，那表示我们的参数结果也相差不大，那我们选择其中一个即可__
