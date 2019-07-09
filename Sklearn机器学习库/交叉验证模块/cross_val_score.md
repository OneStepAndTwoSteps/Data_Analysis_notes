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

### StratifiedKFold和KFold的主要区别

StratifiedKFold用法类似Kfold，但是他是分层采样，确保训练集，测试集中各类别样本的比例与原始数据集中相同。

__举个例子：__

    import numpy as np
    from sklearn.model_selection import StratifiedKFold,KFold

    X=np.array([
        [1,2,3,4],
        [11,12,13,14],
        [21,22,23,24],
        [31,32,33,34],
        [41,42,43,44],
        [51,52,53,54],
        [61,62,63,64],
        [71,72,73,74]
    ])

    y=np.array([1,1,0,0,1,1,0,0])


__KFold:__

    #按顺序分别取第1-2、3-4、5-6和7-8的数据。
    kfolder = KFold(n_splits=4,random_state=1)
    for train, test in kfolder.split(X,y):
    print('Train: %s | test: %s' % (train, test),'\n')

__out__

    Train: [2 3 4 5 6 7] | test: [0 1] 

    Train: [0 1 4 5 6 7] | test: [2 3] 

    Train: [0 1 2 3 6 7] | test: [4 5] 

    Train: [0 1 2 3 4 5] | test: [6 7] 


__KFold:__

    #依照标签的比例来抽取数据，本案例集标签0和1的比例是1：1
    #因此在抽取数据时也是按照标签比例1：1来提取的
    sfolder = StratifiedKFold(n_splits=4,random_state=1)
    for train, test in sfolder.split(X,y):
    print('Train: %s | test: %s' % (train, test))

__out__

    Train: [1 3 4 5 6 7] | test: [0 2]  # 0对应上面的标签1 2对应上面的标签0

    Train: [0 2 4 5 6 7] | test: [1 3]

    Train: [0 1 2 3 5 7] | test: [4 6]

    Train: [0 1 2 3 4 6] | test: [5 7]


#### 小结

我们可以看出在测试集中，我们的 StratifiedKFold 0和1标签的比例是1：1，而KFold没有。

