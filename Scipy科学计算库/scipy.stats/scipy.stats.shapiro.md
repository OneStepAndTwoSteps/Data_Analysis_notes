### 夏皮罗-威尔克（Shapiro-Wilk）检验法

夏皮罗-威尔克检验是一种在频率上统计检验中检验正态性的方法。

#### scipy.stats.shapiro(x,a=None,reta=False)  

shapiro是用来专门做正态性检验的模块，适用于3 < 样本数< 5000 时的正态性检验。shapiro不合适做样本数 > 5000的正态性检验，检验结果的P值可能不准确 (这时候比如我们可以使用QQ图来替代)

x为待检验数据，一般只使用x就行


#### return
    
    w值，p值

p值表示这个数据群是正态分布的概率(只是假设，并不是确定一定具备正态分布)


#### 案例

    >>> from scipy import stats
    >>> np.random.seed(12345678)
    >>> x = stats.norm.rvs(loc=5, scale=3, size=100)
    >>> stats.shapiro(x)

    (0.9772805571556091, 0.08144091814756393)


