## sklearn 计算 RMSE 和 RMSLE



    from sklearn.metrics import mean_squared_error //均方误差
    from sklearn.metrics import mean_squared_log_error //均方对数误差
    from sklearn.metrics import mean_absolute_error //平方绝对误差

    x = [1,2,3,4,5]
    y = [2,4,3,2,6]

    MSE = mean_squared_error(x, y)
    # 开庚号
    RMSE = MSE ** 0.5
    MAE = mean_absolute_error(x, y)
    MSLE = mean_squared_log_error(x, y)
    # 开庚号
    RMSLE = MSLE ** 0.5
    print(MSE, RMSE, MAE, RMSLE)




