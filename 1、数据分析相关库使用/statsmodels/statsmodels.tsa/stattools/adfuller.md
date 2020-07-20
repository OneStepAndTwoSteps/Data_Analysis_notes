# adfuller

导入库：

    from statsmodels.tsa.stattools import adfuller

* ADF 检验了时间序列样本中存在单位根的零假设

### 时间序列分析之ADF检验

参考：

* https://blog.csdn.net/FrankieHello/article/details/86766625/

简略说明：

* 使用单位根检验，如果单位根存在，这个过程就是一个随机漫步（random walk）。

  简单点说，有单位根是不平稳的一种特殊情况。

  返回平稳的定义，一阶二阶矩不随时间改变就是宽平稳。有单位跟则二阶矩随时间改变而改变，所以不平稳。 其他情况比如有确定性趋势项之类的，也是不平稳，但是没有单位根，减掉趋势项就平稳了。
  
  具体操作的时候一定要注意是确定性趋势还是随机趋势（单位根），两者相差很大。





