# `torchvision` 

`torchvision` 是独立于 `PyTorch` 的关于 `图像操作` 的一个工具库，目前包括六个模块：

* 1）`torchvision.datasets：`几个常用视觉数据集，可以下载和加载，以及如何编写自己的 `Dataset。`

* 2）`torchvision.models：`经典模型，例如 `AlexNet、VGG、ResNet` 等，以及训练好的参数。

* 3）`torchvision.transforms：`常用的图像操作，如 `随机切割`、`旋转`、`数据类型转换`、`tensor` 与 `numpy` 和 `PIL` `Image` 的互换等。

* 4）`torchvision.ops：`提供 `CV` 中常用的一些操作，比如 `NMS、ROI_Align、ROI_Pool` 等。

* 5）`torchvision.io：`提供输入输出的一些操作，目前针对的是视频的写入写出。

* 6）`torchvision.utils：`其他工具，比如产生一个图像网格等。