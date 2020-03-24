# 解决 pandas 读取数据时内存过大的问题

### 背景：

在我们使用pandas进行数据处理的时候，有时候发现文件在本地明明不大，但是用pandas以DataFrame形式加载内存中的时候会占用非常高的内存，这是因为pandas的处理机制默认会按照最大的规格去设置数据类型。


### 数据类型占用内存表格

-   __常用的数据类型范围如下所示：__

        dtypes	        范围下限（含）	                        范围上限（含）
        unit8	            0	                                 255
        unit16	            0	                                 65535
        int8	          -128	                                 127
        int16	          -32768	                             32767
        int32	          -2147483648	                         2147483647
        int64	         –9,223,372,036,854,775,808	            9,223,372,036,854,775,807



### 案例展示：

-   __制造数据：__

        data = {'player1':[70,75,60,68]}

        data = pd.DataFrame(data)
        data


            player1
        0	70
        1	75
        2	60
        3	68

-   __输出数据和他的数据类型：__

        for i in data['player1'].values:
            print(type(i))

        <class 'numpy.int64'>
        <class 'numpy.int64'>
        <class 'numpy.int64'>
        <class 'numpy.int64'>


### 解决方法：

    def reduce_mem_usage(df, verbose=True):
    
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

        # 计算当前占用的内存 
        start_mem = df.memory_usage(deep=True).sum() / 1024**2

        # 循环每一列
        for col in df.columns:

            # 获取每一列的数据类型
            col_type = df[col].dtypes

            # 如果数据类型属于上面定义的类型之
            if col_type in numerics:

                # 计算该列数据的最小值和最大值 用于我们指定相应的数据类型 
                c_min = df[col].min()
                c_max = df[col].max()

                # 如果 该列的数据类型属于 int 类型，然后进行判断
                if str(col_type)[:3] == 'int':
                    # 如果 该列最小的值 大于int8类型的最小值，并且最大值小于int8类型的最大值，则采用int8类型 
                    if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                        df[col] = df[col].astype(np.int8)

                    # 同上
                    elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                        df[col] = df[col].astype(np.int16)

                    # 同上
                    elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                        df[col] = df[col].astype(np.int32)

                    # 同上
                    elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                        df[col] = df[col].astype(np.int64)

                # 否则 则采用 float 的处理方法       
                else:

                    if c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                        df[col] = df[col].astype(np.float32)

                    else:
                        df[col] = df[col].astype(np.float64)

        end_mem = df.memory_usage(deep=True).sum() / 1024**2

        if verbose: print('Mem. usage decreased to {:5.2f} Mb ({:.1f}% reduction)'.format(end_mem, 100 * (start_mem - end_mem) / start_mem))
        return df
        


