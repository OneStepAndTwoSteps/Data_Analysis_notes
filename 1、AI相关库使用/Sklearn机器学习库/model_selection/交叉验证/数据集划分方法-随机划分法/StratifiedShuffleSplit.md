### StratifiedShuffleSplit

分层ShuffleSplit交叉验证器

提供训练/测试索引以将数据拆分为训练/测试集。

此交叉验证对象是StratifiedKFold和ShuffleSplit的合并，返回分层的随机折叠。折叠是通过保留每个类别的样品百分比来进行的。

注意：像ShuffleSplit策略一样，分层随机拆分并不能保证所有折痕都会不同，尽管这对于可伸缩的数据集仍然很有可能。



*   导入包

        from sklearn.model_selection import StratifiedShuffleSplit

*   参数

        n_splits int，默认为10
          n_splits是将训练数据分成train/test对的组数，可根据需要进行设置，默认为10

        test_size 浮点数，整数，无，可选（默认值：无）        
          如果为float，则应在0.0到1.0之间，并且代表要包含在测试拆分中的数据集的比例。如果为int，则表示测试样本的绝对数量。
          如果为None，则将值设置为火车尺寸的补码。如果train_size也是，则将其设置为0.1。

        train_size 浮点数，整数或无，默认为无
          如果为float，则应在0.0到1.0之间，并表示要包含在火车分割中的数据集的比例。如果为int，则表示火车样本的绝对数量。
          如果为“无”，则该值将自动设置为测试大小的补码。

        random_state int，RandomState实例或无，可选（默认值：无）   **设置随机种子**
          如果为int，则random_state是随机数生成器使用的种子；否则为false。如果是RandomState实例，则random_state是随机数生成器；
          如果为None，则随机数生成器是所使用的RandomState实例np.random。









