# `nn.module 模块`

* `torcn.nn` 是专门为神经网络设计的模块化接口. `nn` 构建于 `autograd` 之上，可以用来定义和运行神经网络。

* `nn.Module` 是 `nn` 中十分重要的类，包含网络各层的定义及 `forward` 方法。

## `一、定义神经的网络：`

### `1、nn.module 定义网络`

* 需要继承 `nn.Module` 类，并实现 `forward` 方法。继承 `nn.Module` 类之后，在构造函数中要调用 `Module` 的构造函数, `super(Linear, self).init()`

* 一般把网络中具有可学习参数的层放在构造函数 `__init__()` 中。

* 不具有可学习参数的层（如 `ReLU` ）可放在构造函数中，也可不放在构造函数中（而在 `forward` 中使用 `nn.functional` 来代替）。可学习参数放在构造函数中，并且通过 `nn.Parameter()` 使参数以 `parameters`（一种 `tensor` ,默认是自动求导）的形式存在 `Module` 中，并且通过 `parameters()` 或者 `named_parameters()` 以迭代器的方式返回可学习参数。
* 只要在 `nn.Module` 中定义了 `forward` `函数，backward` 函数就会被自动实现（利用 `Autograd` )。而且一般不是显式的调用 `forward(layer.forward)` , 而是 `layer(input)` , 会自执行 `forward()` .


### `2、案例：`

* `第一种方式：直接按照顺序构造神经网络，不在init 中使用激活函数，而在 forward 中通过nn.functional 用激活函数 `

        import torch
        import torch.nn as nn
        import torch.nn.functional as F
        from torch.optim import SGD
        import torch.utils.data as Data


        ## 搭建全连接神经网络回归网络
        class DNNregression(nn.Module):
            def __init__(self):
                super(DNNregression,self).__init__()
                ## 定义第一个隐藏层
                self.hidden1 = nn.Linear(in_features = 8,
                                        out_features = 100,bias=True)
                ## 定义第二个隐藏层
                self.hidden2 = nn.Linear(100,100)
                ## 定义第三个隐藏层
                self.hidden3 = nn.Linear(100,50)
                ## 回归预测层
                self.predict = nn.Linear(50,1)

            ## 定义网络的向前传播路径   
            def forward(self, x):
                x = F.relu(self.hidden1(x))
                x = F.relu(self.hidden2(x))
                x = F.relu(self.hidden3(x))
                output = self.predict(x)
                ## output 为二维向量，这里限制输出为一维向量
                return output[:,0]



* `第二种方式：使用 nn.Sequential 将多个功能成连接到一起`

        ## 定义全连接网络
        class MLPclassifica(nn.Module):
            def __init__(self):
                super(MLPclassifica,self).__init__()
                ## 定义第一个隐藏层
                self.hidden1 = nn.Sequential(
                    nn.Linear(
                        in_features = 57, ## 第一个隐藏层的输入，数据的特征数
                        out_features = 30,## 第一个隐藏层的输出，神经元的数量
                        bias=True, ## 默认会有偏置
                    ),
                    nn.ReLU()
                )
                ## 定义第二个隐藏层
                self.hidden2 = nn.Sequential(
                    nn.Linear(30,10),
                    nn.ReLU()
                )
                ## 分类层
                self.classifica = nn.Sequential(
                    nn.Linear(10,2),
                    nn.Sigmoid()
                )

            ## 定义网络的向前传播路径   
            def forward(self, x):
                fc1 = self.hidden1(x)
                fc2 = self.hidden2(fc1)
                output = self.classifica(fc2)
                ## 输出为两个隐藏层和输出层的输出
                return fc1,fc2,output
                
        ## 输出我们的网络结构
        mlpc = MLPclassifica()
        print(mlpc)


