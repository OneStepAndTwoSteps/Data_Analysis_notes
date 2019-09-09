# impute

impute 可以帮助我们对缺失值进行填充

__import__

    # skleran 0.21之前：
    from sklearn.preprocessing.Imputer

    # sklearn 0.21之后
    from sklearn.impute import SimpleImputer 


__example__

*   __生成数据：__

        import numpy as np
        import pandas as pd
        from sklearn.impute import SimpleImputer

        # 生成缺失数据
        df = pd.DataFrame(np.random.randn(6, 4),
                        columns=['col1', 'col2', 'col3', 'col4'])  # 生成一份数据
        df.iloc[1:2, 1] = np.nan  # 增加缺失值
        df.iloc[4, 3] = np.nan  # 增加缺失值
        print(df)

    __out:__

                col1      col2      col3      col4
            0 -1.691392  1.194569  0.391176  0.155575
            1  0.514021       NaN -1.436018  0.906631
            2 -0.268912 -1.007554 -0.432727 -0.188102
            3  0.843487  0.944824  0.700360 -0.140919
            4 -0.443710  0.391788 -0.450471       NaN
            5  0.775983  0.786574  0.033852 -0.009252

*   __处理缺失值：__

        # 使用sklearn将缺失值替换为特定值 version 0.21.3之后没有axis参数(因为我们通常使用列数据进行计算 因为他是特征列)
        # 建立替换规则：将值为NaN的缺失值以均值做替换
        nan_model = SimpleImputer(missing_values=np.nan, strategy='mean')  
        
        # 应用模型规则  
        nan_result = nan_model.fit_transform(df)  
        print(nan_result)  # 打印输出


    __out:__

        array([[-1.69139151,  1.19456921,  0.39117638,  0.15557532],
              [ 0.51402149,  0.46204018, -1.43601841,  0.9066309 ],
              [-0.26891249, -1.00755422, -0.4327267 , -0.18810163],
              [ 0.84348664,  0.94482415,  0.70035979, -0.14091897],
              [-0.44371015,  0.39178767, -0.45047133,  0.14478681],
              [ 0.77598319,  0.78657408,  0.03385228, -0.00925157]])


