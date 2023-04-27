# make_scorer

[make_scorer 文档](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html)

导入包：

    from sklearn.metrics import make_scorer


案例：

结合 TimeSeriesSplit 时间序列分割(交叉验证) 来进行模型的评估

    FOLDS = 7
    count=1
    # skf = StratifiedKFold(n_splits=FOLDS, shuffle=True, random_state=42)

    tss = TimeSeriesSplit(n_splits=FOLDS)
    y_preds = np.zeros(sample_submission.shape[0])
    y_oof = np.zeros(X_train.shape[0])

    for tr_idx, val_idx in tss.split(X_train, y_train):
        clf = xgb.XGBClassifier(
            n_estimators=600, random_state=4, verbose=True, 
            tree_method='gpu_hist', 
            **params
        )

        X_tr, X_vl = X_train.iloc[tr_idx, :], X_train.iloc[val_idx, :]
        y_tr, y_vl = y_train.iloc[tr_idx], y_train.iloc[val_idx]
        
        clf.fit(X_tr, y_tr)

        score = make_scorer(roc_auc_score, needs_proba=True)(clf, X_vl, y_vl)       # <----- 重点

        print(f'{count} CV - score: {round(score, 4)}')
        count += 1


