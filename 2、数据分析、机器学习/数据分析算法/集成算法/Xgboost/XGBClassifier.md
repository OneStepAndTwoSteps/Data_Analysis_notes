# XGBClassifier

import xgboost as xgb

## `gini系数`

[Gini Coefficient - An Intuitive Explanation](https://www.kaggle.com/batzner/gini-coefficient-an-intuitive-explanation)

### `方案1：`

    from numba import jit    

[`1、定义基尼系数：`](https://www.kaggle.com/cpmpml/extremely-fast-gini-computation)

    @jit
    def eval_gini(y_true, y_prob):
        y_true = np.asarray(y_true)
        y_true = y_true[np.argsort(y_prob)]
        ntrue = 0
        gini = 0
        delta = 0
        n = len(y_true)
        for i in range(n-1, -1, -1):
            y_i = y_true[i]
            ntrue += y_i
            gini += y_i * delta
            delta += 1 - y_i
        gini = 1 - 2 * gini / (ntrue * (n - ntrue))
        return gini


[`2、定义 xgb gini 系数：`](https://www.kaggle.com/ogrellier/xgb-classifier-upsampling-lb-0-283)




    def gini_xgb(preds, dtrain):
        labels = dtrain.get_label()
        gini_score = -eval_gini(labels, preds)
        return [('gini', gini_score)]

`3、调用：`

    xgb_model = xgb.train(params, d_train, nrounds, watchlist, early_stopping_rounds=100, 



### `方案2：`

`1、定义基尼系数：`

    def gini(y, pred):
        g = np.asarray(np.c_[y, pred, np.arange(len(y)) ], dtype=np.float)
        g = g[np.lexsort((g[:,2], -1*g[:,1]))]
        gs = g[:,0].cumsum().sum() / g[:,0].sum()
        gs -= (len(y) + 1) / 2.
        return gs / len(y)

`2、定义 xgb gini 系数：`

    # 返回一个 normalized 后的 gini 分数
    def gini_xgb(pred, y):
        y = y.get_label()
        return 'gini', gini(y, pred) / gini(y, y)


`3、调用：`

    # xgb.train 中的 feval 参数可以用于指定评估方法，这里我们使用自定义的 gini_xgb 使用gini系数来进行评估
    xgb_model = xgb.train(params, d_train, nrounds, watchlist, early_stopping_rounds=100, 
                            feval=gini_xgb, maximize=True, verbose_eval=100)


### `对于基尼系数的分数`

根据 ROC 曲线来评估分类器

分类质量可以使用 ROC 曲线下面的面积大小来计算衡量，这个曲线下的面积就是 AUC 系数。

AUC 系数越高越好。AUC = 1 意味着这是一个完美的分类器，我们把所有的东西都分类准确了。对于纯随机数的分类，我们的 AUC = 0.5。如果 AUC < 0.5，那么意味着这个分类器的性能比随机数还要差。

这里再说一个概念：基尼系数（Gini Coefficient），GC = 2 * AUC - 1。基尼系数越高，代表模型的效果越好。如果 GC = 1，那么这就是一个完美的模型了。如果 GC = 0，那么代表这只是一个随机数模型。

### `注意：`

我们需要区分开 `基尼系数` 和 `基尼不纯度` 之间的区别:

* [Gini指数、Gini系数、Gini不纯是一回事吗？](http://sofasofa.io/forum_main_post.php?postid=1001461)


### 额外参考

[Gini coefficient直观的解释与实现](https://blog.csdn.net/u010665216/article/details/78528261)



