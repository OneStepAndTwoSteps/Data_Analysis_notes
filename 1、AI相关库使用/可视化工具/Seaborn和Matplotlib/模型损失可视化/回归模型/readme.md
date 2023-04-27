# 模型评估：


## `一、分数判定：定义 RMSE 交叉验证函数：`

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


## `二、客户丝滑判定：绘制学习曲线：`



* `4.2.1、使用交叉验证：` 我们可以通过 `交叉验证` 来评估一个模型的 `泛化能力` ，如果一个模型在训练集上表现的 `良好` ，通过 `交叉验证指标` 却得出其泛化能力很 `差` ，那么模型 `过拟合` 。如果两个方面都表现的不好，那么 `欠拟合` 。这种方法可以告诉我们模型是太 `复杂` 还是太 `简单` 了。


* `4.2.2、通过观察学习曲线：` 画出模型在训练集上的表现，同时画出以训练集规模为自变量的训练集函数。为了得到图像，需要在训练集的不同规模子集上进行多次训练

* `代码：`

        def plot_learning_curves(model,x,y):
            x_train,x_val,y_train,y_val = train_test_split(x,y,test_size = 0.2)
            train_errors,val_errors = [],[]
            for m in range(1,len(x_train)):
                model.fit(x_train[:m],y_train[:m])
                y_train_predict = model.predict(x_train[:m])
                y_val_predict = model.predict(x_val)
                train_errors.append(mean_squared_error(y_train_predict,y_train[:m]))
                val_errors.append(mean_squared_error(y_val_predict,y_val))
            plt.plot(np.sqrt(train_errors),'r-',linewidth=2,label = 'train')
            plt.plot(np.sqrt(val_errors),'b-',linewidth=3,label = 'val')    
            plt.ylabel('RMSE')
            plt.xlabel('Training set size')    
            plt.legend(loc='upper right')


        line_reg3 = LinearRegression()
        plot_learning_curves(line_reg3,X,y)


* `输出：`

    <div><img  src="./static/learning_curve.jpg"/></div>