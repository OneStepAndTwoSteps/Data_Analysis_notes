### 基于spark的PrefixSpan的使用案例：

使用条件：

__1、安装java环境，配置环境变量__

__2、安装spark，配置环境变量__

__3、安装scala，配置环境变量__

__4、安装hadoop环境，配置环境变量__


### Spark MLlib关联算法参数介绍

对于PrefixSpan类， 使用它的训练函数train主要需要输入四个参数：序列项集data，支持度阈值minSupport， 最长频繁序列的长度maxPatternLength 和最大单机投影数据库的项数maxLocalProjDBSize。支持度阈值minSupport的定义和FPGrowth类类似，唯一差别是阈值默认值为0.1。maxPatternLength限制了最长的频繁序列的长度，越小则最后的频繁序列数越少。maxLocalProjDBSize参数是为了保护单机内存不被撑爆。如果只是是少量数据的学习，可以忽略这个参数。

