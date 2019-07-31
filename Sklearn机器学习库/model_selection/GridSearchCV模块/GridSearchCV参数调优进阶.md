## 使用GridSearchCV进行参数调优

### 案例

__code__

    from sklearn.ensemble import BaggingClassifier
    from sklearn.model_selection import GridSearchCV,Kfold


    n_estimators = [10,30,50,70,80,150,160, 170,175,180,185];
    cv_splits = Kfold(n_splits=10, test_size=.30, random_state=15)

    parameters = {'n_estimators':n_estimators,
                
            }
    grid = GridSearchCV(BaggingClassifier(base_estimator= None, ## If None, then the base estimator is a decision tree.
                                        bootstrap_features=False),
                                        param_grid=parameters,
                                        cv=cv,
                                        n_jobs = -1)
    grid.fit(X,y) 


    print (grid.best_score_)
    print (grid.best_params_)
    print (grid.best_estimator_)

__out__

    # grid.best_score_
    0.8441947565543071

    # grid.best_params_
    {'criterion': 'entropy', 'max_depth': 5, 'n_estimators': 145}

    # grid.best_estimator_
    RandomForestClassifier(bootstrap=True, class_weight=None, criterion='entropy',
                max_depth=5, max_features='auto', max_leaf_nodes=None,
                min_impurity_decrease=0.0, min_impurity_split=None,
                min_samples_leaf=1, min_samples_split=2,
                min_weight_fraction_leaf=0.0, n_estimators=145, n_jobs=1,
                oob_score=False, random_state=None, verbose=0,
                warm_start=False)


### 设置模型参数为最优模型参数

__方法1 code__

    bagging_grid = grid.best_estimator_

    bagging_grid.score(X,y)

__out__

    0.9887387387387387


__方法2 code__

    best_model=model_selection.GridSearchCV(estimator=clf[1],param_grid=params,scoring='roc_auc',cv=cv_split)
    best_model.fit(x_train,y_train)
    
    # 得到最优参数
    best_params=best_model.best_params_

    # 设置clf[1] 这个模型的参数为 最优参数
    clf[1].set_params(**best_params)



