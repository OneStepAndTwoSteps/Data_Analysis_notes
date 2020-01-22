# ShuffleSplit

sklearn.model_selection.ShuffleSplit类用于将样本集合随机“打散”后划分为训练集、测试集(可理解为验证集，下同)，类申明如下：

## 方法

class sklearn.model_selection.ShuffleSplit(n_splits=10, test_size=None, train_size=None, random_state=None)

### 参数：

    n_splits:int, 划分训练集、测试集的次数，默认为10

    test_size:float, int, None, default=0.1； 测试集比例或样本数量，该值为[0.0, 1.0]内的浮点数时，表示测试集占总样本的比例；该值为整型值时，表示具体的测试集样本数量；train_size不设定具体数值时，该值取默认值0.1，train_size设定具体数值时，test_size取剩余部分

    train_size:float, int, None； 训练集比例或样本数量，该值为[0.0, 1.0]内的浮点数时，表示训练集占总样本的比例；该值为整型值时，表示具体的训练集样本数量；该值为None(默认值)时，训练集取总体样本除去测试集的部分

    random_state:int, RandomState instance or None；随机种子值，默认为None


ShuffleSplit类方法包括get_n_splits、split，前者用于返回划分训练集、测试集的次数，后者申明如下：

split(X, y=None, groups=None)

    X：array-like, shape (n_samples, n_features)；样本特征集合

    y：array-like, shape (n_samples,)；样本标记集合，该值设置时需与X的样本数量(n_samples)一致

    groups：该参数在此处不生效

    返回值：包含训练集、测试集索引值的迭代器


### 案例：

cv_split = model_selection.ShuffleSplit(n_splits = 10, test_size = .3, train_size = .6, random_state = 0 )
