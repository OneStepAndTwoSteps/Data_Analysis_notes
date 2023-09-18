# 混合精度


混合精度指代的是单精度 float和半精度 float16 混合：

## 为什么需要半精度：

float16和float相比恰里，总结下来就是两个原因：内存占用更少，计算更快。

* 内存占用更少：这个是显然可见的，通用的模型 fp16 占用的内存只需原来的一半。memory-bandwidth 减半所带来的好处：

    * 模型占用的内存更小，训练的时候可以用更大的batchsize。
    
    * 模型训练时，通信量（特别是多卡，或者多机多卡）大幅减少，大幅减少等待时间，加快数据的流通。

* 计算更快：
    
    * 目前的不少GPU都有针对 fp16 的计算进行优化。论文指出：在近期的GPU中，半精度的计算吞吐量可以是单精度的 2-8 倍；



## 混合精度的计算：

* float16数据类型的元素占2个bytes，float32数据类型的元素占4个bytes。在混合精度训练中，会使用float16的模型参数进行前向传递和后向传递，计算得到float16的梯度；在优化器更新模型参数时，会使用float32的优化器状态、float32的梯度、float32的模型参数来更新模型参数。


    <div align=center><image src= "./static/1_htZ4PF2fZ0ttJ5HdsIaAbQ.webp" ></image><div>

* （其中float32的梯度是float16经过loss scale转过来的）

    <div align=center><image src= "./static/Snipaste_2023-09-18_17-25-50.png" ></image><div>

* 如果不使用混合精度，那么在进行前向传播的和反向传播的时候会使用 float32 存储梯度，相比于混合精度增加了很多的显存占用




## 参考

* [Understanding Mixed Precision Training] https://towardsdatascience.com/understanding-mixed-precision-training-4b246679c7c4

* n[分析transformer模型的参数量、计算量、中间激活、KV cache] https://zhuanlan.zhihu.com/p/624740065