### LabelBinarizer

使用 LabelBinarizer 相当于使用 LabelEncode +  OneHotEncode

*   exapmle

        from sklearn.preprocessing import LabelBinarizer
        encoder = LabelBinarizer()
        housing_cat_1hot = encoder.fit_transform(housing_cat) 
        housing_cat_1hot


__注意：__ 默认返回的结果是一个密集 NumPy 数组。

向构造器 LabelBinarizer 传递 sparse_output=True ，就可以得到一个稀疏矩阵,如:
    
     encoder = LabelBinarizer(sparse_output=True)。




