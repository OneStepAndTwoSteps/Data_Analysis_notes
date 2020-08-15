# 随机森林模型的基本参数和特征重要性可视化：


`模块：`

    from sklearn.ensemble import RandomForestClassifier

`参数：`

* `n_estimators: `  随机森林里决策树的个数 默认为10

* `criterion:  `    决策树分裂标准，默认是基尼系数(CART算法)，也可以选择entropy(ID3算法)

* `max_depath: `    决策树的最大深度，默认是None，也就是不限制决策树的深度，也可以设置一个整数限制决策树的最大深度。

* `n_jobs:    `     拟合和预测的时候CPU的核数，默认是1，也可以是整数，-1表示CPU有多少个核心，就启动多少job

`其他更多：`

* https://www.w3cschool.cn/doc_scikit_learn/scikit_learn-modules-generated-sklearn-ensemble-randomforestclassifier.html?lang=en#sklearn.ensemble.RandomForestClassifier




## `使用 随机森林 训练数据`

`案例：`

    from sklearn.ensemble import RandomForestClassifier

    # Make the random forest classifier
    random_forest = RandomForestClassifier(n_estimators = 100, random_state = 50, verbose = 1, n_jobs = -1)

    # Train on the training data
    random_forest.fit(train, train_labels)

    # Extract feature importances
    feature_importance_values = random_forest.feature_importances_
    feature_importances = pd.DataFrame({'feature': features, 'importance': feature_importance_values})

    # Make predictions on the test data
    predictions = random_forest.predict_proba(test)[:, 1]

`保存文件：`


    # Make a submission dataframe
    submit = app_test[['SK_ID_CURR']]
    submit['TARGET'] = predictions

    # Save the submission dataframe
    submit.to_csv('random_forest_baseline.csv', index = False)



## `查看特征重要性`

* 调用前先生成 `feature_importances` ,具体查看上面 `使用 随机森林 训练数据`


`模板：`

    def plot_feature_importances(df):
        """
        Plot importances returned by a model. This can work with any measure of
        feature importance provided that higher importance is better. 
        
        Args:
            df (dataframe): feature importances. Must have the features in a column
            called `features` and the importances in a column called `importance
            
        Returns:
            shows a plot of the 15 most importance features
            
            df (dataframe): feature importances sorted by importance (highest to lowest) 
            with a column for normalized importance
            """
        
        # Sort features according to importance
        df = df.sort_values('importance', ascending = False).reset_index()
        
        # Normalize the feature importances to add up to one
        df['importance_normalized'] = df['importance'] / df['importance'].sum()

        # Make a horizontal bar chart of feature importances
        plt.figure(figsize = (10, 6))
        ax = plt.subplot()
        
        # Need to reverse the index to plot most important on top
        ax.barh(list(reversed(list(df.index[:15]))), 
                df['importance_normalized'].head(15), 
                align = 'center', edgecolor = 'k')
        
        # Set the yticks and labels
        ax.set_yticks(list(reversed(list(df.index[:15]))))
        ax.set_yticklabels(df['feature'].head(15))
        
        # Plot labeling
        plt.xlabel('Normalized Importance'); plt.title('Feature Importances')
        plt.show()
        
        return df

`调用：`

    # Show the feature importances for the default features
    feature_importances_sorted = plot_feature_importances(feature_importances)

`效果图：`

<div align=center><img width="550" height="350" src="./static/8.jpg"/></div>







