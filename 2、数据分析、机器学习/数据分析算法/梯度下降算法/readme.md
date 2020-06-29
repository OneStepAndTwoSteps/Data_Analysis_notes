## 批量梯度下降，随机梯度下降，mini-batch随机梯度下降对比说明：

### 大规模数据集

<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/%E5%A4%A7%E8%A7%84%E6%A8%A1%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/1-.png"/></div>

我们已经知晓一种高性能的机器学习的途径，使用低偏差的算法进行大规模的数据训练，我们之前说过的对易混淆单词进行分类的例子，比如 for breakfast I  ate two age，在这个例子中我们可以看出，只要你用大量的数据训练算法，他的效果将看起来非常好，从类似的结果中可以看出来，在机器学习中，通常情况下决定因素往往不是最好的算法，而是谁的训练数据最多，如果你想要进行大规模的数据训练，至少我们需要大规模的数据集。


### 学习大规模数据集
<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/%E5%A4%A7%E8%A7%84%E6%A8%A1%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/2.png"/></div>

大数据集有其自己的特点，具体来说是计算问题，假定你的训练集的大小为m=100000000，对现代很多数据集而言，这个数据量是很实际的，如果你看美国人口普查表，美国有三亿个人口，你可以轻松得到数亿条记录，亦或者是流量网站，我们可以获取流量数据，假设你想要训练一个线性回归或者逻辑回归模型，这个时候我们用到梯度下降，同时我们观察需要梯度下降的项(红色框框起来的地方)，但是如果我们使用梯度下降算法优化我们的θ，此时的m太大了，我们付出的优化代价也非常大，所以我们现在需要一种方法来帮助我们解决这样的问题，接下来我所讲的内容会帮助我们解决这样的问题。

当然我们在使用我们的一亿个样本进行训练时，我们应该询问自己，为什么不使用1000个样本进行训练，我们可以在一亿个样本中随机提取出一千个样本来进行训练。所以我们在进行预训练之前我们一个检查我们的样本，是否可以使用更小的数据集代替大量数据将进行训练(这次训练出来的效果也是相同)

在高方差学习算法中，我们可以判断出增加我们的训练集可以减少我们的error量，可以提高算法模型的效果，单如果是右边这种高偏差的学习算法的话，我们基本可以看出我们选择训练数据集数量为1000时训练出来的效果和训练数据集为1亿时效果是差不多的，所以我们可以用更少的数据集代替大的数据集。而不需要付出很大的代价。

接下来我们针对大规模数据集中的优化算法方法和高效的计算方法进行讲解，一个为随机梯度下降，一个为减少映射用来处理海量数据


### 随机梯度下降
我们之前在使用线性回归、逻辑回归、神经网络中进行计算我们的代价函数和优化目标时我们会用到我们的 __梯度下降算法，但是对于大规模的数据集梯度下降算法需要优化迭代的次数太多，代价太大，__ 接下来我们会将随机梯度下降算法，其是对于普通梯度下降的一个优化。

<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/%E5%A4%A7%E8%A7%84%E6%A8%A1%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/3.png"/></div>

我们现在回顾一下我们的线性回归和梯度下降，第一个是式子是假设函数，第二个式子是代价函数，第三个式子是梯度下降，右边的图是我们通过改变我们的θ参数，从而减小我们的代价函数的图。

<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/%E5%A4%A7%E8%A7%84%E6%A8%A1%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/4+5.png"/></div>

右侧图就是我们的梯度下降的过程，他会通过我们红色标点的轨迹找到我们的全局最小值，下载有一个问题，当我们的m很大时我们的微分项(红框)计算量会变得非常大，以美国人口普查为例，当我们的m=3亿时，我们需要将3亿条数据进行求和(这还仅仅只是计算出一次微分项)，这种梯度下降的算法有另外一个名字(批量梯度下降算法)，因为我们的数据量非常大，我们将我们的数据存储在硬盘上，我们进行计算时，我们不能一次性的进行计算(因为计算机的内存容纳不下这些数据)，所以我们会一次先传一部分的数据进去进行求和，直到3亿条数据全部传完然后计算出我们的微分项，求和完成之后我们再进行我们的梯度下降，这次训练完成之后我们只是计算了梯度下降中的一步(一个红色的叉叉)，然后我们需要再按照上面的方法进行微分项的求和，然后再进行梯度下降，一直迭代到找到全局最优值。

接下来我们会讨论一种算法，我们不需要再传入所有的数据， __只用传一个训练样本即可，就是我们的随机梯度下降。__

PS: __随机梯度下降,一次参数优化只学习一个样本。__

### 批量梯度下降和随机梯度下降对比


<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/%E5%A4%A7%E8%A7%84%E6%A8%A1%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/6+7.png"/></div>

第一个式子是代价函数，第二个式子是优化过程，在红色框框起来这个部分就是我们的优化目标(代价函数J_train(θ)，关于θj的偏微分)

接下来我们看随机梯度下降算法，为了可以更好的描述随机梯度下降算法，这里我们用另外一种方式将代价函数写出来，我们将代价函数定义为(绿色框部分)，其等于1/2的假设函数与真实值的平方误差，因此此代价函数实际上衡量的是我的假设函数，在某个样本(x(i),y(i))上的表现，你可以已经发现左侧的总体代价函数J_train可以写成右侧的形式，所以J_train就等于假设函数在m个训练样本中每一个样本(x(i),y(i))上的代价函数的平均值 

接下来我们看随机荼毒下降的优化过程，第一步首先我们要随机打乱我们的数据，这是防止打乱之前数据之间存在关联，同时可以使我们的收敛更快。接着我们看 __随机梯度下降的优化过程__ ，我们可以看到随机梯度下降的微分项(黄色框)和我们的批量梯度下降不同，我们可以看出随机梯度下降已经不用在对我们所有的数据集进行求和了， __他计算的是单个样本的梯度项 ，其内部的操作为：我们先将代价函数进行梯度下降，首先我们只关注我们的第一个样本，此时我们修改我们的参数使得我们的第一个样本可以拟合的更好一些，然后得到我们对第一个样本进行优化后的θ参数，然后我对我们的参数进行修改，使得我们第二个样本拟合的更好，同理依次进行θ参数的优化。最后得到我们的全局最小值。__

__对于随机梯度下降来讲，我们我们每次只要关注一个训练样本，而在这个过程中我们已经开始一点一点把参数，朝着全局最小值的方向进行修改了__


<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/%E5%A4%A7%E8%A7%84%E6%A8%A1%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/8.png"/></div>


__批量梯度下降和随机梯度下降的对比：__ 随机梯度下降的收敛速度更快，使用随机梯度下降在训练时，我们进行梯度下降的方向可能有误，但是可以通过下一次的样本训练进行一个修改，通过随机迂回的路线向全局最小值进行进发，随机梯度下降和批量梯度下降的收敛形式也不同，随机梯度下降会在一个区域(如我们圈起来的地方)中朝着全局最小值的方向徘徊，使得最后的结果非常接近全局最小值，我们就可以得到一个很好的假设，因此常用我们的梯度下降法，能得到一个很接近全局最小值的参数。

通常外面的Repeat这个外层循环，循环的次数通常看数据集的大小，当数据集很大的时候通常只循环一次，循环次数由1-10之间为正常循环次数。


### Mini-Batch 梯度下降
__Mini-Batch 梯度下降算法是介于批量梯度下降算法和随机梯度下降算法之间的算法，每计算常数𝑏次训练实例，便更新一次参数 𝜃 。__

在批量梯度下降算法中每次迭代我们都要使用到所有的m个样本，在随机梯度下降中我们每次迭代只需要一个样本。Mini-batch算法具体来说就是每次迭代，会使用b个样本，这个b我们称为mini-batch大小的参数，b的常用取值为2-100。

在批量梯度下降算法中每次迭代我们都要使用到所有的m个样本，在随机梯度下降中我们每次迭代只需要一个样本，Mini-batch算法具体来说就是每次迭代，会使用b个样本，这个b我们称为mini-batch大小的参数，b的常用取值为2-100


<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/%E5%A4%A7%E8%A7%84%E6%A8%A1%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/9.png"/></div>

这里我们的数据量为m=1000，mini-batch为10，我们以10为一个batch，进行一次内部循环 。

使用mini-batch梯度下降算法的优势在于下降的速度更快，以美国人口普查数据而言，b取10，和批量梯度下降相比，不需要一次性加载3亿条数据，而是一次使用10条数据进行参数的更新，和随机梯度下降相比，而不再一次使用一个样本进行参数更新而是10个，增加了并行计算.

mini-batch算法的一个缺点之一在于，可能需要确定b的大小，不过如果你有一个优秀的向量化方法，有时可以比随机梯度下降运行更快


### 随机梯度下降收敛

现在我们已经知道了随机梯度下降算法，那我们如何保障调试的过程已经结束，并且已经收敛到了合适的位置呢？还有如何调整我们随机梯度下降的学习率α呢？
	
接下来我们会讨论一种算法，确保我们的随机梯度下降可以收敛，以及选择一个合适的学习率α

<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/%E5%A4%A7%E8%A7%84%E6%A8%A1%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/10.png"/></div>


之前我们讲到判断梯度下降已经收敛的标准是我们的代价函数，我们确保我们每一次我们的代价函数的迭代中都是下降的，当训练集小的时候，计算比较容易，但是在大规模的训练集的情况下，这是不现实的，因为计算代价太大了，因为我们需要计算我们（红色框部分）的均方差。

在随机梯度下降中，我们通过单个样本进行更新参数，为了检查我们的随机梯度下降是否收敛，我们需要每1000次迭代就画出前一步中我们计算出的cost函数，我们把前1000个样本的cost函数的平均值画出来，他会有效的帮助你估计出你的算法在前1000个样本上表现有多好

比起之前的J_train我们需要对所有样本进行遍历来说随机梯度下降的这个步骤只用在更新θ之前计算这些cost函数，并不需要太大的计算量。

__接下来看一下随机梯度下降的收敛图，我们对其进行分析,并给出解决方案。__


<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/%E5%A4%A7%E8%A7%84%E6%A8%A1%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/11.png"/></div>

__第一幅图:__ 这里我们画出前一千个样本的cost函数(蓝线)，因为他们是前一千个样本的平均值，因此开起来会有很多噪声，它可能不是每一步迭代都在下降，假如你得到了像第一幅图的图像，这是一个很好的下降过程，因为你可以看出来代价函数的值在下降，然后通过一个点之后我们的下降速度变得缓慢，通过这个图我们可以判断我们的算法已经收敛了，如果我们降低我们的学习率(红线)，我们会得到一个下降的更缓慢的曲线，他可能使得我们的算法收敛到一个更好的结果，我们可以看出他并不会直接收敛到全局最小值，而是在一个范围内反复震荡，最后逐渐接近全局最小值，如果用一个更小的学习率，最后这种震荡就会更小，不过我们经常会忽略这两条线带来的结果差别，但是使用小的学习率有时候确实可以帮助我们得到更好的参数值。

__第二幅图:__ 出现第二幅图的情况，当我们使用1000个样本进行训练的我们得到蓝色的曲线，当我们使用5000个样本进行训练的时候，我们得到的曲线会更加平滑(红线)，使用大数据集可以帮助我们获得更平滑的曲线，但是缺点在于增加了我们的计算量。

__第三幅图:__ 出现第三幅图的情况，好像你的算法并没有在收敛，因为整体的曲线看起来是平的，代价函数的值好像没有下降，但是如果你增加你的求代价函数均值的训练样本数量，我们可能就会得到一条像红色曲线的平滑曲线，通过红色区县我们可以看出我们的算法其实是有在收敛的，只不过我们求均值的样本太少了，导致包含了太多的噪声，导致我们看不出其实是在收敛的，当然如果我们增大我们的数据集也可能得到像紫色曲线一样的线段，此时很不幸我们的算法没有在收敛，此时我们可能就需要调整我们的学习率或者调整特征或者其他东西。

__第四幅图:__ 如果你得到的是第四幅图的情况，表示你需要使用更小的学习率进行学习

<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/%E5%A4%A7%E8%A7%84%E6%A8%A1%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/12.png"/></div>


我们知道 __随机梯度下降不会直接帮助我们收敛到全局最小值，而是在一个全局最小值的范围反复的迭代。__ 在大多数随机梯度下降的算法中，我们的学习率α是一个不变的常数，所以我们才得到了这样的情况，如果你想要让随机梯度下降更好的收敛到全局最小值，你需要做的是让学习率α随着时间逐渐变小，有一种方法是设置α为常数1，然后除以迭代次数加上某个常数2，迭代次数就是你运行随机梯度下降d额迭代次数，其实就是你已经计算过的训练样本的数量，而常数1和常数2是算法de 两个额外参数，同样需要选择合适的值，才能有更好的表现。


但是很多人不使用这样的方法，因为你需要去不断的定义你的常数1和常数2，需要你有很好的经验支持，但是不得不说的是这样确实可以给我们带来更好的算法的收敛(更接近最小值)，通过减小我们的学习率我们确实可以使得最后接近我们的全局最小值的时候我们的震荡会更小，直到收敛到非常靠近全局最小值d额地方，

### 使用 python 进行梯度下降


<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/%E5%A4%A7%E8%A7%84%E6%A8%A1%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/13.png"/></div>


#### 批量梯度下降：


    eta = 0.1 # 学习率
    n_iterations = 1000
    m = 100

    theta = np.random.rand(2,1) # 随机初始化值

    for iteration in n_iterations:
        gradients = 2/m * X_b.T.dot(X_b.dot(theta)-y)
        theta = theta - eta * gradients

特点：数据量大时十分占用空间，训练速度慢。


#### 使用 tensorflow 进行批量梯度下降：


    housing = fetch_california_housing()
    m,n = housing.data.shape
    # np.c_按colunm来组合array
    housing_data_plus_bias = np.c_[np.ones((m,1)),housing.data]
    scaler_housing_data_plus_bias = scaler.fit_transform(housing_data_plus_bias)

    n_epochs = 1000
    learning_rate = 0.1

    X = tf.constant(scaler_housing_data_plus_bias,dtype=tf.float32,name='X')
    Y = tf.constant(housing.target.reshape(-1,1),dtype=tf.float32,name='Y')

    theta = tf.Variable(tf.random_uniform([n+1,1],-1.0,1.0),name='theta')
    y_pred = tf.matmul(X,theta,name='predictions')

    error = y_pred - y
    mse = tf.reduce_mean(tf.square(error),name='mse')

    gradients = 2/m * tf.matmul(tf.transpose(X),error)    # 梯度向量
    training_op = tf.assign(theta,theta - learning_rate * gradients)

    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        init.run()
        for epoch in range(n_epochs):
            if epoch%100 == 0:
                print("Epoch: ",epoch,"MSE: ",mse.eval())
                sess.run(training_op)
        best_theta = theta.eval()





#### 随机梯度下降：


    n_epochs = 50
    t0,t1 = 5,50

    def learning_shedule(t):
        return t0/(t+t1)

    theta = np.random.rand(2,1)
    for epoch in  range(n_epochs):
        for i in range(m):
            random_index = np.random.randint(m) # 随机取数据
            xi = X_b[random_index:random_index+1]
            yi = y[random_index:random_index+1]

            gradients = 2/m *	xi.T.dot(xi.dot(theta)-yi)	

            # eta：刚开始学习率较大，之后逐渐降低学习率，寻找最小值
            eta	= learning_schedule(epoch	* m + i)    

            theta = theta - eta * gradients

特点：适用于大规模数据集，但是无法得到最优值。


#### 小批量随机梯度下降：

写法：就是将随机梯度下降中每次只迭代一个值改成迭代随机的一段训练集。


### 梯度下降过程和推导

*   https://www.cnblogs.com/solong1989/p/9900867.html 梯度下降算法过程详细解读

*   https://blog.csdn.net/qq_41800366/article/details/86583789 梯度下降算法原理讲解——机器学习


### 总结：

这里我们介绍了一种方法，近似地监测出随机梯度下降算法在最优化代价函数中的表现，这种方法不需要定时地扫描整个训练集，来算出整个样本集的代价函数，而是只需要每次对最后 1000 个，或者多少个样本，求一下平均值。

应用这种方法，你既可以保证随机梯度下降法正在正常运转和收敛，也可以用它来调整学习速率𝛼的大小。














