#author py chen
import sys,os
# from pyspark import SparkConf

# 配置环境变量，这里因为是基于windows的环境，这里我们将需要的工具用环境变量导入
os.environ['SPARK_HOME'] = "D:/py包/spark-2.3.3-bin-hadoop2.7"
sys.path.append("D:/py包/spark-2.3.3-bin-hadoop2.7/python/lib/py4j-0.10.7-src.zip")
sys.path.append("D:/py包/spark-2.3.3-bin-hadoop2.7/bin")
sys.path.append("D:/py包/spark-2.3.3-bin-hadoop2.7/python")
sys.path.append("D:/py包/spark-2.3.3-bin-hadoop2.7/python/pyspark")
sys.path.append("D:/py包/spark-2.3.3-bin-hadoop2.7/python/lib")
sys.path.append("D:/py包/spark-2.3.3-bin-hadoop2.7/python/lib/pyspark.zip")
sys.path.append("C:/Program Files/Java/jdk1.8.0_60")

print(os.environ['SPARK_HOME'])
print(os.environ['PYTHONPATH'])

from pyspark import SparkContext
sc = SparkContext("local","testing")
print(sc)


from  pyspark.mllib.fpm import FPGrowth
data = [["A", "B", "C", "E", "F","O"], ["A", "C", "G"], ["E","I"], ["A", "C","D","E","G"], ["A", "C", "E","G","L"],
       ["E","J"],["A","B","C","E","F","P"],["A","C","D"],["A","C","E","G","M"],["A","C","E","G","N"]]

'''
sc.parallelize()

并行集合的一个重要参数是slices，表示数据集切分的份数。
Spark将会在集群上为每一份数据起一个任务。典型地，你可以在集群的每个CPU上分布2-4个slices.一般来说，Spark会尝试根据集群的状况，来自动设定slices的数目。
然而，你也可以通过传递给parallelize的第二个参数来进行手动设置。（例如：sc.parallelize(data,10)).
'''
# 将数据读取创建RDD对象，并且分割为2份
rdd = sc.parallelize(data, 2)

#支持度阈值为20%
# minSupport：最小支持度， numPartitions: 用于分发工作的分区数（并不会减少行数）而是切分数据。
model = FPGrowth.train(rdd, minSupport=0.2, numPartitions=2)

# 模型结果输出
print(sorted(model.freqItemsets().collect()))

# 输出结果：

'''
[FreqItemset(items=['A'], freq=8),
FreqItemset(items=['B'], freq=2), 
FreqItemset(items=['B', 'A'], freq=2),
FreqItemset(items=['B', 'C'], freq=2), 
FreqItemset(items=['B', 'C', 'A'], freq=2), 
FreqItemset(items=['B', 'E'], freq=2),
FreqItemset(items=['B', 'E', 'A'], freq=2),
FreqItemset(items=['B', 'E', 'C'], freq=2),
FreqItemset(items=['B', 'E', 'C', 'A'], freq=2),
FreqItemset(items=['C'], freq=8), 
FreqItemset(items=['C', 'A'], freq=8), 
FreqItemset(items=['D'], freq=2), 
FreqItemset(items=['D', 'A'], freq=2),
FreqItemset(items=['D', 'C'], freq=2),
FreqItemset(items=['D', 'C', 'A'], freq=2), 
FreqItemset(items=['E'], freq=8), 
FreqItemset(items=['E', 'A'], freq=6), 
FreqItemset(items=['E', 'C'], freq=6), 
FreqItemset(items=['E', 'C', 'A'], freq=6), 
FreqItemset(items=['F'], freq=2), 
FreqItemset(items=['F', 'A'], freq=2), 
FreqItemset(items=['F', 'B'], freq=2), 
FreqItemset(items=['F', 'B', 'A'], freq=2),
FreqItemset(items=['F', 'B', 'C'], freq=2),
FreqItemset(items=['F', 'B', 'C', 'A'], freq=2), 
FreqItemset(items=['F', 'B', 'E'], freq=2),
FreqItemset(items=['F', 'B', 'E', 'A'], freq=2),
FreqItemset(items=['F', 'B', 'E', 'C'], freq=2),
FreqItemset(items=['F', 'B', 'E', 'C', 'A'], freq=2),
FreqItemset(items=['F', 'C'], freq=2),
FreqItemset(items=['F', 'C', 'A'], freq=2), 
FreqItemset(items=['F', 'E'], freq=2), 
FreqItemset(items=['F', 'E', 'A'], freq=2), 
FreqItemset(items=['F', 'E', 'C'], freq=2), 
FreqItemset(items=['F', 'E', 'C', 'A'], freq=2),
FreqItemset(items=['G'], freq=5), 
FreqItemset(items=['G', 'A'], freq=5), 
FreqItemset(items=['G', 'C'], freq=5), 
FreqItemset(items=['G', 'C', 'A'], freq=5), 
FreqItemset(items=['G', 'E'], freq=4), 
FreqItemset(items=['G', 'E', 'A'], freq=4), 
FreqItemset(items=['G', 'E', 'C'], freq=4), 
FreqItemset(items=['G', 'E', 'C', 'A'], freq=4)]
'''