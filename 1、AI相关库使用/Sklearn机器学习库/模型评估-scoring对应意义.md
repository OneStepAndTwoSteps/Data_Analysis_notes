## 模型评估：量化预测的质量

有3种不同的API用于评估模型预测的质量：

1、__Estimator评分方法：__ Estimators有一种score方法可以为他们设计要解决的问题提供默认评估标准。本页未对此进行讨论，但在每个估算工具的文档中都有讨论。

2、__评分参数：__ 使用交叉验证（例如model_selection.cross_val_score和model_selection.GridSearchCV）的模型评估工具依赖于内部评分策略。这将在评分参数：定义模型评估规则一节中讨论。

3、__度量功能：__ 该metrics模块实现了针对特定目的评估预测误差的功能。这些指标详细介绍了分类指标，多标签排名指标，回归指标和群集指标。


#### scoring 分别采取的评分机制所对应的计算函数
-《[ The scoring parameter: defining model evaluation rules ](https://docs.w3cub.com/scikit_learn/modules/model_evaluation/#scoring-parameter)》
