## 数据描述


您将获得每日历史销售数据。任务是预测测试集中每个商店的销售产品总量。请注意，商店和产品列表每个月都会略有变化。创建可以处理此类情况的强大模型是挑战的一部分。

### 文件说明

sales_train.csv - 训练集。2013年1月至2015年10月的每日历史数据。

test.csv - 测试集。您需要预测2015年11月这些商店和产品的销售额。

sample_submission.csv - 格式正确的示例提交文件。

items.csv - 有关商品/产品的补充信息。

item_categories.csv   - 有关项目类别的补充信息。

shops.csv - 有关商店的补充信息。


### 数据字段

ID  - 表示测试集中的（Shop，Item）元组的Id

shop_id - 商店的唯一标识符

item_id - 产品的唯一标识符

item_category_id - 项目类别的唯一标识符

item_cnt_day - 销售的产品数量。您正在预测此度量的每月金额

item_price - 商品的当前价格

日期  - 日期格式为dd / mm / yyyy

date_block_num - 一个连续的月号，用于方便。2013年1月是0，2013年2月是1，...，2015年10月是33

item_name  - 项目名称

shop_name - 商店名称

item_category_name - 项目类别的名称



