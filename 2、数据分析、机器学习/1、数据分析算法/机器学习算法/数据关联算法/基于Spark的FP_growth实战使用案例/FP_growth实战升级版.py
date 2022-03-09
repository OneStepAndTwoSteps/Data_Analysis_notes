#author py chen
import sys,os
import pandas as pd
# from pyspark import SparkConf
os.environ['SPARK_HOME'] = "D:/py包/spark-2.3.3-bin-hadoop2.7"
sys.path.append("D:/py包/spark-2.3.3-bin-hadoop2.7/python/lib/py4j-0.10.7-src.zip")
sys.path.append("D:/py包/spark-2.3.3-bin-hadoop2.7/bin")
sys.path.append("D:/py包/spark-2.3.3-bin-hadoop2.7/python")
sys.path.append("D:/py包/spark-2.3.3-bin-hadoop2.7/python/pyspark")
sys.path.append("D:/py包/spark-2.3.3-bin-hadoop2.7/python/lib")
sys.path.append("D:/py包/spark-2.3.3-bin-hadoop2.7/python/lib/pyspark.zip")
sys.path.append("C:/Program Files/Java/jdk1.8.0_60")
from pyspark.ml.fpm import FPGrowth
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import csv

spark = SparkSession.builder.appName("FrequentPatternMiningExample").getOrCreate()
file_path = '32-Python' + '/' + 'Python-语句结构.csv'
# file_path='61-java经典课程\Java经典课程-Java基础之入门.csv'



# 读取文件中的知识点，把他输出成列表
with open(file_path, 'r', encoding='utf-8') as data:
    new_data_list = []
    lists = csv.reader(data)
    for i in lists:
        if len(i) > 1:
            new_data_list.append(i)
    print(new_data_list)

    # 有效知识点的长度(非空)，因为下面制造df需要id和items一一对应
    data_len = len(new_data_list)

    # 制作id列表，用于下面构造df
    data_id = [i for i in range(data_len)]
    print(id)

dict = {'id': data_id, 'items': new_data_list}
print(dict)

# 构造df
new_python_data = pd.DataFrame(data=dict, columns=['id', 'items'])

# 将df转化成spark的df格式
df = spark.createDataFrame(new_python_data)
# 查看输出内容
df.collect()

# 实例化模型，并且传入分析的内容，支持度，置信度
fpGrowth = FPGrowth(itemsCol="items", minSupport=0.5, minConfidence=0.6)
# 模型荀雪莲
model = fpGrowth.fit(df)

#  下面这些步骤用于拼接计算结果的效果

df_freq = model.freqItemsets
df_ar = model.associationRules

total = data_len
df_supp = df_freq.withColumn("support", df_freq.freq/total)
df_supp_ar = df_ar.join(df_supp,df_supp.items==df_ar.consequent, 'left').drop('items')
df_lift = df_supp_ar.withColumn("lift", df_supp_ar.confidence/df_supp_ar.support)

df_freq_new = df_freq.withColumn('items', F.concat_ws(',', 'items'))
df_lift_new = df_lift.withColumn('antecedent', F.concat_ws(',', 'antecedent')).withColumn('consequent', F.concat_ws(',', 'consequent'))


# 可视化，如下图
df_lift_new.show()

'''
+----------+----------+------------------+----+------------------+------------------+
|antecedent|consequent|        confidence|freq|           support|              lift|
+----------+----------+------------------+----+------------------+------------------+
| 循环结构2| 分支结构1|0.7333333333333333|  17|0.7727272727272727|0.9490196078431372|
| 分支结构1| 循环结构2|0.6470588235294118|  15|0.6818181818181818|0.9490196078431373|
+----------+----------+------------------+----+------------------+------------------+
'''

# 查找单列数据，如只看antecedent这一列数据可以使用两个方法show()，collect()
df_lift_new.select('antecedent').show()

df_lift_new.select('antecedent').collect()


df_freq_new.show()

'''
+-----------+----+
|      items|freq|
+-----------+----+
|      分支结构1|  17|
|      循环结构2|  15|
|循环结构2,分支结构1|  11|
|      循环结构1|  15|
|      分支结构2|  11|
+-----------+----+
'''
