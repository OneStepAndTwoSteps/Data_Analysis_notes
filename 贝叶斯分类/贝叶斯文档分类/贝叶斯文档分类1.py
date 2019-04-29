
import os
import pandas as pd
import jieba
import io
from sklearn.feature_extraction.text import  TfidfVectorizer
from sklearn.naive_bayes import  MultinomialNB
from sklearn import metrics
# sklearn.metrics中含有分类报告函数classification_report()
# from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_fscore_support

# from sklearn.model_selection import train_test_split

text_train_path='text_classification-master/text classification/train'
text_test_path='text_classification-master/text classification/test'
stop_file_path='text_classification-master/text classification/stop/stopword.txt'

def read_file(label,file_path):
    label={}
    for i,file in enumerate(file_path):
        with open(file,'r',encoding='gb18030') as  f:
            text=f.read()
            label[i]=text
    return label


def merge_data(dataset):

    for dir_abspath,_,filename in os.walk(dataset):
        if len(filename) == 0 :
            print('None')
        else:
            dirname=dir_abspath.split('\\')[1]
            dirname_list=dirname+'_list'
            dirname_list=[]
            for basename in filename:
                dirname_list.append(os.path.join(dir_abspath,basename))

            dirname_dict=dirname+'dict'
            dirname_dict=read_file(label=dirname,file_path=dirname_list)

            df1=pd.DataFrame({'content':dirname_dict,'label':dirname})
            if 'train' in dir_abspath:
                df1.to_csv('train_data.csv',mode='a',index=None)
            if 'test' in dir_abspath :
                df1.to_csv('test_data.csv',mode='a',index=None)



if __name__ == '__main__':
    # merge_data(text_test_path)
    # exit()
    # 加载数据
    train_csv=pd.read_csv('train_data.csv',delimiter=',')
    test_csv=pd.read_csv('test_data.csv',delimiter=',')


    print(train_csv.head())
    print('一共有{0}条内容，一共有{1}条标签'.format(len(train_csv.content.unique()),len(train_csv.label.unique())))
    # print(train_csv)

   # 划分训练集内容和对应的标签
    X_train,Y_train=train_csv['content'],train_csv['label']
    X_test,Y_test=test_csv['content'],test_csv['label']
    print(X_train.head())

    # 加载停用词表
    stop_words = [line.strip() for line in io.open(stop_file_path, encoding='utf-8').readlines()]

    # max_df表示单词在文档中出现的最高频率，此处max_df设置为0.5表示一个单词如果在50%的文本中都出现过，则不作为分词统计，因为它只携带了很少的信息
    # 一般不设置min_df因为这样的词很多、
    tf=TfidfVectorizer(tokenizer=jieba.cut,stop_words=stop_words,max_df=0.5)
    train_features=tf.fit_transform(X_train)
    print(train_features.shape) # 测试集特征矩阵的列数与训练集特征矩阵的列数是一致的

    # test_tf=TfidfVectorizer(tokenizer=jieba.cut,stop_words=stop_words,max_df=0.5,vocabulary=tf.vocabulary_)
    # test_features = test_tf.fit_transform(X_test)
    test_features = tf.transform(X_test)
    print(test_features.shape) # 测试集特征矩阵的列数与训练集特征矩阵的列数是一致的
    print('一共有{0}条内容，一共有{1}条标签'.format(len(test_csv.content),len(test_csv.label)))


    # 多项式叶贝斯分类器 alpha为平滑参数
    '''
        为什么要使用平滑呢？因为如果一个单词在训练样本中没有出现，这个单词的概率就会被计算为 0。但训练集样本只是整体的抽样情况，
        我们不能因为一个事件没有观察到，就认为整个事件的概率为 0。为了解决这个问题，我们需要做平滑处理。
        
        当 alpha=1 时，使用的是 Laplace 平滑。Laplace 平滑就是采用加 1 的方式，来统计没有出现过的单词的概率。
        这样当训练样本很大的时候，加 1 得到的概率变化可以忽略不计，也同时避免了零概率的问题。
        
        当 0<alpha<1 时，使用的是 Lidstone 平滑。对于 Lidstone 平滑来说，alpha 越小，迭代次数越多，精度越高。我们可以设置 alpha 为 0.001。
        
        实验结果： 没加alpha=0.001时精度为0.83 加了之后精度为0.93
    '''
    clf=MultinomialNB(alpha=0.001)
    clf.fit(train_features,Y_train)


    # 预测
    predicted_labels = clf.predict(test_features)

    # print(pd.DataFrame(features.toarray(),columns=tf.get_feature_names()))

    # 显示前10行预测和实际标签
    # for prediction, truth in zip(predicted_labels[:10], Y_test[:10]):
    #     print(prediction, truth)

    # 输出精度
    # print(metrics.accuracy_score(Y_test,predicted_labels))

    # 输出准确率: {0}, 召回率: {1}, F1值: {2｝
    p, r, f1, _ = precision_recall_fscore_support(Y_test, predicted_labels, average='macro')
    print("\n准确率: {0}, 召回率: {1}, F1值: {2}".format(p, r, f1))


    # print(classification_report(Y_test, predicted_labels, labels=train_csv.label.unique()))
