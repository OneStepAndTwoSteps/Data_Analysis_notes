# sklearn模块
         


## 从文本中提取特征信息    CountVectorizer类和TfidfVectorizer类 
  
同时说明 __sklearn中的fit，transform，fit_transform 在文本提取特征中各自的作用。__  这里注意是对于 __文本__ 。

首先，计算机是不能从文本字符串中发现规律。只有将字符串编码为计算机可以理解的数字，计算机才有可能发现文本中的规律。

对文本编码，就是让词语与数字对应起来，建立基于给定文本的词典。（fit方法 ）

再根据词典对所有的文本数据进行转码。（transform方法）

scikit库的CountVectorize类就是这种思路。

     from sklearn.feature_extraction.text import CountVectorizer

     cv = CountVectorizer()

__使用fit方法，CountVectorizer()类的会从corpus语料中学习到所有词语，进而构建出text词典。__

    text=["Hey hey hey lets go get lunch today :)",
           "Did you go home?",
           "Hey!!! I need a favor"]
    
    text相当于三篇文章

 __fit学会语料中的所有词语，构建词典__
 
    cv.fit(text)
    CountVectorizer(analyzer='word', binary=False, decode_error='strict',
            dtype=<class 'numpy.int64'>, encoding='utf-8', input='content',
            lowercase=True, max_df=1.0, max_features=None, min_df=1,
            ngram_range=(1, 1), preprocessor=None, stop_words=None,
            strip_accents=None, token_pattern='(?u)\\b\\w\\w+\\b',
            tokenizer=None, vocabulary=None)
            
  __这里我们查看下“词典”，也就是特征集(11个特征词)__
  
    cv.get_feature_names()
    
   Out:
   
      ['did',
       'favor',
       'get',
       'go',
       'hey',
       'home',
       'lets',
       'lunch',
       'need',
       'today',
       'you']
       
  __注意feature_name的返回结果，我们可以发现这几条规律：__
    
    一、所有的单词都是小写

    二、单词长度小于两个字母的，会被剔除掉

    三、标点符号会剔除掉

    四、不重复

    五、这个特征集是有顺序的     
       
  文档-词频矩阵（document-term matrix），英文简写为dtm
   
    dtm=cv.transform(texts)
    print(dtm)
    
  Out:
      (0, 2)	1
      (0, 3)	1
      (0, 4)	3
      (0, 6)	1
      (0, 7)	1
      (0, 9)	1
      (1, 0)	1
      (1, 3)	1
      (1, 5)	1
      (1, 10)	1
      (2, 1)	1
      (2, 4)	1
      (2, 8)	1
    
  用pandas库以行列形式展示-  在 jupyer notebook中展示的没有加print：
  
    pd.DataFrame(cv_fit.toarray(),columns=cv.get_feature_names())
  
对应输出的pandas图片，和上面的out(输出)结合来看，就是第0行第3个数为1次，第0行第4个数为1次......
![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/sklearn%E6%96%87%E6%9C%AC%E6%8F%90%E5%8F%96%E7%89%B9%E5%BE%81%E5%80%BC/1.jpg)

同时在我们pandas显示出来的图片中每一行代表一个文章，每一列代表一个特征，在第0行的hey特征下面的数字为3，表示hey在该文章里面出现了3次。


## 注意: 
   此时我们已经构建完成了我们的词频矩阵，如果我们还想加入新的文档此时我们需要注意了。
   
   举个例子：
         
         new_document = ['Hello girl lets go get a drink tonight']
         new_dtm = cv.transform(new_document)
         print(new_dtm.toarray())
         pd.DataFrame(new_dtm.toarray(), columns=cv.get_feature_names())
         
   Out: new_dtm.toarray()的输出
   
         [[0 0 1 1 0 0 1 0 0 0 0]]
         
显示如下图：
![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/sklearn%E6%96%87%E6%9C%AC%E6%8F%90%E5%8F%96%E7%89%B9%E5%BE%81%E5%80%BC/2.jpg)

__小结：__

即使new_document含有8个单词，但是在上面的dataframe表中只有3个特征词被有效编码，Hello,girl,drink和tonight词未被表征。这是因为我们初识的text语料所构建的词典并未含有这些词。但是对文本进行特征表征时，使用的确实text所生产的词典。

我们机器学习所用的数据，一般被分成训练集和测试集。训练集是为了让机器学习数据的规律（拟合模型），测试集是为了验证规律的有效性。训练集本质上代表的是过去及现在已知的数据，测试集本质上代表的是未来的未知数据（现在不存在的数据），我们是用已知的数据预测未来。

__所以我们只能让fit方法操作于训练集，构建基于过去或已知数据的特征集。__



## CountVectorizer和TfidfVectorizer方法的不同

__CountVectorizer__ 和 __TfidfVectorizer__ 是 __文本特征提取__ 的两种方法。两者的主要区别在于，CountVectorizer仅仅通过计算词语词频，没有考虑该词语是否有代表性。而TfidfVectorizer可以更加精准的表征一个词语对某个话题的代表性。










## GridSearchCV 交叉熵
from sklearn.grid_search import GridSearchCV 

GridSearchCV中的cv：表示将训练集划分为几份，用于交叉验证。

### 交叉验证例子：

  以决策树为例，当我们确定了要使用决策树算法的时候，为了能够更好地拟合和预测，我们需要调整它的参数。在决策树算法中，我们通常选择的参数是决策树的最大深度。

  于是我们会给出一系列的最大深度的值，比如 {'max_depth': [1,2,3,4,5,6,7]}，我们会尽可能包含最优最大深度。

  __不过，我们如何知道哪一个最大深度的模型是最好的呢？我们需要一种可靠的评分方法，对每个最大深度的决策树模型都进行评分，这其中非常经典的一种方法就是交叉验证。__
  
  交叉验证的数据集划分 我们在创建一颗决策树时通常会将数据集划分为训练集和测试集。 如
    
    data_train, data_test, target_train, target_test = \
    train_test_split(housing.data, housing.target, test_size = 0.1, random_state = 42)
    
  如上面代码为例，我们设置测试集数据为10%，所以训练集数据为90%。
    
训练集用来训练我们的模型，它的作用就像我们平时做的练习题；测试集用来评估我们训练好的模型表现如何，它的作用像我们做的高考题，这是要绝对保密不能提前被模型看到的。
    
因此，__交叉验证中，我们用到的数据是训练集中的所有数据。__我们将训练集的所有数据平均划分成K份（通常选择K=10），取第K份作为验证集，它的作用就像我们用来估计高考分数的模拟题，
余下的K-1份作为交叉验证的训练集。
    
对于我们最开始选择的决策树的5个最大深度 ，以 max_depth=1 为例，我们先用第2-10份数据作为训练集训练模型，用第1份数据作为验证集对这次训练的模型进行评分，得到第一个分数；然后重新构建一个 max_depth=1 的决策树，用第1和3-10份数据作为训练集训练模型，用第2份数据作为验证集对这次训练的模型进行评分，得到第二个分数……以此类推，最后构建一个 max_depth=1 的决策树用第1-9份数据作为训练集训练模型，用第10份数据作为验证集对这次训练的模型进行评分，得到第十个分数。于是对于 max_depth=1 的决策树模型，我们训练了10次，验证了10次，得到了10个验证分数，然后计算这10个验证分数的平均分数，就是 max_depth=1 的决策树模型的最终验证分数。
  
  ### 最后：
  对于 max_depth = 2,3,4,5 时，分别进行和 max_depth=1 相同的交叉验证过程，得到它们的最终验证分数。然后我们就可以对这5个最大深度的决策树的最终验证分数进行比较，分数最高的那一个就是最优最大深度，对应的模型就是最优模型。






日后补充
-----------------------------------

__Fit():__ Method calculates the parameters μ and σ and saves them as internal objects.
解释：简单来说，就是求得训练集X的均值啊，方差啊，最大值啊，最小值啊这些训练集X固有的属性。可以理解为一个训练过程 

fit方法用于构建特征空间（也就是构建词典）
 
__Transform():__ Method using these calculated parameters apply the transformation to a particular dataset.
解释：在Fit的基础上，进行标准化，降维，归一化等操作（看具体用的是哪个工具，如PCA，StandardScaler等）。

训练集其实主要是学会数据中的特征空间（构建词典），之后我们需要用学到的特征空间去处理测试集。所以我们只需要用到transform方法，从而将测试集数据从文本数据转化为特征矩阵。

transform方法使用该空间将文本数据转化为特征矩阵

__Fit_transform():__ joins the fit() and transform() method for transformation of dataset.
解释：fit_transform是fit和transform的组合，既包括了训练又包含了转换。








