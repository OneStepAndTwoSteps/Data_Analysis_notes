## StratifiedKFold和KFold的主要区别

StratifiedKFold用法类似Kfold，但是他是分层采样，确保训练集，测试集中各类别样本的比例与原始数据集中相同。

__举个例子：__

    import numpy as np
    from sklearn.model_selection import StratifiedKFold,KFold

    X=np.array([
        [1,2,3,4],
        [11,12,13,14],
        [21,22,23,24],
        [31,32,33,34],
        [41,42,43,44],
        [51,52,53,54],
        [61,62,63,64],
        [71,72,73,74]
    ])

    y=np.array([1,1,0,0,1,1,0,0])


__KFold:__

    #按顺序分别取第1-2、3-4、5-6和7-8的数据。
    kfolder = KFold(n_splits=4,random_state=1)
    for train, test in kfolder.split(X,y):
    print('Train: %s | test: %s' % (train, test),'\n')

__out__

    Train: [2 3 4 5 6 7] | test: [0 1] 

    Train: [0 1 4 5 6 7] | test: [2 3] 

    Train: [0 1 2 3 6 7] | test: [4 5] 

    Train: [0 1 2 3 4 5] | test: [6 7] 


__StratifiedKFold:__

    #依照标签的比例来抽取数据，本案例集标签0和1的比例是1：1
    #因此在抽取数据时也是按照标签比例1：1来提取的
    sfolder = StratifiedKFold(n_splits=4,random_state=1)
    for train, test in sfolder.split(X,y):
    print('Train: %s | test: %s' % (train, test))

__out__

    Train: [1 3 4 5 6 7] | test: [0 2]  # 0对应上面的第0个样本-标签1 2对应上面的第2个样本-标签0

    Train: [0 2 4 5 6 7] | test: [1 3]

    Train: [0 1 2 3 5 7] | test: [4 6]

    Train: [0 1 2 3 4 6] | test: [5 7]
    

#### 小结

我们可以看出在测试集中，我们的 StratifiedKFold 0和1标签的比例是1：1，而KFold没有。
