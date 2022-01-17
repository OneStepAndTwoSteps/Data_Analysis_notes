# `torch.utils 模块`


## <font color= #EC7063  >一、torch.utils.data：</font > 

* 这个功能包的作用是收集、打包数据，给数据索引，然后按照 `batch` 将数据分批喂给神经网络。


### <font color= #EC7063  >1、torch.utils.data.DataLoader：</font > 

* 数据读取的核心是 `torch.utils.data.DataLoader` 类。它是一个数据迭代读取器，支持 1）映射方式和迭代方式读取数据；2）自定义数据读取顺序；3）自动批；4）自动内存定位。

        DataLoader(dataset, batch_size=1, shuffle=False, sampler=None,batch_sampler=None, 
        num_workers=0, collate_fn=None,pin_memory=False, drop_last=False, timeout=0,worker_init_fn=None)


        dataset：       数据源；
        batch_size：    一个整数，定义每一批读取的元素个数；
        shuffle：       一个布尔值，定义是否随机读取；
        sampler：       定义获取数据的策略，必须与 shuffle 互斥；
        num_workers：   一个整数，读取数据使用的线程数；
        collate_fn：    一个将读取的数据处理、聚合成一个一个 batch 的自定义函数；
        drop_last：     一个布尔值，如果最后一批数据的个数不足 batch 的大小，是否保留这个 batch。

* `案例：`
  
        ## 生成一个可迭代的读取器，每一次读取为一个 batch，一个 batch 中包含32个数据(iteration)。
        train_data_loader = Data.DataLoader(train_data,batch_size=32,
                                            shuffle=True,num_workers=2)


* `相关概念：`

    `Epoch：` 所有训练样本都已输入到模型中，称为一个 epoch。

    `Iteration：`一批样本输入到模型中，称之为一个 iteration。
    
    `Batchsize：`批大小，决定一个 epoch 有多少个 iteration。


### <font color= #EC7063  >2、torch.utils.data.TensorDataset：</font > 

* `TensorDataset` 本质上与 `python zip` 方法类似，对数据进行打包整合。

* `案例：`

        ## 训练集X转化为张量
        train_xt = torch.from_numpy(boston_Xs.astype(np.float32))
        ## 训练集y转化为张量
        train_yt = torch.from_numpy(boston_y.astype(np.float32))
        ## 将训练集转化为张量后,使用TensorDataset将X和Y整理到一起
        train_data = Data.TensorDataset(train_xt,train_yt)



