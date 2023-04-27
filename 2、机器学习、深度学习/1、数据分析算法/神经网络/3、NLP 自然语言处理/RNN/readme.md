# `RNN 循环神经网络`

普通的神经网络，它们都只能单独的取处理一个个的输入，前一个输入和后一个输入是完全没有关系的。但是，某些任务需要能够更好的处理序列的信息，即前面的输入和后面的输入是有关系的，我们可以通过 RNN 来帮助解决。


## `循环神经网络`

循环神经网络通过使用自反馈的神经元，能够处理任意长度的时序数据。

`给定一串输入数据：`

<div align=center><img  height="50" src="./static/2.jpg"/></div>

`RNN` 通过下面公式更新带反馈变的隐藏层的 `活性值 h(t)`

<div align=center><img height="50"  src="./static/3.jpg"/></div>


`RNN` 模型有比较多的变种，这里介绍最主流的RNN模型结构如下：

<div align=center><img width="800" height="600"  src="./static/rnn模型.jpg"/></div>



## `RNN 前向传播`
   
对于一个简单 RNN 网络在 t 时刻的更新公式为：

<div align=center><img width="450" height="200"  src="./static/4-1.jpg"/></div>

`其中：`

* `xt` 为 `t时刻网络的输入`

* `ht` 为 `t时刻隐藏层的活性值`，此时ht不仅和当前时刻的输入xt 有关，也和上一个时刻的隐藏状态值ht-1 相关。

* `zt` 为 `t时刻隐藏层的净输入`

* `U` 为 `状态权重矩阵`

* `W` 为 `状态输入矩阵`

* `b` 为 `偏置项`

* `f(·)` 为 `非线性激活函数` ，通常为 `Tanh`或者 `sigmoid`


## `反向传播：`

`定义损失函数 L` ，其中的 `g(ht)` 为 `t时刻` 的 `输出` 。

<div align=center><img width="450" height="200"  src="./static/损失函数.jpg"/></div>

`整个序列的损失函数关于 U 求导：`

<div align=center><img width="450" height="200"  src="./static/反向传播1.jpg"/></div>

`对 U 进行求导：`

<div align=center><img   src="./static/反向传播2.jpg"/></div>



`补充：`

* `[hk-1]j` 意为第 `k-1时刻` 隐状态的 `j` 维，`i[]` 为除了第 `i` 行值为 `x` 外，其余都为 `0` 的 `行向量`。其实就是一个第 `i` 行的 `行向量`，其中第 `j` 列为` hk-1` 其他列为 `0`.

`最后：`

<div align=center><img  width="600" height="280" src="./static/反向传播3.jpg"/></div>

## `RNN 小结：`

* `RNN` 虽然理论上可以很漂亮的解决序列数据的训练，但是它也像 `DNN` 一样有 `梯度消失` 时的问题，当序列很长的时候问题尤其严重。因此，上面的 `RNN` 模型一般不能直接用于应用领域。在语音识别，手写书别以及机器翻译等 `NLP` 领域实际应用比较广泛的是基于 `RNN` 模型的一个特例 `LSTM` 。

* `RNN` 的独特价值在于：它能有效的处理序列数据。比如：文章内容、语音音频、股票价格走势…

    `之所以他能处理序列数据，是因为在序列中前面的输入也会影响到后面的输出，相当于有了“记忆功能”。`但是 `RNN` 存在严重的短期记忆问题，长期的数据影响很小（哪怕他是重要的信息）。

    于是基于 `RNN` 出现了 `LSTM` 和 `GRU` 等变种算法。



## `参考：`

* `自然语言处理-Natural language processing | NLP：`https://easyai.tech/ai-definition/nlp/

* `循环神经网络(RNN)模型与前向反向传播算法: `https://www.cnblogs.com/pinard/p/6509630.html


* `理解 Word2Vec 之 Skip-Gram 模型：`https://www.zhihu.com/people/gu-ao-78-6