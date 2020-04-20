# cross_val_score 交叉验证

使用交叉验证的最简单方法是cross_val_score在估算器和数据集上调用辅助函数。

## cross_val_score 的使用

    cross_val_score(estimator, X, y=None, groups=None, scoring=None, cv=None, n_jobs=1, verbose=0, fit_params=None, pre_dispatch='2*n_jobs')

### 参数介绍

[➡➡ scoring 参数官网链接 ⬅⬅](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter) 

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
            mean_squared_error’ sklearn.metrics.mean_squared_error
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


## 回归 `scoring`

`neg_mean_squared_error`  (负均方误差函数)

*   `neg_mean_squared_error` 转为 `rmse` :

        rmse = np.sqrt(-cross_val_score(model, X, y, cv=5, scoring='neg_mean_absolute_error'))


`neg_mean_absolute_error` (绝对值和的平均)



## `cross_val_score` 负分的表示含义

### 问：

在cross_val_score进行计算得分时，使用随机森林回归 决策树回归 线性回归 adaboost等这些回归算法会出现了负数的情况，那么为什么会出现负数的情况，还有这些负数如何评价模型的好坏呢？

### 答：

__这是因为我们用回归一般都是用MSE RMSE 这些评估的__ ，这些值的目标是最小化损失函数，而我们的目标是最大化评估分数，所以sklearn会加上一个负号表示打分。所以这些负数里数值越大模型越好，比如-1比-2好。

也就是：`误差函数越大，模型越不好，所以Python自动在前面加 - 号， 越大表示误差越小，模型越好`

### 解
(我的想法是这样：RMSE 可以得到样本的均方根误差 因为损失函数越小越好，但是我们的目标要最大化评估分数，所以评估分数要越高越好，所以加上一个负号之后 1 就变成 -1 ， 2 变成 -2 ，在损失函数看来 1 比 2 好，在评估分数看来 -1 比 -2好。)

### 续
-《[RMSE 和 MSE 这两个指标都是描述真实值和预测值之间的误差的度量:点击了解 RMSE MSE](https://github.com/OneStepAndTwoSteps/Data_Analysis_notes/blob/master/1%E3%80%81%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E7%9B%B8%E5%85%B3%E5%BA%93%E4%BD%BF%E7%94%A8/Sklearn%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%BA%93/metrics/%E6%A8%A1%E5%9E%8B%E8%AF%84%E4%BC%B0/%E5%9B%9E%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E8%AF%84%E4%BC%B0%E6%8C%87%E6%A0%87/MAE%E3%80%81MSE%E3%80%81RMSE%20%E5%92%8C%20RMSLE%E6%8C%87%E6%A0%87.md)》


