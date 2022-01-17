# `CNN channels`

## 一、关于 `channels` (通道)：

`channels` 分为三种：

1、最初输入的图片样本的 `channels` ，取决于图片类型，比如 `RGB` ；

2、卷积操作完成后输出的 `out_channels` ，取决于卷积核的数量。此时的 `out_channels` 也会作为下一次卷积时的卷积核的 `in_channels` ；

3、卷积核中的 `in_channels` ，刚刚2中已经说了，就是上一次卷积的 `out_channels` ，如果是第一次做卷积，就是1中样本图片的 `channels` 。


## 二、关于 `cnn` 中的 `shape：`


* `1、输入层 shape：`根据输入数据的 `shape` 得到：

    比如现在通过 `DataLoader` 读取数据，然后通过 `for` 循环读取到一个 `batch`：

        train_data_loader = Data.DataLoader(train_data,batch_size=32,
                                        shuffle=True,num_workers=2)

        for step, (b_x, b_y) in enumerate(train_data_loader):  
            if step > 0:
                break

        b_x.shape
        torch.Size([32, 3, 224, 224])
               
    `torch.Size([32, 3, 224, 224])` 分别对应： `[batch,channels,height,width]`


* `2、卷积核 shape：` 


        ## 第一层卷积核：torch.Size([16, 1, 3, 3])
        a = nn.Conv2d(          
                in_channels = 3,        ## 输入的feature map
                out_channels = 64,      ## 输出的feature map
                kernel_size = 3,        ##卷积核尺寸
                stride=1,               ##卷积核步长
                padding=1,              # 进行填充)
                
        a
        Conv2d(3, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))

        a.weight.shape
        torch.Size([64, 3, 3, 3])

    `torch.Size([64, 3, 3, 3])` 分别对应： `64` 个 `3*3` 的卷积核。

    `in_channels：`卷积核中的 `in_channels` ，就是上一次卷积的 `out_channels` ，如果是第一次做卷积，就是样本图片的 `channels` 。




