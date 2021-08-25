# `N-Gram 模型`

`N-gram` 相当于计算条件概率，如当出现这些词之后，下一个出现xx词的概率是多少，通过计算条件概率，选取最可能出现的词。

## `举个例子:`

* 假设完整的句子是 `as the proctor started the clock, the students opened their`，需要预测下一个词的概率分布。对于 `4-gram` 方法，则只有 `students opened their` 对下一个词有影响，前面的词都没有影响。

    然后我们统计训练集语料库中发现，分母 `students opened their` 出现`1000` 次，其后接 `books` 即 `students opened their books` 出现了 `400` 次，所以 `P(books|students opened their)=400/1000=0.4` 。类似的，下一个词为 `exams` 他在文中 `students opened their exams` 出现了 `100` 次，可以算出下一个词为 `exams` 的概率是 `0.1`。所以 `4-gram` 方法认为下一个词是 `books` 的概率更大。

    需要提醒的是，`n-gram` 方法在统计语料库中的 `n-gram` 时，对词的顺序是有要求的，即必须要和给定的 `n-gram` 的顺序一样才能对频数加 `1` ，比如这个例子中只有出现和 `students opened their` 顺序一样才行，如果是 `their students opened` 则不行。

    这很好理解，词的顺序不一样，含义都变了，肯定不行。



## `n-gram方法的不足：` 

* 考虑的状态有限。n-gram只能看到前n-1个词，无法建模长距离依赖关系，上面就是一个很好的例子。

* 稀疏性问题。对于一个稀有的（不常见的）w，如果他的词组没有在语料库中出现，则分子为0，但w很有可能是正确的，概率至少不能是0啊。比如students opened their petri dishes，对于学生物的学生来说是有可能的，但如果students opened their petri dishes没有在语料库中出现的话，petri dishes的概率就被预测为0了，这是不合理的。当然这个问题可以通过对词典中所有可能的词组频率+1平滑来部分解决。

* 更严重的稀疏性问题是，如果分母的词组频率在语料库中是0，那么所有w对应的分子的词组频率就更是0了，根本就没法计算概率。这种情况只能使用back-off策略，即如果4-gram太过于稀疏了，则降到3-gram，分母只统计opened their的频率。一般的，虽然n-gram中的n越大，语言模型预测越准确，但其稀疏性越严重，这是肯定的啦。n其实就相当于维度，我们知道在空间中，维度越高越稀疏，高维空间非常稀疏。对于n-gram，一般取n<=5。

* 存储问题，需要存储所有n-gram的频率，如果n越大，这种n-gram的组合越多，所以存储空间呈幂次上升。


## `参考：`

* `自然语言处理中N-Gram模型介绍：`https://zhuanlan.zhihu.com/p/32829048


* ` CS224N（1.24）Language Models and RNNs：`http://bitjoy.net/2019/07/31/cs224n%ef%bc%881-24%ef%bc%89language-models-and-rnns/