### DictVectorizer 特征提取

我们在进行模型训练时，如果特征值里有一些特征是字符串，这样会不方便后续的运算，需要转成数值类型，比如在决策树中的泰坦尼克获救率资料中的 Sex 字段，有 male 和 female 两种取值。我们可以把它变成 Sex=male 和 Sex=female 两个字段，数值用 0 或 1 来表示。同理其中的 Embarked 有 S、C、Q 三种可能，我们也可以改成 Embarked=S、Embarked=C 和 Embarked=Q 三个字段，数值用 0 或 1 来表示。

这里你可能会疑惑为什么有三个可能性为什么只用0/1就可以表示呢？其实在转化为字典之后我们可以发现 Embarked=S 成了一个字段 Embarked=C 成了一个字段 和 Embarked=Q 也成了一个字段，现在相当于我们将 Embarked变为三个字段，如果数据中 Embarked 是等于 C，那么我们将其标记为1即可，因为S C Q 是互斥的。如果还不是很清楚的话可以看示例。

那该如何操作呢，我们可以使用 sklearn 特征选择中的 DictVectorizer 类，用它将可以处理符号化的对象，将符号转成数字 0/1 进行表示。

__DictVectorizer将特征值映射列表转换为向量。__

__导入模块：__
   
    from sklearn.feature_extraction import DictVectorizer 

__类：__
   
    DictVectorizer（dtype = <class'numpy.float64'>，separator ='='，sparse = True，sort = True ）

__相关参数：__

__dtype：__ callable, 可选参数, 默认为float。特征值的类型，传递给Numpy.array或者Scipy.sparse矩阵构造器作为dtype参数。

__separator:__ string, 可选参数, 默认为"="。当构造One-hot编码的特征值时要使用的分割字符串。分割传入字典数据的键与值的字符串，生成的字符串会作为特征矩阵的列名。

__sparse:__ boolearn, 可选参数,默认为True。transform是否要使用scipy产生一个sparse矩阵。DictVectorizer的内部实现是将数据直接转换成sparse矩阵，如果sparse为False， 再把sparse矩阵转换成numpy.ndarray型数组。

__sort：__ boolearn,可选参数,默认为True。在拟合时是否要多feature_names和vocabulary_进行排序。


### 使用注意：

在进行特征的提取之前需要将数据转化为字典格式。

