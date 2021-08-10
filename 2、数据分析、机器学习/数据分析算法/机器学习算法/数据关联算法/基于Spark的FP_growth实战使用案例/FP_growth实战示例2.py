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

spark = SparkSession.builder.appName("FrequentPatternMiningExample").getOrCreate()
df = spark.createDataFrame([
    (0, [1, 2, 5]),
    (1, [1, 2, 3, 5]),
    (2, [1, 2])
], ["id", "items"])
print(df)

fpGrowth = FPGrowth(itemsCol="items", minSupport=0.5, minConfidence=0.6)
model = fpGrowth.fit(df)

# Display frequent itemsets.
model.freqItemsets.show()

# Display generated association rules.
model.associationRules.show()

# transform examines the input items against all the association rules and summarize the
# consequents as prediction
model.transform(df).show()


# 输出结果：

'''
+---------+----+
|    items|freq|
+---------+----+
|      [1]|   3|
|      [2]|   3|
|   [2, 1]|   3|
|      [5]|   2|
|   [5, 2]|   2|
|[5, 2, 1]|   2|
|   [5, 1]|   2|
+---------+----+

+----------+----------+------------------+
|antecedent|consequent|        confidence|
+----------+----------+------------------+
|    [5, 2]|       [1]|               1.0|
|       [2]|       [1]|               1.0|
|       [2]|       [5]|0.6666666666666666|
|    [2, 1]|       [5]|0.6666666666666666|
|       [5]|       [2]|               1.0|
|       [5]|       [1]|               1.0|
|    [5, 1]|       [2]|               1.0|
|       [1]|       [2]|               1.0|
|       [1]|       [5]|0.6666666666666666|
+----------+----------+------------------+

+---+------------+----------+
| id|       items|prediction|
+---+------------+----------+
|  0|   [1, 2, 5]|        []|
|  1|[1, 2, 3, 5]|        []|
|  2|      [1, 2]|       [5]|
+---+------------+----------+


'''
