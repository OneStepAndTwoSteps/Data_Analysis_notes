# MapReduce的map、shuffle、reduce操作


<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/MapReduce/1.png"/></div>

假设我们现在有3本书，我们现在想要统计三本书中每一个单词出现了多少次


*   __map操作__
    
    可以帮助我们记录，每一个单词在数中出现的次数，如果每一次单词出现就在后面记为1，



*   __shuffle操作__

    可以帮助我们将打标记的点进行一个统计，也就是统计我们单词出现的总次数。


*   __reduce操作__

    最后将所有数据进行一个整合，也就是我们三本书中每一个单词出现的次数


### 小结：

Map 是设计的关键，Map是分解动作，是将输入数据从数据表特征空间向最终空间的转换，且解空间应该是线性空间，具备可加性。

Reduce 是对中间的解空间元素(也就是Map的输出)进行归约合并的操作。
