### __StratifiedKFold

StratifiedKFold用法类似Kfold，但是他是分层采样，确保训练集，测试集中各类别样本的比例与原始数据集中相同。

__StratifiedKFold:__

    #依照标签的比例来抽取数据，本案例集标签0和1的比例是1：1

    #因此在抽取数据时也是按照标签比例1：1来提取的

    import numpy as np
    from sklearn.model_selection import StratifiedKFold

    X=np.array([

    0    [1,2,3,4],
    1    [11,12,13,14], 
    2    [21,22,23,24], 
    3    [31,32,33,34], 
    4    [41,42,43,44], 
    5    [51,52,53,54], 
    6    [61,62,63,64], 
    7    [71,72,73,74]  

    ])

    y=np.array([1,1,0,0,1,1,0,0])


    sfolder = StratifiedKFold(n_splits=4,random_state=1)
    
    for train, test in sfolder.split(X,y):
    
    print('Train: %s | test: %s' % (train, test))

__out__

    Train: [1 3 4 5 6 7] | test: [0 2]  # 0对应上面的第0个样本-标签1 2对应上面的第2个样本-标签0

    Train: [0 2 4 5 6 7] | test: [1 3]

    Train: [0 1 2 3 5 7] | test: [4 6]

    Train: [0 1 2 3 4 6] | test: [5 7]