# 回归算法

## 回归模型的集成

回归模型的集成相对简单，可以直接通过 `将各个模型的预测结果按照一定比例进行组合` 即可。

如：

现在建立了两种模型分别是：`GradientBoostingRegressor` 和 `RandomForestRegressor`，他们预测的结果为 `pred1` 和 `pred2`, 现在取 `pred = 0.7 * pred1 + 0.3 * pred2 `，最后的 pred 就是集成后的结果。



