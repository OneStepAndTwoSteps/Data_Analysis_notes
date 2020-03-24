# 模型评估

sklearn 精确率，召回率，F1-Means 函数使用说明


### 准确率(precision_score)

#### 计算精确率
 
精确率是 tp / (tp + fp)的比例，其中tp是真正性的数量，fp是假正性的数量. 精确率直观地可以说是分类器不将负样本标记为正样本的能力.
 
精确率最好的值是1，最差的值是0.

#### Examples

    from sklearn.metrics import precision_score

    y_true = [0, 1, 2, 0, 1, 2]
    y_pred = [0, 2, 1, 0, 0, 1]
    print(precision_score(y_true, y_pred, average='macro'))  
    # 0.2222222222222222

    print(precision_score(y_true, y_pred, average='micro'))  
    # 0.3333333333333333

    print(precision_score(y_true, y_pred, average='weighted'))  
    # 0.2222222222222222

    print(precision_score(y_true, y_pred, average=None))  
    # [0.66666667 0.         0.        ]

 


### 召回率(recall_score)

#### 计算召回率
 
召回率是比率tp / (tp + fn)，其中tp是真正性的数量，fn是假负性的数量. 召回率直观地说是分类器找到所有正样本的能力.
召回率最好的值是1，最差的值是0.

#### Examples

    from sklearn.metrics import recall_score

    y_true = [0, 1, 2, 0, 1, 2]
    y_pred = [0, 2, 1, 0, 0, 1]
    print(recall_score(y_true, y_pred, average='macro'))  # 0.3333333333333333
    print(recall_score(y_true, y_pred, average='micro'))  # 0.3333333333333333
    print(recall_score(y_true, y_pred, average='weighted'))  # 0.3333333333333333
    print(recall_score(y_true, y_pred, average=None))  # [1. 0. 0.]





###  f1-means


#### 计算F1 score，它也被叫做F-score或F-measure.
 
F1 score可以解释为精确率和召回率的加权平均值. F1 score的最好值为1，最差值为0. 精确率和召回率对F1 score的相对贡献是相等的. F1 score的计算公式为：
F1 = 2 * (precision * recall) / (precision + recall)


#### Examples

    >>>
    >>> from sklearn.metrics import f1_score
    >>> y_true = [0, 1, 2, 0, 1, 2]
    >>> y_pred = [0, 2, 1, 0, 0, 1]
    >>> f1_score(y_true, y_pred, average='macro')  
    0.26...
    >>> f1_score(y_true, y_pred, average='micro')  
    0.33...
    >>> f1_score(y_true, y_pred, average='weighted')  
    0.26...
    >>> f1_score(y_true, y_pred, average=None)
    array([0.8, 0. , 0. ])



## 参数介绍：

#### 参数：

y_true : 一维数组，或标签指示符 / 稀疏矩阵，实际（正确的）标签.

y_pred : 一维数组，或标签指示符 / 稀疏矩阵，分类器返回的预测标签.

labels : 列表，可选值. 当average != binary时被包含的标签集合，如果average是None的话还包含它们的顺序. 在数据中存在的标签可以被排除，比如计算一个忽略多数负类的多类平均值时，数据中没有出现的标签会导致宏平均值（marco average）含有0个组件. 对于多标签的目标，标签是列索引. 默认情况下，y_true和y_pred中的所有标签按照排序后的顺序使用.

pos_label : 字符串或整型，默认为1. 如果average = binary并且数据是二进制时需要被报告的类. 若果数据是多类的或者多标签的，这将被忽略；设置labels=[pos_label]和average != binary就只会报告设置的特定标签的分数.

average : 字符串，可选值为[None, ‘binary’ (默认), ‘micro’, ‘macro’, ‘samples’, ‘weighted’]. 多类或	者多标签目标需要这个参数. 如果为None，每个类别的分数将会返回. 否则，它决定了数据的平均值类型.

‘binary’: 仅报告由pos_label指定的类的结果. 这仅适用于目标（y_{true, pred}）是二进制的情况.

‘micro’: 通过计算总的真正性、假负性和假正性来全局计算指标.

‘macro’: 为每个标签计算指标，找到它们未加权的均值. 它不考虑标签数量不平衡的情况.

‘weighted’: 为每个标签计算指标，并通过各类占比找到它们的加权均值（每个标签的正例数）.它解决了’macro’的标签不平衡问题；它可以产生不在精确率和召回率之间的F-score.

‘samples’: 为每个实例计算指标，找到它们的均值（只在多标签分类的时候有意义，并且和函数accuracy_score不同）.

sample_weight : 形状为[样本数量]的数组，可选参数. 样本权重.

#### 返回值：

precision : 浮点数(如果average不是None) 或浮点数数组, shape =[唯一标签的数量]
二分类中正类的精确率或者在多分类任务中每个类的精确率的加权平均.

