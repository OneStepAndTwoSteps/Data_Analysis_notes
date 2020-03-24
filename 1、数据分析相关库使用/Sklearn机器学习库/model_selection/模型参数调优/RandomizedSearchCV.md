### RandomizedSearchCV 

__模型调优 - 随机搜索__
    
但是当超参数的搜索空间很大时，最好使用 __RandomizedSearchCV__ 。
    
这个类的使用方法和类 GridSearchCV 很相似，但它不是尝试所有可能的组合，而是通过选择每个超参数的一个随机值的特定数量的随机组合。

*   这个方法有两个优点：

    * 如果你让随机搜索运行，比如 1000 次，它会探索每个超参数的 1000 个不同的值（而不是像网格搜索那样，只搜索每个超参数的几个值）。

    * 你可以方便地通过设定搜索次数，控制超参数搜索的计算量。

与GridSearchCV相比，并非所有参数值都经过试验，而是 __从指定的分布中采样了固定数量的参数设置__。尝试的参数设置数目由 __n_iter__ 给出。

*   __考察其源代码，其搜索策略如下：__

    *   （a）对于搜索范围是分布的超参数，根据给定的分布随机采样；

    *   （b）对于搜索范围是list的超参数，在给定的list中等概率采样；

    *   （c）对a、b两步中得到的n_iter组采样结果(__获取的参数个数由n_iter决定__)，进行遍历。

    __注意：__ 如果所有参数均以列表形式显示，则将执行不替换的采样。如果给定至少一个参数作为分布，则使用替换抽样。




#### 案例 - 与GridSearchCV用法相似

    from sklearn.model_selection import RandomizedSearchCV
    params_grid = {'n_estimators':[3,10,30],'max_features':[2,4,6,8]}

    forest_reg = RandomForestRegressor()
    rdgrid_search = RandomizedSearchCV(forest_reg,param_distributions=params_grid,cv=5,
                                        scoring='neg_mean_squared_error')
    rdgrid_search.fit(housing_prepared,housing_labels)


__注意：__ 使用 __随机搜索__ 时就不能使用列表 __指定多条dict组合__ 了。即不能在设置params_grid时使用 params_grid =[{dict1},{dict2}] 。 


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


#### 属性筛选 

通过筛选，可以过滤掉一些不重要的特征。

__每个属性在随机森林中的分数：__

    这里我们使用的是RandomizedSearchCV所以它没有.feature_importances_方法，但是我们可以通过：

    rdgrid_search.best_estimator_.feature_importances_ 方法查看

__案例：__

    feature_importances = rdgrid_search.best_estimator_.feature_importances_ 

    # 因为训练数据是经过特征组合和onehot向量化的，所以这里指定他们的特征名称，让名称和特征重要值进行组合。
    extra_attribs = ["rooms_per_hhold", "pop_per_hhold", "bedrooms_per_room"]
    cat_one_hot_attribs = list(encoder.classes_)
    attributes = attribute + extra_attribs + cat_one_hot_attribs

    sorted(zip(feature_importances,attributes), reverse=True)

__输出：__

    [(0.40140789378914327, 'median_income'),
    (0.14722384301328129, 'INLAND'),
    (0.11052461094138229, 'pop_per_hhold'),
    (0.06446225001619467, 'longitude'),
    (0.05875453187145547, 'bedrooms_per_room'),
    (0.058284227824105646, 'latitude'),
    (0.04498560495190621, 'housing_median_age'),
    (0.0429344962211386, 'rooms_per_hhold'),
    (0.016626005100248267, 'total_rooms'),
    (0.015172190771710623, 'total_bedrooms'),
    (0.015027265803833633, 'population'),
    (0.013600441727164157, 'households'),
    (0.005724775743725753, '<1H OCEAN'),
    (0.0031180068959337577, 'NEAR OCEAN'),
    (0.0019602616976249097, 'NEAR BAY'),
    (0.0001935936311514464, 'ISLAND')]

