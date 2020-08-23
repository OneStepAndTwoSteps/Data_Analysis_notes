
## classification_report

sklearn 中的 classification_report 函数用于显示主要分类指标的文本报告．在报告中显示每个类的精确度，召回率，F1值等信息。


### 导入包

    from sklearn.metrics import classification_report


### 参数讲解

    y_true：1维数组，或标签指示器数组/稀疏矩阵，目标值。 

    y_pred：1维数组，或标签指示器数组/稀疏矩阵，分类器返回的估计值。 

    labels：array，shape = [n_labels]，报表中包含的标签索引的可选列表。 

    target_names：字符串列表，与标签匹配的可选显示名称（相同顺序）。 

    sample_weight：类似于shape = [n_samples]的数组，可选项，样本权重。 

    digits：int，输出浮点值的位数．


### 输出结果

    y_true 为样本真实标记，y_pred 为样本预测标记

    support：某类别在测试数据中的样本个数，测试数据中有 1 个样本的真实标签为 class 0

    precision：模型预测的结果中有多少是预测正确的

    micro avg：计算所有数据下的指标值，比如全部数据 5 个样本中有 3 个预测正确，故 micro avg 为 0.6
    
    macro avg：每个类别评估指标未加权的平均值，比如准确率的 macro avg，(0.50+0.00+1.00)/3=0.5

    weighted avg：加权平均，比如第一个值的计算方法，(0.50*1 + 0.0*1 + 1.0*3)/5 = 0.70



### 输出结果说明

以下面例子为例


#### 例子1

    1、标签labels 和 target_name

        target_names = ['class 0','class 1','class 2'] 分别是 labels = [0,1,2] 的命名

        最终以 y_pred 的结果为标准 进行分类，如下 y_pred = [0, 0, 2, 2, 1] [0,1,2]我们看出是三分类，所以labels默认为[0,1,2] 

        class 0 就是表示我们 label = 0 的也就是我们的分类标签 0

    2、support

        support表示某类别在测试数据中的样本个数，从class 0 为例 我们能看出测试数据中有 1 个样本的真实标签为 class 0，其实就是y_true有几个0，support就有几个

    3、然后就是分别表示 class 0 1 2 的精确率，召回率，f1

        micro avg：计算所有数据下的指标值，比如全部数据 5 个样本中有 3 个预测正确，故 micro avg 为 0.6
        
        macro avg：每个类别评估指标未加权的平均值，比如以 precision 为例 macro avg，(0.50+0.00+1.00)/3=0.5

        weighted avg：加权平均，比如比如以 precision 为例，(0.50*1 + 0.0*1 + 1.0*3)/5 = 0.70

#### 例子2   

    其实例子2 中labels默认只有2个，我们这里可以指定显示出3个，不过没什么意义




### 案例

__直接将预测值和真实值进行对比即可__

__例子__

    >>> from sklearn.metrics import classification_report
    >>> y_true = [0, 1, 2, 2, 2]
    >>> y_pred = [0, 0, 2, 2, 1]
    >>> target_names = ['class 0', 'class 1', 'class 2']
    >>> print(classification_report(y_true, y_pred, target_names=target_names))

__out__    

                precision    recall  f1-score   support

        class 0       0.50      1.00      0.67         1
        class 1       0.00      0.00      0.00         1
        class 2       1.00      0.67      0.80         3

    accuracy                              0.60         5
    macro avg         0.50      0.56      0.49         5
    weighted avg      0.70      0.60      0.61         5



__例子__

    >>> y_pred = [1, 1, 0]
    >>> y_true = [1, 1, 1]
    >>> print(classification_report(y_true, y_pred, labels=[1, 2, 3]))

__out__     
 
                precision    recall  f1-score   support

            1       1.00      0.67      0.80         3
            2       0.00      0.00      0.00         0
            3       0.00      0.00      0.00         0

    micro avg       1.00      0.67      0.80         3
    macro avg       0.33      0.22      0.27         3
    weighted avg    1.00      0.67      0.80         3
