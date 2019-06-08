## ARMA模型工具

### ARMA模型包
from statsmodels.tsa.arima_model import ARMA

### ARMA类 
ARMA(endog,order,exog=None)创建ARMA类

endog：英文是 endogenous variable，代表内生变量，又叫非政策性变量，它是由模型决定的，不被政策左右，可以说是我们想要分析的变量，或者说是我们这次项目中需要用到的变量。

order：代表是 p 和 q 的值，也就是 ARMA 中的阶数。

exog：英文是 exogenous variables，代表外生变量。外生变量和内生变量一样是经济模型中的两个重要变量。相对于内生变量而言，外生变量又称作为政策性变量，在经济机制内受外部因素的影响，不是我们模型要研究的变量。

__举例说明：__

如果我们想要创建 ARMA(7,0) 模型，可以写成：ARMA(data,(7,0))，其中 data 是我们想要观察的变量，(7,0) 代表 (p,q) 的阶数。
