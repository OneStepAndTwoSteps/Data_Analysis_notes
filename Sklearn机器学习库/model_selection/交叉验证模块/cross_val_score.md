## cross_val_score 交叉验证

使用交叉验证的最简单方法是cross_val_score在估算器和数据集上调用辅助函数。

### cross_val_score的使用

    cross_val_score(estimator, X, y=None, groups=None, scoring=None, cv=None, n_jobs=1, verbose=0, fit_params=None, pre_dispatch='2*n_jobs')

#### 参数介绍

    estimator:实现'适合'的估算器对象用于拟合数据的对象。(机器学习算法模型)

    X:训练集

　　y：训练集的目标值

    scoring:评测模型的打分标准，scoring可调用的对应的函数名称如下： 
        
        分类：
        　 ‘accuracy’sklearn.metrics.accuracy_score
    　　　　‘average_precision’sklearn.metrics.average_precision_score
    　　　　‘f1’sklearn.metrics.f1_score f1就是F-measure
    　　　　‘precision’sklearn.metrics.precision_score
    　　　　‘recall’sklearn.metrics.recall_score
    　　　　‘roc_auc’sklearn.metrics.roc_auc_score

        回归：
            mean_squared_error’sklearn.metrics.mean_squared_error
    　　　　‘r2’sklearn.metrics.r2_score
    　　　　neg_mean_absolute_error
    　　　　neg_mean_squared_error
    　　　　neg_median_absolute_error：参考http://blog.csdn.net/lipe12/article/details/51200510
        
        聚类：
            ‘adjusted_rand_score’sklearn.metrics.adjusted_rand_score


    cv：int，交叉验证生成器或可迭代的，可选的确定交叉验证拆分策略。cv的可能输入是：
    无，使用默认的3倍交叉验证，整数，用于指定a中的折叠数(Stratified)KFold，要用作交叉验证生成器的对象。

    简单来说如果cv参数不指定或者指定为整数则使用StratifiedKFold。在所有其他情况下，使用KFold。

    n_jobs： cpu核数


    pre_dispatch：控制总执行任务数量，以防止任务数量超过CPU数量，将内存消耗殆尽。
　　　　　　　　　　None：不做任务量限制，任务产生就执行。
　　　　　　　　　　int 值：限制总并行执行的最大任务数。


### cross_val_score 负分的表示含义

在cross_val_score进行计算得分时，使用随机森林回归 决策树回归 线性回归 adaboost等这些回归算法会出现了负数的情况，那么为什么会出现负数的情况，还有这些负数如何评价模型的好坏呢？

__这是因为我们用回归一般都是用MSE RMSE这些评估的，这些值的目标是最小化损失函数，而我们的目标是最大化评估分数，所以sklearn会加上一个负号表示打分。所以这些负数里数值越大模型越好，比如-1比-2好。__ (我的想法是这样：因为损失函数越小越好，但是我们的目标要最大化评估分数，所以评估分数要越高越好，所以加上一个负号之后 1 就变成 -1 ， 2 变成 -2 在损失函数看来 1 比 2 好，在评估分数看来 -1 比 -2好)

#### 小结

我们可以看出在测试集中，我们的 StratifiedKFold 0和1标签的比例是1：1，而KFold没有。

