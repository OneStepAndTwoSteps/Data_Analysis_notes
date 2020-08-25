# XGBClassifier

    import xgboost as xgb
    import lightgbm as lgb

## `XGB 参考文章`

* [Python机器学习笔记：XgBoost算法](https://www.cnblogs.com/wj-1314/p/9402324.html)

## `gini系数`

* [Gini Coefficient - An Intuitive Explanation](https://www.kaggle.com/batzner/gini-coefficient-an-intuitive-explanation)

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


### XGB + LGB 集成

案例：

`1、定义gini评估方法`

    def gini(y, pred):
        g = np.asarray(np.c_[y, pred, np.arange(len(y)) ], dtype=np.float)
        g = g[np.lexsort((g[:,2], -1*g[:,1]))]
        gs = g[:,0].cumsum().sum() / g[:,0].sum()
        gs -= (len(y) + 1) / 2.
        return gs / len(y)

    def gini_xgb(pred, y):
        y = y.get_label()
        return 'gini', gini(y, pred) / gini(y, y)

    def gini_lgb(preds, dtrain):
        y = list(dtrain.get_label())
        score = gini(y, preds) / gini(y, y)
        return 'gini', score, True

`2、使用 xgb 和 lgb 训练和预测：`

`版本一：使用 ndarrary 数据进行训练：`

    import xgboost as xgb
    import lightgbm as lgb


    # xgb
    params = {'eta': 0.02, 'max_depth': 4, 'subsample': 0.9, 'colsample_bytree': 0.9, 
            'objective': 'binary:logistic', 'eval_metric': 'auc', 'silent': True}

    X = train.drop(['id', 'target'], axis=1)
    features = X.columns
    X = X.values                                <---- nd arrary 数据
    y = train['target'].values
    sub=test['id'].to_frame()
    sub['target']=0

    nrounds=200  # need to change to 2000
    kfold = 2  # need to change to 5
    skf = StratifiedKFold(n_splits=kfold, random_state=0)
    for i, (train_index, test_index) in enumerate(skf.split(X, y)):
        print(' xgb kfold: {}  of  {} : '.format(i+1, kfold))
        X_train, X_valid = X[train_index], X[test_index]
        y_train, y_valid = y[train_index], y[test_index]
        d_train = xgb.DMatrix(X_train, y_train) 
        d_valid = xgb.DMatrix(X_valid, y_valid) 
        watchlist = [(d_train, 'train'), (d_valid, 'valid')]
        xgb_model = xgb.train(params, d_train, nrounds, watchlist, early_stopping_rounds=100, 
                            feval=gini_xgb, maximize=True, verbose_eval=100)

        # 结尾 除以 (2*kfold)，是因为要将 xgb 和 lgb 去平均然后将结果相加合并
        sub['target'] += xgb_model.predict(xgb.DMatrix(test[features].values), 
                            ntree_limit=xgb_model.best_ntree_limit+50) / (2*kfold)
    gc.collect()
    sub.head(2)

    # lgb
    params = {'metric': 'auc', 'learning_rate' : 0.01, 'max_depth':10, 'max_bin':10,  'objective': 'binary', 
            'feature_fraction': 0.8,'bagging_fraction':0.9,'bagging_freq':10,  'min_data': 500}

    skf = StratifiedKFold(n_splits=kfold, random_state=1)
    for i, (train_index, test_index) in enumerate(skf.split(X, y)):
        print(' lgb kfold: {}  of  {} : '.format(i+1, kfold))
        X_train, X_eval = X[train_index], X[test_index]
        y_train, y_eval = y[train_index], y[test_index]
        lgb_model = lgb.train(params, lgb.Dataset(X_train, label=y_train), nrounds, 
                    lgb.Dataset(X_eval, label=y_eval), verbose_eval=100, 
                    feval=gini_lgb, early_stopping_rounds=100)

        # 结尾 除以 (2*kfold)，是因为要将 xgb 和 lgb 去平均然后将结果相加合并
        sub['target'] += lgb_model.predict(test[features].values, 
                            num_iteration=lgb_model.best_iteration) / (2*kfold)
        
    sub.to_csv('sub10.csv', index=False, float_format='%.5f') 
    gc.collect()
    sub.head(2)

`版本2：使用 dataframe 数据进行训练：`

    # xgb
    params = {'eta': 0.02, 'max_depth': 4, 'subsample': 0.9, 'colsample_bytree': 0.9, 
            'objective': 'binary:logistic', 'eval_metric': 'auc', 'silent': True}

    X = train.drop(['id', 'target'], axis=1)
    features = X.columns
    y = train['target']
    sub=test['id'].to_frame()
    sub['target']=0

    nrounds=200  # need to change to 2000
    kfold = 2  # need to change to 5
    skf = StratifiedKFold(n_splits=kfold, random_state=0)
    for i, (train_index, test_index) in enumerate(skf.split(X, y)):
        print(' xgb kfold: {}  of  {} : '.format(i+1, kfold))
        X_train, X_valid = X.loc[train_index], X.loc[test_index]
        y_train, y_valid = y.loc[train_index], y.loc[test_index]
        d_train = xgb.DMatrix(X_train, y_train) 
        d_valid = xgb.DMatrix(X_valid, y_valid) 
        watchlist = [(d_train, 'train'), (d_valid, 'valid')]
        xgb_model = xgb.train(params, d_train, nrounds, watchlist, early_stopping_rounds=100, 
                            feval=gini_xgb, maximize=True, verbose_eval=100)

        # 结尾 除以 (2*kfold)，是因为要将 xgb 和 lgb 去平均然后将结果相加合并
        sub['target'] += xgb_model.predict(xgb.DMatrix(test[features]), 
                            ntree_limit=xgb_model.best_ntree_limit+50) / (2*kfold)
    gc.collect()
    sub.head(2)

    # lgb
    params = {'metric': 'auc', 'learning_rate' : 0.01, 'max_depth':10, 'max_bin':10,  'objective': 'binary', 
            'feature_fraction': 0.8,'bagging_fraction':0.9,'bagging_freq':10,  'min_data': 500}

    skf = StratifiedKFold(n_splits=kfold, random_state=1)
    for i, (train_index, test_index) in enumerate(skf.split(X, y)):
        print(' lgb kfold: {}  of  {} : '.format(i+1, kfold))
        X_train, X_eval = X.loc[train_index], X.loc[test_index]
        y_train, y_eval = y.loc[train_index], y.loc[test_index]
        lgb_model = lgb.train(params, lgb.Dataset(X_train, label=y_train), nrounds, 
                    lgb.Dataset(X_eval, label=y_eval), verbose_eval=100, 
                    feval=gini_lgb, early_stopping_rounds=100)

        # 结尾 除以 (2*kfold)，是因为要将 xgb 和 lgb 去平均然后将结果相加合并
        sub['target'] += lgb_model.predict(test[features], 
                            num_iteration=lgb_model.best_iteration) / (2*kfold)
        
    sub.to_csv('sub10.csv', index=False, float_format='%.5f') 
    gc.collect()
    sub.head(2)


`3、运行结果：`

    xgb kfold: 1  of  2 : 
    [0]	train-auc:0.601121	valid-auc:0.598673	train-gini:0.201639	valid-gini:0.19759
    Multiple eval metrics have been passed: 'valid-gini' will be used for early stopping.

    Will train until valid-gini hasn't improved in 100 rounds.
    [100]	train-auc:0.62676	valid-auc:0.619545	train-gini:0.253519	valid-gini:0.239091
    [199]	train-auc:0.641313	valid-auc:0.629075	train-gini:0.282627	valid-gini:0.25815
    xgb kfold: 2  of  2 : 
    [0]	train-auc:0.602562	valid-auc:0.593907	train-gini:0.205442	valid-gini:0.187655
    Multiple eval metrics have been passed: 'valid-gini' will be used for early stopping.

    Will train until valid-gini hasn't improved in 100 rounds.
    [100]	train-auc:0.628673	valid-auc:0.618482	train-gini:0.257344	valid-gini:0.236967
    [199]	train-auc:0.643521	valid-auc:0.627597	train-gini:0.287043	valid-gini:0.255193
    lgb kfold: 1  of  2 : 
    Training until validation scores don't improve for 100 rounds.
    [100]	valid_0's auc: 0.625366	valid_0's gini: 0.250732
    [200]	valid_0's auc: 0.627438	valid_0's gini: 0.254876
    lgb kfold: 2  of  2 : 
    Training until validation scores don't improve for 100 rounds.
    [100]	valid_0's auc: 0.623138	valid_0's gini: 0.246276
    [200]	valid_0's auc: 0.625488	valid_0's gini: 0.250977

        id	target
    0	0	0.060758
    1	1	0.065624


## 绘制 xgb 的 feature importance

`1、绘制点状图：` 

    def model_feature_importances(model):
        trace = go.Scatter(
            y = np.array(list(model.get_fscore().values())), # xgb 模型使用 .get_fscore() 方法获取特征重要性
            x = np.array(list(model.get_fscore().keys())),
            mode='markers',
            marker=dict(
                sizemode = 'diameter',
                sizeref = 1,
                size = 13,
                #size= model.feature_importances_,
                #color = np.random.randn(500), #set color equal to a variable
                color =  np.array(list(model.get_fscore().values())),
                colorscale='Portland',
                showscale=True
            ),
            text = np.array(list(model.get_fscore().keys()))
        )
        data = [trace]

        layout= go.Layout(
            autosize= True,
            title= 'xgb Feature Importance',
            hovermode= 'closest',
            xaxis= dict(
                ticklen= 5,
                showgrid=False,
                zeroline=False,
                showline=False
            ),
            yaxis=dict(
                title= 'Feature Importance',
                showgrid=False,
                zeroline=False,
                ticklen= 5,
                gridwidth= 2
            ),
            showlegend= False
        )
        fig = go.Figure(data=data, layout=layout)
        fig.show()

    # 调用方法
    model_feature_importances(xgb_model2)



`展示图：`



<div align=center><img width="800" height="300" src="./static/feature_importance2.jpg"/></div>



`2、绘制柱状图：`

    xgb_importance = np.array(list(xgb_model2.get_fscore().values()))
    xgb_features = np.array(list(xgb_model2.get_fscore().keys()))

    x, y = (list(x) for x in zip(*sorted(zip(xgb_importance,xgb_features), reverse = False)))
    trace2 = go.Bar(
        x=x ,
        y=y,
        marker=dict(
            color=x,
            colorscale = 'Viridis',
            reversescale = True
        ),
        name='Random Forest Feature importance',
        orientation='h',
    )

    layout = dict(
        title='Barplot of Feature importances',
        width = 900, height = 2000,
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=True,
    #         domain=[0, 0.85],
        ))

    fig1 = go.Figure(data=[trace2])
    fig1['layout'].update(layout)
    py.iplot(fig1, filename='plots')


`展示图：`



<div align=center><img width="800" height="300" src="./static/feature_importance.jpg"/></div>


### 额外参考

[Gini coefficient直观的解释与实现](https://blog.csdn.net/u010665216/article/details/78528261)



