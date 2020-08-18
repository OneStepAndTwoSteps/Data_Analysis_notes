# 特征预处理

机器学习的模式之一：`特征工程` 比模型构建和超参数调整有更大的投资回报。正如 `Andrew Ng` 喜欢说的：“应用机器学习基本上是特征工程。”

虽然选择正确的模型和最佳设置很重要，但是模型只能从给定的数据中学习。确保这些数据尽可能与任务相关是数据科学家的工作（也许还有一些自动化工具可以帮助我们）。

`特征工程` 指的是一个遗传过程，可以包括特征构造：从现有数据中添加新的特征，以及特征选择：只选择最重要的特征或其他降维方法。我们可以使用许多技术来创建特性和选择特性。

当我们开始使用其他数据源时，我们将进行大量的特征工程，比如我们可以尝试以下两种简单的特征构造方法：

* `Polynomial Features 多项式特征`

* `Domain knowledge features 领域知识特征`


## `一、Polynomial Features：`

一种简单的特征构造方法称为 `多项式特征`。在该方法中，我们生成的特征是现有特征的幂函数以及现有特征之间的交互项。

例如，我们可以创建变量 `EXT_SOURCE_1的二次方` 和 `EXT_SOURCE_2的二次方`，也可以创建变量 `EXT_SOURCE_1 x EXT_SOURCE_2^2`，`EXT_SOURCE_1^2 x EXT_SOURCE_2^2`，依此类推。这些由多个独立变量组合而成的特征称为 [交互项](https://en.wikipedia.org/wiki/Interaction（统计学）) 因为它们捕捉变量之间的相互作用。换言之，虽然两个变量本身可能不会对目标产生强烈的影响，但将它们组合成一个单独的交互变量可能会显示出与目标的关系。交互项在统计模型中常用来捕捉多个变量的影响，但我不认为它们在机器学习中经常使用。尽管如此，我们可以尝试一些，看看它们是否有助于我们的模型来预测是否会有帮助。


在下面的代码中，我们使用 `EXT_SOURCE` 和 `DAYS_BIRTH` 变量创建多项式特征。`Scikit Learn` 有一个很有用的类，叫做 `PolynomialFeatures` ，它创建多项式和交互项，达到指定的程度。我们可以使用3度来查看结果（当我们创建多项式特征时，我们希望避免使用太高的次数，这既因为 `特征的数量与次数成指数关系` ，也因为我们可能会遇到 `过拟合` 的问题）。

`案例：`

    # 为多项式特征生成一个新的数据帧，筛选出 app_train 的一些特征，然后生成一个新的数据帧
    poly_features = app_train[['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3', 'DAYS_BIRTH', 'TARGET']]
    poly_features_test = app_test[['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3', 'DAYS_BIRTH']]

    # 用于处理缺失值的填充器
    from sklearn.preprocessing import Imputer
    imputer = Imputer(strategy = 'median')

    poly_target = poly_features['TARGET']

    poly_features = poly_features.drop(columns = ['TARGET'])

    #需要插补缺失值
    poly_features = imputer.fit_transform(poly_features)
    poly_features_test = imputer.transform(poly_features_test)

    from sklearn.preprocessing import PolynomialFeatures
                                    
    # 创建具有指定次数的多项式对象
    poly_transformer = PolynomialFeatures(degree = 3)


    # 多项式特征的训练
    poly_transformer.fit(poly_features)

    # 转换特征
    poly_features = poly_transformer.transform(poly_features)
    poly_features_test = poly_transformer.transform(poly_features_test)
    print('Polynomial Features shape: ', poly_features.shape)

`输出：`

    Polynomial Features shape:  (307511, 35)



### `查看构造出的新特征：`

* `get_feature_names` 可以用于获取 `PolynomialFeatures` 中的相关特征


`案例：`

    poly_transformer.get_feature_names(input_features = ['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3', 'DAYS_BIRTH'])[:15]

`输出: `

    ['1',
    'EXT_SOURCE_1',
    'EXT_SOURCE_2',
    'EXT_SOURCE_3',
    'DAYS_BIRTH',
    'EXT_SOURCE_1^2',
    'EXT_SOURCE_1 EXT_SOURCE_2',
    'EXT_SOURCE_1 EXT_SOURCE_3',
    'EXT_SOURCE_1 DAYS_BIRTH',
    'EXT_SOURCE_2^2',
    'EXT_SOURCE_2 EXT_SOURCE_3',
    'EXT_SOURCE_2 DAYS_BIRTH',
    'EXT_SOURCE_3^2',
    'EXT_SOURCE_3 DAYS_BIRTH',
    'DAYS_BIRTH^2']



* 共有35个特征，每个特征都被提升到3级幂和交互项。现在，我们可以看到这些新特性是否与目标相关。


### `查看构造出的新特征之间的关联性：`

`案例：`

    # Create a dataframe of the features 
    poly_features = pd.DataFrame(poly_features, 
                                columns = poly_transformer.get_feature_names(['EXT_SOURCE_1', 'EXT_SOURCE_2', 
                                                                            'EXT_SOURCE_3', 'DAYS_BIRTH']))

    # Add in the target
    poly_features['TARGET'] = poly_target

    # Find the correlations with the target
    poly_corrs = poly_features.corr()['TARGET'].sort_values()

    # Display most negative and most positive
    print(poly_corrs.head(10))
    print(poly_corrs.tail(5))


`输出：`

    EXT_SOURCE_2 EXT_SOURCE_3                -0.193939
    EXT_SOURCE_1 EXT_SOURCE_2 EXT_SOURCE_3   -0.189605
    EXT_SOURCE_2 EXT_SOURCE_3 DAYS_BIRTH     -0.181283
    EXT_SOURCE_2^2 EXT_SOURCE_3              -0.176428
    EXT_SOURCE_2 EXT_SOURCE_3^2              -0.172282
    EXT_SOURCE_1 EXT_SOURCE_2                -0.166625
    EXT_SOURCE_1 EXT_SOURCE_3                -0.164065
    EXT_SOURCE_2                             -0.160295
    EXT_SOURCE_2 DAYS_BIRTH                  -0.156873
    EXT_SOURCE_1 EXT_SOURCE_2^2              -0.156867
    Name: TARGET, dtype: float64
    DAYS_BIRTH     -0.078239
    DAYS_BIRTH^2   -0.076672
    DAYS_BIRTH^3   -0.074273
    TARGET          1.000000
    1                    NaN
    Name: TARGET, dtype: float64


* 一些新的变量与目标的相关性比原始特征更大（就绝对大小而言）。当我们构建机器学习模型时，我们可以尝试使用或不使用这些特性来确定它们是否真的有助于模型学习。


* 我们将把这些特性添加到训练和测试数据的副本中，然后评估有无这些特性的模型。很多时候在机器学习中，要知道一种方法是否有效，唯一的方法就是尝试一下！

### `将构造好的新特征加入到数据中：`

`案例：`

    # 将测试特征放入数据帧
    poly_features_test = pd.DataFrame(poly_features_test, 
                                    columns = poly_transformer.get_feature_names(['EXT_SOURCE_1', 'EXT_SOURCE_2', 
                                                                                    'EXT_SOURCE_3', 'DAYS_BIRTH']))

    # 将多项式特征合并到训练数据帧中，SK_ID_CURR 是数据的标识符，这里先将原始的 SK_ID_CURR 加入到新特征中。
    poly_features['SK_ID_CURR'] = app_train['SK_ID_CURR']
    app_train_poly = app_train.merge(poly_features, on = 'SK_ID_CURR', how = 'left') # 合并数据

    # 将多项式特征合并到测试数据帧中
    poly_features_test['SK_ID_CURR'] = app_test['SK_ID_CURR']
    app_test_poly = app_test.merge(poly_features_test, on = 'SK_ID_CURR', how = 'left')

    # 对齐数据帧
    app_train_poly, app_test_poly = app_train_poly.align(app_test_poly, join = 'inner', axis = 1)

    # Print out the new shapes
    print('Training data with polynomial features shape: ', app_train_poly.shape)
    print('Testing data with polynomial features shape:  ', app_test_poly.shape)

`输出：`

    Training data with polynomial features shape:  (307511, 278)
    Testing data with polynomial features shape:   (48744, 278)


## `二、领域知识特征：`


也许称之为 `领域知识` 是不完全正确的，拿信用卡违约分析来说：因为我不是一个信用专家，但也许我们可以称之为 `尝试应用有限的金融知识`。在这种思路下，我们可以制作一些功能，试图捕捉我们认为对判断客户是否会拖欠贷款很重要的信息。在这里，我将使用五个功能，这些功能都是由Aguiar的脚本启发的：



* `信贷收入百分比：`信贷金额相对于客户收入的百分比

* `年金收入百分比：`贷款年金相对于客户收入的百分比

* `信用期限：`按月支付的期限（因为年金是每月到期的金额

* `雇佣天数百分比：`雇佣天数相对于客户年龄的百分比


`案例：`

    app_train_domain = app_train.copy()
    app_test_domain = app_test.copy()

    app_train_domain['CREDIT_INCOME_PERCENT'] = app_train_domain['AMT_CREDIT'] / app_train_domain['AMT_INCOME_TOTAL']
    app_train_domain['ANNUITY_INCOME_PERCENT'] = app_train_domain['AMT_ANNUITY'] / app_train_domain['AMT_INCOME_TOTAL']
    app_train_domain['CREDIT_TERM'] = app_train_domain['AMT_ANNUITY'] / app_train_domain['AMT_CREDIT']
    app_train_domain['DAYS_EMPLOYED_PERCENT'] = app_train_domain['DAYS_EMPLOYED'] / app_train_domain['DAYS_BIRTH']

    app_test_domain['CREDIT_INCOME_PERCENT'] = app_test_domain['AMT_CREDIT'] / app_test_domain['AMT_INCOME_TOTAL']
    app_test_domain['ANNUITY_INCOME_PERCENT'] = app_test_domain['AMT_ANNUITY'] / app_test_domain['AMT_INCOME_TOTAL']
    app_test_domain['CREDIT_TERM'] = app_test_domain['AMT_ANNUITY'] / app_test_domain['AMT_CREDIT']
    app_test_domain['DAYS_EMPLOYED_PERCENT'] = app_test_domain['DAYS_EMPLOYED'] / app_test_domain['DAYS_BIRTH']


### `可视化新变量：`

我们应该在一个图形中可视化地探索这些领域知识变量。对于所有这些，我们将用目标值着色相同的KDE图。

案例：

    plt.figure(figsize = (12, 20))
    # iterate through the new features
    for i, feature in enumerate(['CREDIT_INCOME_PERCENT', 'ANNUITY_INCOME_PERCENT', 'CREDIT_TERM', 'DAYS_EMPLOYED_PERCENT']):
        
        # create a new subplot for each source
        plt.subplot(4, 1, i + 1)
        # plot repaid loans
        sns.kdeplot(app_train_domain.loc[app_train_domain['TARGET'] == 0, feature], label = 'target == 0')
        # plot loans that were not repaid
        sns.kdeplot(app_train_domain.loc[app_train_domain['TARGET'] == 1, feature], label = 'target == 1')
        
        # Label the plots
        plt.title('Distribution of %s by Target Value' % feature)
        plt.xlabel('%s' % feature); plt.ylabel('Density');
        
    plt.tight_layout(h_pad = 2.5)


<div align=center><img width="600" height="990" src="./static/Visualize New Variables.jpg"/></div>

## `三、其他：`

### `3.1、Function for Numeric Aggregations (数值聚合函数)：`

当想要获取某一 dataframe 中的数字信息，我们可以计算所有数字列的统计信息。 为此，我们可以针对数据的 `ID` 进行分组，对分组的数据框进行 `agg` 转换，然后将结果合并回训练数据中。 `agg` 函数将仅计算认为该操作有效的数字列的值。 我们将坚持使用 `mean`，`max`，`min`，`sum`，但是任何函数都可以在此处传递。 我们甚至可以编写我们自己的函数，并在`agg`调用中使用它。

`模板：`

    def agg_numeric(df, group_var, df_name):
        """Aggregates the numeric values in a dataframe. This can
        be used to create features for each instance of the grouping variable.
        
        Parameters
        --------
            df (dataframe): 
                要进行统计的df数据
            group_var (string): 
                分组 df 的变量，也就是按照哪一列进行 groupby 分组统计
            df_name (string): 
                用于重命名列的变量，在新生成的 统计变量前加上 df_name
            
        Return
        --------
            agg (dataframe): 
                a dataframe with the statistics aggregated for 
                all numeric columns. Each instance of the grouping variable will have 
                the statistics (mean, min, max, sum; currently supported) calculated. 
                The columns are also renamed to keep track of features created.
        
        """
        # 删除除分组变量以外的 id 变量,看情况决定是否定义
        for col in df:
            # if col != group_var and 'SK_ID' in col: # 列名中不包含 group_var 并且包含 SK_ID 的列进行删除            
                df = df.drop(columns = col)
                
        group_ids = df[group_var]                   # 将数据的唯一标识 id 列数据赋值于 group_ids
        numeric_df = df.select_dtypes('number')     # 找出数据中类型为数字的列，赋值给新的 df
        numeric_df[group_var] = group_ids           # 将唯一标识 id 赋予给新的 df

        # 按指定变量分组并计算统计信息，计算的到的新 agg 是一个有阶层的 groupby 对象，需要经过下面步骤进行过滤
        agg = numeric_df.groupby(group_var).agg(['count', 'mean', 'max', 'min', 'sum']).reset_index() # 进行 agg 操作

        # Need to create new column names
        columns = [group_var]

        # 遍历变量名称，整理上面生成的 agg 对象
        for var in agg.columns.levels[0]:
            # Skip the grouping variable
            if var != group_var:
                # Iterate through the stat names
                for stat in agg.columns.levels[1][:-1]:
                    # Make a new column name for the variable and stat
                    columns.append('%s_%s_%s' % (df_name, var, stat))

        agg.columns = columns
        return agg

`调用：`
    
    bureau_agg_new = agg_numeric(bureau.drop(columns = ['SK_ID_BUREAU']), group_var = 'SK_ID_CURR', df_name = 'bureau')
    bureau_agg_new.head()


`展示图：`



<div align=center><img width="800" height="120" src="./static/Function for Numeric Aggregations.jpg"/></div>


##  `删除共线特征：`

对于 `共线变量`，我们不仅可以计算变量与目标值的相关性，还可以计算每个变量与其他每个变量的相关性。 这将使我们看到是否存在应该从数据中删除的高度共线变量。

`案例：`

* `1、`寻找与其他变量的相关性大于0.8的任何变量：


        # 设置阈值
        threshold = 0.8

        # 创建一个空字典以容纳相关变量
        above_threshold_vars = {}

        # 对于每一列，记录高于阈值的变量
        for col in corrs:
            above_threshold_vars[col] = list(corrs.index[corrs[col] > threshold])

* `2、`对于每对高度相关的变量，我们只想删除其中一个变量。 以下代码创建了一组变量，只需将每个变量对中的一个相加即可删除。


        # 跟踪要删除的列和已检查的列
        cols_to_remove = []
        cols_seen = []
        cols_to_remove_pair = []

        # 遍历列和相关列
        for key, value in above_threshold_vars.items():
            # 跟踪已检查的列
            cols_seen.append(key)
            for x in value:
                if x == key:
                    next
                else:
                    # 如果存在高相关的特征，只保留一个
                    if x not in cols_seen:                  # 如果该特征在之前的 key 数据中没有出现过。
                        cols_to_remove.append(x)            # 存在高度相关，将高度相关的特征放入 cols_to_remove 中。
                        cols_to_remove_pair.append(key)     # cols_to_remove 和 cols_to_remove_pair 得到的结果一致。
                    
        cols_to_remove = list(set(cols_to_remove))
        print('Number of columns to remove: ', len(cols_to_remove))

* `3、`删除高度相关特征


        train_corrs_removed = train.drop(columns = cols_to_remove)
        test_corrs_removed = test.drop(columns = cols_to_remove)

        print('Training Corrs Removed Shape: ', train_corrs_removed.shape)
        print('Testing Corrs Removed Shape: ', test_corrs_removed.shape)




