## SimpleImputer

### 案例

现在有一份数据，其中 total_bedrooms 属性存在缺失值。

### 数据清洗

大多机器学习算法不能处理缺失的特征，因此先创建一些函数来处理特征缺失的问题。前面，你应该注意到了属性 total_bedrooms 有一些缺失值。

有三个解决选项：


*    去掉对应的街区；

*    去掉整个属性；

*    进行赋值（0、平均值、中位数等等）。

用 DataFrame 的 dropna() ， drop() ，和 fillna() 方法，可以方便地实现：

    housing.dropna(subset=["total_bedrooms"]) # 选项1

    housing.drop("total_bedrooms", axis=1) # 选项2

    median = housing["total_bedrooms"].median()
    housing["total_bedrooms"].fillna(median) # 选项3

如果 __选择选项 3__，你需要计算训练集的中位数，用中位数填充训练集的缺失值，__不要忘记保存该中位数__ 。后面用测试集评估系统时，需要替换测试集中的缺失值，__也可以用来实时替换新数据中的缺失值。__


Scikit-Learn 提供了一个方便的类来处理缺失值： Imputer 。下面是其使用方法：

*   __首先，需要创建一个 Imputer 实例，指定用某属性的中位数来替换该属性所有的缺失值：__


        from sklearn import impute
        imputer = impute.SimpleImputer(strategy='median')
        # 原数据中存在非数值的列，这里先将其删除，然后记录每一个属性的中位数
        housing_new = housing.copy(deep=True).drop('ocean_proximity',axis=1)

        imputer.fit(housing_new)

*   __imputer 计算出了每个属性的中位数，并将结果保存在了实例变量 statistics_中。__

    虽然此时只有属性 total_bedrooms 存在缺失值，__但我们不能确定在以后的新的数据中会不会有其他属性也存在缺失值，所以安全的做法是将 imputer 应用到每个数值：__

        display(imputer.statistics_)

        housing_new.median().values

        array([-1.1849e+02,  3.4260e+01,  2.9000e+01,  2.1270e+03,  4.3500e+02,
        1.1660e+03,  4.0900e+02,  3.5348e+00,  1.7970e+05])

        array([-1.1849e+02,  3.4260e+01,  2.9000e+01,  2.1270e+03,  4.3500e+02,
                1.1660e+03,  4.0900e+02,  3.5348e+00,  1.7970e+05])

*   __现在，你就可以使用这个“训练过的” imputer 来对训练集进行转换，将缺失值替换为中位数：__


        # 这里将数据填充到数据中，此时x就包含了我们全部的数据(当然非数值数据不在其中)。
        x = imputer.transform(housing_new)
        housing_tr = pd.DataFrame(x,columns=housing_new.columns) 

*   此时就已经将中位数填充到数据中了。总代码：



        from sklearn import impute
        imputer = impute.SimpleImputer(strategy='median')
        # 原数据中存在非数值的列，这里先将其删除，然后记录每一个属性的中位数
        housing_new = housing.copy(deep=True).drop('ocean_proximity',axis=1)

        imputer.fit(housing_new)
        # 这里将数据填充到数据中，此时x就包含了我们全部的数据(当然非数值数据不在其中)。
        x = imputer.transform(housing_new)
        housing_tr = pd.DataFrame(x,columns=housing_new.columns) 

