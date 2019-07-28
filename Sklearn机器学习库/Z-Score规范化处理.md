### Z-Score规范化处理

Z-score标准化，也称为标准化分数，这种方法根据原始数据的均值和标准差进行标准化，经过处理后的数据符合标准 __正态分布__，即均值为0，标准差为1（根据下面的转化函数很容易证明），转化函数为：

![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/Data_Analysis/master/Sklearn%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%BA%93/static/Z-score.png)

对应的类是
from sklearn.preprocessing import StandardScaler

__例子：__

    # 准备训练集和测试集
    x_train,x_test,y_train,y_test=train_test_split(content[features_mean],content['diagnosis'],test_size=0.3)

    # 数据规范化
    # 采用 Z-Score 规范化数据，保证每个特征维度的数据均值为 0，方差为 1
    ss=StandardScaler()
    train_x=ss.fit_transform(x_train)
    test_x=ss.transform(x_test)










