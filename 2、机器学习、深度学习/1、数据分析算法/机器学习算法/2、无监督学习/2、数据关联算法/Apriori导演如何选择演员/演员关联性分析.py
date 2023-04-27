#author py chen
from efficient_apriori import apriori
import csv

director="成龙"
data=open('导演'+ director +'.csv','r',encoding='utf-8')
lists=csv.reader(data)
# print(data.read())

data_lists=[]
for names in lists:
    # print(names)
    actor_list=[]
    for name in names:
        # 去掉数据中的空格
        new_name=name.strip()
        actor_list.append(new_name)
    # 取出名字
    data_lists.append(actor_list[1:])
data.close()

print(data_lists)

##  挖掘频繁项集和关联规则 ## 设置最小支持度和最小置信度参数
itemsets,rules = apriori(data_lists,min_support=0.1,min_confidence=0.8)
print(itemsets)
print(rules)

# {1: {('元彪',): 3, ('卢惠光',): 3, ('夏野萨博',): 4, ('张曼玉',): 3, ('董骠',): 3, ('詹姆士·谢',): 4}, 2: {('夏野萨博', '詹姆士·谢'): 4}}
# [{詹姆士·谢} -> {夏野萨博}, {夏野萨博} -> {詹姆士·谢}]
