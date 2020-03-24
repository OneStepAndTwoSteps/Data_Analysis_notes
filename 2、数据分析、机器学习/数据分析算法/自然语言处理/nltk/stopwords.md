# stopwords

在nltk中停用词的使用

    from nltk.corpus import stopwords

    # 设置英文停用词
    stop_words = set(stopwords.words("english"))

此时即可使用停用词


### 调用停用词案例

    vectorizer = TfidfVectorizer(
                sublinear_tf=True,
                analyzer='word',
                token_pattern=r'\w{1,}',
                ngram_range=(1, 2),
                min_df=5,
                stop_words=stop)
    
    overview_text = vectorizer.fit_transform(train['overview'].fillna(''))
    linreg = LinearRegression()
    linreg.fit(overview_text, train['log_revenue'])
    eli5.show_weights(linreg, vec=vectorizer, top=20, feature_filter=lambda x: x != '<BIAS>')


*   stop_words = set(stopwords.words("english")) 这一步不设置，上面 TfidfVectorizer 中就无法直接调用
