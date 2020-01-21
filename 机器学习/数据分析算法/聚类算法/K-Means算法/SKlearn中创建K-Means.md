
### 在SKlearn中使用K-Means算法：

from sklearn.cluster import KMeans

### K-Means的一些重要参数:
KMeans(n_clusters=8, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=1, algorithm='auto')
  
__一、n_clusters:__ 即 K 值，表示分几类，一般需要多试一些 K 值来保证更好的聚类效果。你可以随机设置一些 K 值，然后选择聚类效果最好的作为最终的 K 值；

__二、max_iter：__ 最大迭代次数，如果聚类很难收敛的话，设置最大迭代次数可以让我们及时得到反馈结果，否则程序运行时间会非常长；

__三、n_init：__ 初始化中心点的运算次数，默认是 10。程序是否能快速收敛和中心点的选择关系非常大，所以在中心点选择上多花一些时间，来争取整体时间上的快速收敛还是非常值得的。由于每一次中心点都是随机生成的，这样得到的结果就有好有坏，非常不确定，所以要运行 n_init 次, 取其中最好的作为初始的中心点。如果 K 值比较大的时候，你可以适当增大 n_init 这个值；

__四、init：__ 即初始值选择的方式，默认是采用优化过的 k-means++ 方式，你也可以自己指定中心点，或者采用 random 完全随机的方式。自己设置中心点一般是对于个性化的数据进行设置，很少采用。random 的方式则是完全随机的方式，一般推荐采用优化过的 k-means++ 方式；

__五、algorithm：__ k-means 的实现算法，有“auto” “full”“elkan”三种。一般来说建议直接用默认的"auto"。简单说下这三个取值的区别，如果你选择"full"采用的是传统的 K-Means 算法，“auto”会根据数据的特点自动选择是选择“full”还是“elkan”。我们一般选择默认的取值，即“auto” 。

  
  
