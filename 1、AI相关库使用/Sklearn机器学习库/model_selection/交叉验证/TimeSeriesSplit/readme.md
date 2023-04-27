# 时间序列分割 TimeSeriesSplit

    sklearn.model_selection.TimeSeriesSplit

    class sklearn.model_selection.TimeSeriesSplit(n_splits=5, max_train_size=None) 

## TimeSeriesSplit 的使用

`介绍：`

    按照时间进行切分，会根据指定的 kfold 值，对数据切割成相应的分数，并且是呈顺序的，也就是后面切割出来的数据，是包含前面的数据的。

`案例：`

    from sklearn.model_selection import TimeSeriesSplit

    kfold = 7
    tss = TimeSeriesSplit(n_splits=kfold)

    for tr_idx, val_idx in tss.split(X_train, y_train):
        print('tr_idx: ',tr_idx)
        print('val_idx: ',val_idx)    


`输出结果：`

    tr_idx:  [    0     1     2 ... 12497 12498 12499]
    val_idx:  [12500 12501 12502 ... 24997 24998 24999]
    tr_idx:  [    0     1     2 ... 24997 24998 24999]
    val_idx:  [25000 25001 25002 ... 37497 37498 37499]
    tr_idx:  [    0     1     2 ... 37497 37498 37499]
    val_idx:  [37500 37501 37502 ... 49997 49998 49999]
    tr_idx:  [    0     1     2 ... 49997 49998 49999]
    val_idx:  [50000 50001 50002 ... 62497 62498 62499]
    tr_idx:  [    0     1     2 ... 62497 62498 62499]
    val_idx:  [62500 62501 62502 ... 74997 74998 74999]
    tr_idx:  [    0     1     2 ... 74997 74998 74999]
    val_idx:  [75000 75001 75002 ... 87497 87498 87499]
    tr_idx:  [    0     1     2 ... 87497 87498 87499]
    val_idx:  [87500 87501 87502 ... 99997 99998 99999]





