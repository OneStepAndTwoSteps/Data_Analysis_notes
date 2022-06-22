# `LSTM 长短期记忆`

## `一、RNN -> LSTM：` 

* `RNN` 容易产生梯度消失或梯度爆炸，核心问题就是 `RNN` 在不同时间步使用共享参数 $W$，导致 $t+n$ 时刻的损失对时刻的参数的偏导数存在 $W$ 的指数形式，一旦 $W$ 很小或很大就会导致梯度消失或梯度爆炸的问题。下图形象的显示了梯度消失的问题，即梯度不断反传，梯度不断变小（箭头不断变小）。

    <div align=center><img height =350 src="./static/1.jpg"/></div>

    在 `RNN` 中，由于梯度消失问题，长距离以前的状态对当前时刻的影响很小，所以导致无法建模长距离依赖关系，所以出现了 `LSTM` 。


* `LSTM` 相比于 `RNN`  的几点改进：

    * `RNN` 的特性使得自身具有长距离依赖，随着序列的增长，使得更早的输入信息重要性会弱于晚输入的信息，并且容易出现梯度消失和梯度爆炸等情况：
    
    </br>
    
    <div align=center><img height =150 src="./static/RNN shortcoming.jpg"/></div>

    </br>
    

    * `LSTM` 通过引入门机制来有效的抑制了梯度消失和梯度爆炸，并且根据门的特性，相比于 `RNN` ，可以使得 `LSTM` 忘记不重要的信息，记住关键信息：
  
    </br>

    <div align=center><img height =200 src="./static/LSTM 1.jpg"/></div>




## `二、LSTM：`

基础的 `LSTM` 共有三个门控机制，分别是 `遗忘门`、`输入门`、和`输出门`：

* `遗忘门：`这个门决定了应该丢弃或保留哪些信息，将来自上一层隐藏状态的信息 $h^{(t-1)}$  和当前输入的信息 $x^{(t)}$  输入到 `sigmoid` 函数中，把值压缩到 `0` 到 `1` 之间，如果值接近 `0` ，那么意味着忘记，如果值接近 `1` ，那么意味着保留。

    <div align=center><img height =200 src="./static/forget gate.gif"/></div>

    <div align=center><img height =40 src="./static/forget gate2.jpg"/></div>


* `输入门：` 为细胞的更新服务，首先将先前的隐藏状态 $h^{(t-1)}$  和当前的输入 $x^{(t)}$  输入到 `sigmoid` 函数中，通过最后的 `0 1` 结果，来决定哪一些值是需要被更新，如果值为 `0` ，表示这些值是不重要的，如果是 `1` 意味着重要。 紧接着将 先前的隐藏状态 $h^{(t-1)}$  和当前的输入 $x^{(t)}$  输入到 `tanh` 函数中，将值压缩到 `-1` 到 `1` 之间去规范网络。

    在细胞更新中需要将输入门中得到的 `sigmoid output` 和 `tanh output` 做一个相乘，`sigmoid` 的输出决定了哪一些消息在经过 `tanh` 输出后是重要的。

    <div align=center><img height =200 src="./static/input gate.gif"/></div>

    <div align=center><img height =80 src="./static/input gate2.jpg"/></div>


* `细胞更新：` 进入如下的公式运算，遗忘门  $f^{(t)}$   控制上一个时刻的内部状态   $C^{(t-1)}$   需要遗忘多少信息,输入门  $i^{(t)}$   控制当前时刻的候选状态  $\tilde{C}^{(t-1)}$   有多少信息需要保存。


    <div align=center><img height =200 src="./static/cell state update.gif"/></div>

    <div align=center><img height =40 src="./static/cell state update2.jpg"/></div>


* `输出门：` 输出门决定下一个隐藏状态应该是什么。请记住，隐藏状态包含有关先前输入的信息。隐藏状态也用于预测。首先，我们将之前的隐藏状态和当前输入传递给一个 `sigmoid` 函数。然后我们将新修改的单元状态传递给 `tanh` 函数。我们将 `tanh` 输出与 `sigmoid` 输出相乘来决定隐藏状态应该携带什么信息。输出是隐藏状态。然后将新的单元状态和新的隐藏状态转移到下一个时间步。

    <div align=center><img height =200 src="./static/output gate.gif"/></div>

    <div align=center><img height =80 src="./static/output gate2.jpg"/></div>

## `三、关于 LSTM 解决减轻梯度爆炸和梯度消失问题的两个点`：

* `1、使用更复杂的循环函数：`复杂的循环函数使得梯度在回传的过程中经过更多导数较小的激活函数，从而降低了梯度爆炸发生的可能性。

 * `2、遗忘门的使用：`遗忘门中的偏置项 $b^{(f)}$ 通过在初始化的过程中会设置的比较大，从而使 $f^{(t)}$ 接近于 1 ，即单元新状态 $C^{(t)}$ 将尽量保存 $C^{(t-1)}$ 中的信息，因此在训练时，即使其他的回传路径仍然面临着梯度消失的风险， $C^{(t)}$ 上的梯度还是可以通过 $C^{(t-1)}$ 一直回传，不宜消失，但是在训练过程中 $f^{(t)}$ 的值可能会逐渐减小，通过遗忘门的梯度也会逐渐消失，所以遗忘门只能在一定程度上减轻梯度消失的问题，并非完全解决。

尽管从理论上看去掉遗忘门可以完全避免梯度消失的问题，但是有遗忘门的 LSTM 的神经网络实际效果往往更好。

## `参考：`

* `RNN vs LSTM vs GRU -- 该选哪个？：`https://www.zhihu.com/search?q=gru%20lstm&utm_content=search_suggestion&type=content

* `LSTM模型与前向反向传播算法：`https://www.cnblogs.com/pinard/p/6519110.html


* `CS224N（1.29）Vanishing Gradients, Fancy RNNs：`http://bitjoy.net/2019/08/01/cs224n%ef%bc%881-29%ef%bc%89vanishing-gradients-fancy-rnns/


* `Illustrated Guide to LSTM’s and GRU’s: A step by step explanation：`https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21