###  LableEncode

大多数机器学习算法跟喜欢和数字打交道，所以让我们把这些文本标签转换为数字。

*   Scikit-Learn 为这个任务提供了一个转换器 LabelEncoder ：

        from sklearn.preprocessing import LabelEncoder

        # 实例化对象
        le = LabelEncoder()
        housing_cat = housing['ocean_proximity']
        housing_encoding = le.fit_transform(housing_cat)
        display(housing_encoding)
        # 如果存在多列数据就不能使用LabelEncoder，可以使用factorize()
        housing_cat_encoded, housing_categories = housing_cat.factorize()
        housing_cat_encoded

        array([3, 3, 3, ..., 1, 1, 1])
        array([0, 0, 0, ..., 2, 2, 2], dtype=int64)


*   你可以查看映射表，编码器是通 过属性 classes_ 来学习的（ <1H OCEAN 被映射为 0， INLAND 被映射为 1，等等）

        le.classes_
        array(['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'],dtype=object)

*   查看映射表

        housing_categories
        Index(['NEAR BAY', '<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'ISLAND'], dtype='object')


__注意：__ 使用labelencode转换数据之后，对于有大小之分的数据可使用，对于无大小之分的数据存在问题，比如现在将数据转化为了 0 - 4的数值，那么 label1的特征就和label0 的特征距离近，所以相似，此时就需要使用onehot编码。