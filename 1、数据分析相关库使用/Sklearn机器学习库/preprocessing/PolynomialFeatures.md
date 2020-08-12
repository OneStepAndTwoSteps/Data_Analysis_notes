 # PolynomialFeatures

`PolynomialFeatures` 用于创建 `多项式特征`

于是，我们使用 Scikit-Learning 的 PolynomialFeatures 类进行训练数据集的转换，让训练集中 每个特征的平方 （2 次多项式） 作为 新特征（在这种情况下，仅存在一个特征）

### `PolynomialFeatures` 这个类有 3 个参数：

* `degree`：控制多项式的次数；

* `interaction_only`：默认为 False，如果指定为 True，那么就不会有特征自己和自己结合的项，组合的特征中没有 a2 和 b2；

* `include_bias`：默认为 True 。如果为 True 的话，那么结果中就会有 0 次幂项，即全为 1 这一列。

### 参数详解：

* `interaction_only` 的意思是，得到的组合特征只有相乘的项，没有平方项。

* `interaction_only` 设置成 True 的意思是： 例如 [a,b] 的多项式交互式输出 [1,a,b,ab]。

* `include_bias` 设置 0 次幂那一列是否要。





