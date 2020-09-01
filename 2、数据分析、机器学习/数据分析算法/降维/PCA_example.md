# PCA 的使用案例

sklearn 中的模块

    from sklearn.decomposition import PCA

## `PCA 降维案例`

一般遇到特征非常多时，我们会采用 PCA 的方式来进行降维：

### `在操作前需要读取数据`

    df_trans = pd.read_csv('../input/train_transaction.csv')
    df_test_trans = pd.read_csv('../input/test_transaction.csv')

### `降维操作可以分为这几步：`

* `1、`因为我们要训练模型，那么对于 train 数据和 test 数据的某些特征都要进行降维，所以我们可以对数据进行合并：


        df_test['isFraud'] = 'test'                                 # 在测试数据中没有 目标值，此处先生成一个假的目标值代替
        df = pd.concat([df_train, df_test], axis=0, sort=False )    # 对 train 和 test 数据进行合并，axis = 0，列合并，也就是向下合并
        df = df.reset_index()
        df = df.drop('index', axis=1)

* `2、`导入相应模块，并且制定一个进行 PCA 降维的函数：

        from sklearn.decomposition import PCA
        from sklearn.preprocessing import minmax_scale

        def PCA_change(df, cols, n_components, prefix='PCA_', rand_seed=4):

            # 进行 PCA ，保留的主成分个数为 n_components，随机种子为 rand_seed
            pca = PCA(n_components=n_components, random_state=rand_seed)
            
            # 进行训练 
            principalComponents = pca.fit_transform(df[cols])
            
            # 生成一个 PCA 后的 principalDf df数据
            principalDf = pd.DataFrame(principalComponents)

            # 删除 df 数据中的原先列
            df.drop(cols, axis=1, inplace=True)

            # 对 PCA 降维后的主成分列进行新的命名
            principalDf.rename(columns=lambda x: str(prefix)+str(x), inplace=True)

            # 拼接数据 按照行进行拼接，也就是向右延伸
            df = pd.concat([df, principalDf], axis=1)
            
            return df

* `3、`调用函数：

        for col in mas_v:
            df[col] = df[col].fillna((df[col].min() - 2))          # 如果数据中存在空值，那么进行填充
            df[col] = (minmax_scale(df[col], feature_range=(0,1))) # 对数据进行归一化操作，最大值为 1 ，最小值为0

        # 调用 PCA 函数，生成的 df 数据就是指定列进行降维后的新数据
        df = PCA_change(df, mas_v, prefix='PCA_V_', n_components=30)



