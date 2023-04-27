### 交叉验证中的warning

*   1、标签中的数据不够分组：


    <div align=center><img width="500" height="400" src="https://raw.githubusercontent.com/OneStepAndTwoSteps/Data_Analysis_notes/master/static/sklearn%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%BA%93/model_selection/%E4%BA%A4%E5%8F%89%E9%AA%8C%E8%AF%81/1.jpg"/></div>


    这种问题的原因是你标签中 最少的那个标签数量 小于你要分组的数量 即标签 0 的个数小于 n_split的大小。