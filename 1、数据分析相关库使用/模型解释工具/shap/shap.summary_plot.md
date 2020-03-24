# .summary_plot


使用 SHAP 对特征进行总体分析


## 案例

*   __首先建立一個模型__

        params = {'num_leaves': 30,
                'min_data_in_leaf': 20,
                'objective': 'regression',
                'max_depth': 6,
                'learning_rate': 0.01,
                "boosting": "gbdt",
                "feature_fraction": 0.9,
                "bagging_freq": 1,
                "bagging_fraction": 0.9,
                "bagging_seed": 11,
                "metric": 'rmse',
                "lambda_l1": 0.2,
                "verbosity": -1}
        model1 = lgb.LGBMRegressor(**params, n_estimators = 20000, nthread = 4, n_jobs = -1)
        model1.fit(X_train, y_train, 
                eval_set=[(X_train, y_train), (X_valid, y_valid)], eval_metric='rmse',
                verbose=1000, early_stopping_rounds=200)


*   __使用.summary_plot方法对特征进行总体分析__

    explainer = shap.TreeExplainer(model1, X_train)
    shap_values = explainer.shap_values(X_train)

    shap.summary_plot(shap_values, X_train)

    *   下图中每一行代表一个特征，横坐标为SHAP值。一个点代表一个样本，__颜色越红说明特征本身数值越大，颜色越蓝说明特征本身数值越小__。

        我们可以直观地看出 _budget_year_ratio 是一个很重要的特征，而且基本上是与收入成正相关的。 budget(预算) 也会影响收入，蓝色点主要集中在SHAP小于0的区域，可见 budget(预算) 小会降低收入，如果 budget 较高，也会增加收入，因为age这一行最右边端的点基本上都是红色的。


    *   __展示图__

        
        <div ><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/Data_Analysis/master/static/%E6%A8%A1%E5%9E%8B%E8%A7%A3%E9%87%8A%E5%B7%A5%E5%85%B7/shap/1.png"/></div>


    *   __图解扩展：__

        我们可以直观地看出潜力potential是一个很重要的特征，而且基本上是与身价成正相关的。年龄age也会明显影响身价，蓝色点主要集中在SHAP小于0的区域，可见年纪小会降低身价估值，另一方面如果年纪很大，也会降低估值，甚至降低得更明显，因为age这一行最左端的点基本上都是红色的。

        *   __展示图__

        <div ><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/Data_Analysis/master/static/%E6%A8%A1%E5%9E%8B%E8%A7%A3%E9%87%8A%E5%B7%A5%E5%85%B7/shap/2.png"/></div>


