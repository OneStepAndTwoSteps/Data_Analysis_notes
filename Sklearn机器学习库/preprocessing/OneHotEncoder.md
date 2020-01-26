### OneHotEncoder

将分类要素编码为一键式数字数组。

该转换器的输入应为整数或字符串之类的数组，表示分类（离散）特征所采用的值。使用单热（又名“ one-of-K”或“ dummy”）编码方案对特征进行编码。这将为每个类别创建一个二进制列，并返回一个稀疏矩阵或密集数组（取决于sparse 参数）

默认情况下，编码器会根据每个要素中的唯一值得出类别。或者，您也可以categories 手动指定。

需要这种编码才能将分类数据提供给许多scikit学习估计器，尤其是线性模型和具有标准内核的SVM。

注意：y标签的一键编码应改用LabelBinarizer。

*   __参数：__

    __categories‘auto’ or a list of array-like, default=’auto’__
        
    *   'auto'：根据训练数据自动确定类别。也就是根据labelencode出来的数字进行确定类别

    *   'list'：categories[i]保存第ith列中预期的类别。传递的类别不应在单个功能中混合使用字符串和数字值，并且应该对数字值进行排序。
    
    __drop‘first’ or a array-like of shape (n_features,), default=None__

        指定一种用于删除每个功能类别之一的方法。这在完美共线特征导致问题的情况下很有用，例如将结果数据输入神经网络或不规则回归时。

        无：保留所有功能（默认）。

        'first'：删除每个功能中的第一个类别。如果仅存在一个类别，则该功能将被完全删除。

        array：drop[i]是功能中应该删除的类别。X[:, i]

    __sparse：bool__

        如果设置为True，将返回稀疏矩阵，否则将返回数组

    __dtype：number__

        所需的输出dtype。

    __handle_unknown{‘error’, ‘ignore’}, default=’error’__

        在转换过程中是否引发错误或忽略是否存在未知分类特征（默认为引发）。
        当此参数设置为“忽略”并且在转换过程中遇到未知类别时，此功能生成的一键编码列将全为零。
        在逆变换中，未知类别将表示为“无”。

*   __Attributes__

    __categories_list of arrays__ 

        在拟合过程中确定的每个特征的类别（按X中特征的顺序，并与的输出相对应transform）。这包括drop （如果有）中指定的类别。

    __drop_idx_array of shape (n_features,)__

        drop_idx_[i]是categories_[i]每个功能要删除的类别的索引。如果将保留所有已转换的要素，则为None。


### example

*   __导入包，并实例化对象__

        from sklearn.preprocessing import OneHotEncoder
        ohe = OneHotEncoder(categories='auto')
        housing_cat = housing['ocean_proximity']

*   __1、使用labelencode转化的结果进行onehot__
*   但是要注意，我们只有一列数据，而使用fit_transform函数需要2D数据，这里我们需要使用reshape函数转换

        housing_cat_1hot = ohe.fit_transform(housing_cat_encoded.reshape(-1,1))

*   __2、或者直接进行onehot转换__

        # housing_hot_encoded = ohe.fit_transform(housing[['ocean_proximity']])
        # housing_hot_encoded

*   __输出一个Scipy的稀疏矩阵__

    <20640x5 sparse matrix of type '<class 'numpy.float64'>'
        with 20640 stored elements in Compressed Sparse Row format>

