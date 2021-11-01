## `一、定义 RMSE 交叉验证函数：`

`代码：`
    
    ### 1、导入包
    from sklearn.model_selection import KFold, cross_val_score, train_test_split

    ### 2、设置交叉验证层数
    n_folds = 5

    ### 3、RMSE 交叉验证函数
    def rmse_cv(model,x,y):
        kf = KFold(n_folds, shuffle=True, random_state=42).get_n_splits(x.values)
        rmse= np.sqrt(-cross_val_score(model, x.values, y, scoring="neg_mean_squared_error", cv = kf))
        print(cross_val_score(model, x.values, y, scoring="neg_mean_squared_error", cv = kf))  

        return(rmse)


    ### 4、生成模型
    # make_pipeline 是流水线，下面代码在开始工作时会先将数据进行标准化再进行训练 
    lasso = make_pipeline(RobustScaler(), Lasso(alpha =0.0005, random_state=1))
    

    ### 5、把模型带入 rmse_cv 中计算 RMSE
    score = rmse_cv(lasso,train,target)
    print("\nLasso score: {:.4f} ({:.4f})\n".format(score.mean(), score.std()))


`输出：`

    [-0.02147087 -0.02135566 -0.02447285 -0.02292236 -0.01954146]

    Lasso score: 0.1481 (0.0056)
