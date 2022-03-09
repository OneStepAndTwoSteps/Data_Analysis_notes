# `word2vec`

## `Skip-gram 和 CBOW 模型`

* `CBOW：`输入是窗口大小，比如 `8` 个，输出 `V` 个，最终选择 `V` 个中 `softmax` 最大的那个值，`拿一个词语的上下文作为输入，来预测这个词语本身`。

* `Skip-Gram:` 输入是中心词 `1` 个，输出 `V` 个，最终选择 `V` 个中 `softmax` 最大的那个值，`用一个词语作为输入，来预测它周围的上下文`。


## `参考：`


`理解 Word2Vec 之 Skip-Gram 模型：`https://zhuanlan.zhihu.com/p/27234078

`白话Word2Vec：`https://www.jianshu.com/p/f58c08ae44a6

`word2vec原理(一) CBOW与Skip-Gram模型基础：`https://www.cnblogs.com/pinard/p/7160330.html
