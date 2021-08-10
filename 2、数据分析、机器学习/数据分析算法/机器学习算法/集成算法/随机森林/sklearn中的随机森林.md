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


### 查看随着特征数量增多，重要性的变化曲线

`案例：`

    def plot_feature_importances(df, threshold = 0.9):
        """
        Plots 15 most important features and the cumulative importance of features.
        Prints the number of features needed to reach threshold cumulative importance.
        
        Parameters
        --------
        df : dataframe
            Dataframe of feature importances. Columns must be feature and importance
        threshold : float, default = 0.9
            Threshold for prining information about cumulative importances
            
        Return
        --------
        df : dataframe
            Dataframe ordered by feature importances with a normalized column (sums to 1)
            and a cumulative importance column
        
        """
        
        plt.rcParams['font.size'] = 18
        
        # Sort features according to importance
        df = df.sort_values('importance', ascending = False).reset_index()
        
        # Normalize the feature importances to add up to one
        df['importance_normalized'] = df['importance'] / df['importance'].sum()
        df['cumulative_importance'] = np.cumsum(df['importance_normalized'])

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
        
        # Cumulative importance plot
        plt.figure(figsize = (8, 6))
        plt.plot(list(range(len(df))), df['cumulative_importance'], 'r-')
        plt.xlabel('Number of Features'); plt.ylabel('Cumulative Importance'); 
        plt.title('Cumulative Feature Importance');
        plt.show();
        
        importance_index = np.min(np.where(df['cumulative_importance'] > threshold))
        print('%d features required for %0.2f of cumulative importance' % (importance_index + 1, threshold))
        
        return df

`调用: `

    norm_feature_importances = plot_feature_importances(feature_importances)

<div align=center><img width="550" height="550" src="./static/9.jpg"/></div>

