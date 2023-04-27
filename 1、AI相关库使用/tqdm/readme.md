# tqdm 模块

tqdm 是 Python 中专门用于进度条美化的模块，通过在非 while 的循环体内嵌入 tqdm，可以得到一个能更好展现程序运行过程的提示进度条

### tqdm:

tqdm 中的 tqdm() 是实现进度条美化的基本方法，在 for 循环体中用 tqdm() 包裹指定的迭代器或 range() 即可，下面是两个简单的例子：


    from tqdm import tqdm
    import time

    text = ""
    for char in tqdm(["a", "b", "c", "d"]):
        time.sleep(0.25)
        text = text + char
        
    print(text)

### tqdm_notebook

tqdm针对jupyter notebook添加了专门的进度条美化方法，使用tqdm_notebook()方法，下面是一个简单的例子：

    for col in tqdm_notebook(to_encode):
        freq_enc_dict = frequency_encoding(col)
        train[col] = train[col].map(lambda x: freq_enc_dict.get(x, np.nan))
        test[col] = test[col].map(lambda x: freq_enc_dict.get(x, np.nan))
        cat_cols.remove(col)



        