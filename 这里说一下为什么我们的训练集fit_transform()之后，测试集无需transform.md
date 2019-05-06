
### 这里说一下为什么我们的训练集fit_transform()之后，测试集无需transform
                
我们在做一个数据归一化的时候，在train的时候用到了：train_ss_x = ss.fit_transform(train_x)
            
实际上：fit_transform是fit和transform两个函数都执行一次。所以ss是进行了fit拟合的。 __只有在fit拟合之后，才能进行transform。__
        
在进行test的时候，我们已经在train的时候fit过了，所以直接transform即可。
             
另外，如果我们没有fit，直接进行transform会报错，因为需要先fit拟合，才可以进行transform。

__补充:__
             
其他地方也是同理，如果我们的模型已经fit_transform了，后面我们只用transform即可

