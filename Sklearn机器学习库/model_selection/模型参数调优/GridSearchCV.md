## GridSearchCV

网格搜索，用于模型参数调优


### 案例 

#### 调优随机森林：

*   __code：__

        from sklearn.model_selection import GridSearchCV

        params_grid = [
            {'n_estimators':[3,10,30],'max_features':[2,4,6,8]},
            {'bootstrap':[False],'n_estimators':[3,4],'max_features':[2,3,4]}
        ]

        forest_reg = RandomForestRegressor()
        grid_search = GridSearchCV(forest_reg,params_grid,cv=5,scoring='neg_mean_squared_error')
        grid_search.fit(housing_prepared,housing_labels)

*   __out：__

        GridSearchCV(cv=5, error_score='raise-deprecating',
                    estimator=RandomForestRegressor(bootstrap=True, criterion='mse',
                                                    max_depth=None,
                                                    max_features='auto',
                                                    max_leaf_nodes=None,
                                                    min_impurity_decrease=0.0,
                                                    min_impurity_split=None,
                                                    min_samples_leaf=1,
                                                    min_samples_split=2,
                                                    min_weight_fraction_leaf=0.0,
                                                    n_estimators='warn', n_jobs=None,
                                                    oob_score=False, random_state=None,
                                                    verbose=0, warm_start=False),
                    iid='warn', n_jobs=None,
                    param_grid=[{'max_features': [2, 4, 6, 8],
                                'n_estimators': [3, 10, 30]},
                                {'bootstrap': [False], 'max_features': [2, 3, 4],
                                'n_estimators': [3, 4]}],
                    pre_dispatch='2*n_jobs', refit=True, return_train_score=False,
                    scoring='neg_mean_squared_error', verbose=0)


#### 获取调优数据：

*   __获取指定的参数在模型中的最优参数__

    grid_search.best_params_

    {'max_features': 6, 'n_estimators': 30}


*   __获取指定的参数在模型中的最优估计量__

    grid_search.best_estimator_

    
    RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=None,
                        max_features=6, max_leaf_nodes=None,
                        min_impurity_decrease=0.0, min_impurity_split=None,
                        min_samples_leaf=1, min_samples_split=2,
                        min_weight_fraction_leaf=0.0, n_estimators=30,
                        n_jobs=None, oob_score=False, random_state=None,
                        verbose=0, warm_start=False)

*   __获取不同参数的评估得分__

    cvres = grid_search.cv_results_
    for mean_score,params in zip(cvres['mean_test_score'],cvres['params']):
        print(np.sqrt(-mean_score),params)

    63835.04474289847 {'max_features': 2, 'n_estimators': 3}
    54774.747820043405 {'max_features': 2, 'n_estimators': 10}
    52766.031776847965 {'max_features': 2, 'n_estimators': 30}
    60530.66481796719 {'max_features': 4, 'n_estimators': 3}
    52814.51075834044 {'max_features': 4, 'n_estimators': 10}
    50463.63352036248 {'max_features': 4, 'n_estimators': 30}
    59082.40630565676 {'max_features': 6, 'n_estimators': 3}
    52100.41367024943 {'max_features': 6, 'n_estimators': 10}
    49805.80987823989 {'max_features': 6, 'n_estimators': 30}
    59170.05228368051 {'max_features': 8, 'n_estimators': 3}
    51799.22273135455 {'max_features': 8, 'n_estimators': 10}
    49947.85091208428 {'max_features': 8, 'n_estimators': 30}
    61464.761311303315 {'bootstrap': False, 'max_features': 2, 'n_estimators': 3}
    59733.722781719756 {'bootstrap': False, 'max_features': 2, 'n_estimators': 4}
    59097.191447587196 {'bootstrap': False, 'max_features': 3, 'n_estimators': 3}
    57932.14105580043 {'bootstrap': False, 'max_features': 3, 'n_estimators': 4}
    58157.2674625454 {'bootstrap': False, 'max_features': 4, 'n_estimators': 3}
    56579.88070970995 {'bootstrap': False, 'max_features': 4, 'n_estimators': 4}
