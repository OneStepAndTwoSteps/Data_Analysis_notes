# `mmpretrain`


## `一、configs/_base_ `

* 在 configs/_base_ 文件夹下有 4 个基本组件类型，分别是：

    * 模型(model)

    * 数据(data)

    * 训练策略(schedule)

    * 运行设置(runtime)

  你可以通过继承一些基本配置文件轻松构建自己的训练配置文件。我们称这些被继承的配置文件为 原始配置文件，如 `_base_` 文件夹中的文件一般仅作为原始配置文件。

### `1.1、 resnet18_8xb32_in1k.py：`

* 下面使用 resnet18_8xb32_in1k.py 配置文件 作为案例进行说明并注释每一行含义:

        _base_ = [                                    # 此配置文件将继承所有 `_base_` 中的配置
            '../_base_/models/resnet18.py'',           # 模型配置
            '../_base_/datasets/imagenet_bs32.py',    # 数据配置
            '../_base_/schedules/imagenet_bs256.py',  # 训练策略配置
            '../_base_/default_runtime.py'            # 默认运行设置
        ]


  现在的配置文件只有简短的几行，我们可以通过执行 train.py 跟上对应的参数
  来生成完整的配置文件，在生成完整的配置之后，各个配置参数的含义：


* `model 块: `

        model = dict(
            type='ImageClassifier',  # 模型类型是图像分类
            
            --- backbone 特征提取：--- 
            backbone=dict(
                type='ResNet',  # 使用ResNet作为backbone
                depth=18,  # ResNet的深度为18层
                num_stages=4,  # ResNet的阶段数量为4
                out_indices=(3, ),  # ResNet输出的stage位置，这里只输出第三个stage
                style='pytorch'
            ),

            --- 以上部分通常不进行调整 ---

            --- Neck 特征融合 ---
            neck=dict(type='GlobalAveragePooling'),  # 使用全局平均池化层作为neck

            --- head 分类 ---
            head=dict(
                type='LinearClsHead',  # 使用全连接层作为分类器
                num_classes=102,  # 分类数量为102
                in_channels=512,  # 输入通道数为512
                loss=dict(type='CrossEntropyLoss', loss_weight=1.0),  # 使用交叉熵作为损失函数
                topk=(1, 5)  # 记录top-k的准确率
            )
        )

    * `Backbone：`通常用于提取输入数据的特征，比如图像分类任务中的卷积层或者是图像分割任务中的编码器部分。我们可以通过修改 backbone 的类型、深度、宽度、输出通道数等参数来改变特征提取的效果。


      * `out_indices=(3, )：` ResNet18 ，一共有 18 层，其中根据卷据和残差层的组合分别分为了 4 个 Stage ,`out_indices=(3, )` 表示只输出 ResNet 的第 4 个 stage 的特征。：

          <div align=center><img width=700 src="./static/ResNet18_50.jpg"/></div>


    * `Neck：`用于将 backbone 中提取的特征进行融合，从而获得更加高级别的特征表示。比如在目标检测任务中，我们可以使用 FPN 架构将不同尺度的特征进行融合。在图像分类任务中，我们可以使用平均池化、自适应平均池化、最大池化等操作将特征进行压缩和融合，从而得到更加紧凑的特征表示。

    * `Head：`通常用于最终的分类、回归、分割等任务，比如在图像分类任务中，我们可以通过添加全连接层或者是卷积层来完成分类任务。我们可以修改 head 的类型、类别数、激活函数、损失函数等参数来改变模型的输出。


* `data 块: `

        data = dict(
            samples_per_gpu=8,
            workers_per_gpu=2,
            train=dict(
                type='ImageNet',                                        ## 指定加载数据的数据类，可以自定义
                data_prefix='../mmcls/data/flower_data/train_filelist', ## 指定图片存放的路径
                ann_file='../mmcls/data/flower_data/train.txt',         ## 每张图片对应的标签
                pipeline=train_pipeline
            ),
            val=dict(
                type='ImageNet',
                data_prefix='../mmcls/data/flower_data/val_filelist',
                ann_file='../mmcls/data/flower_data/val.txt',
                pipeline=test_pipeline
            ),
            test=dict(
                type='ImageNet',
                data_prefix='../mmcls/data/flower_data/val_filelist',
                ann_file='../mmcls/data/flower_data/val.txt',
                pipeline=test_pipeline
            )
        )


    * `type：`有的时候当我们训练一个比 `ImageNet` 分类数更小的模型时，就有可能会报错，此时我们就需要自定义类，在自定义类中指明我们每一个类别的描述信息，自定义类放在 `\mmcls\datasets` 中，如 `\mmcls\datasets\my_filelist.py` 。


    * `需要注意的是：`在自定义 `数据处理类(如 MyFilelist)` 的时候，需要仿照  `mmcls\datasets\imagenet.py` 的写法，并且还需要将你定义的类，添加到 `datasets\__init__.py` 中

            from .my_filelist import MyFilelist  ## <-- 新增的自定义处理类

            __all__ = [
                'BaseDataset', 'ImageNet', 'CIFAR10', 'CIFAR100', 'MNIST', 'FashionMNIST',
                'VOC', 'MultiLabelDataset', 'build_dataloader', 'build_dataset',
                'DistributedSampler', 'ConcatDataset', 'RepeatDataset',
                'ClassBalancedDataset', 'DATASETS', 'PIPELINES', 'ImageNet21k', 'SAMPLERS',
                'build_sampler', 'RepeatAugSampler', 'KFoldDataset', 'MyFilelist', ## <-- 新增的自定义处理类
            ]



