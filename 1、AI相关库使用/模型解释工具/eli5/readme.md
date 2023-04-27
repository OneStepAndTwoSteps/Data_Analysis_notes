# ELI5

ELI5是一个Python包，它有助于调试机器学习分类器并解释它们的预测。它为以下机器学习框架和包提供支持：

*   __scikit-learn__

    目前，ELI5允许解释scikit-learning线性分类器和回归量的权重和预测，将决策树打印为文本或SVG，显示特征重要性并解释决策树和基于树的集合的预测。

    支持Pipeline和FeatureUnion。

    ELI5通过scikit-learn了解文本处理实用程序，并可相应地突出显示文本数据。它还允许通过撤消散列来调试包含HashingVectorizer的scikit-learn管道。

*   __XGBoost__
    
    显示功能重要性并解释XGBClassifier，XGBRegressor和xgboost.Booster的预测。

*   __LightGBM__ 
    
    显示功能重要性并解释LGBMClassifier和LGBMRegressor的预测。

*   __CatBoost__
    
    显示CatBoostClassifier和CatBoostRegressor的功能重要性。

*   __lightning__ 
    
    解释闪电分类器和回归量的权重和预测。

*   __sklearn-crfsuite__
    
      ELI5允许检查sklearn_crfsuite.CRF模型的权重。

*   __Keras__ 
    
      通过Grad-CAM可视化解释图像分类器的预测。

ELI5还实现了几种检测黑盒模型的算法 ([Inspecting Black-Box Estimators](https://eli5.readthedocs.io/en/latest/blackbox/index.html#eli5-black-box))：

*   __TextExplainer__   

    允许使用 LIME 算法解释任何文本分类器的预测（Ribeiro等，2016）。有一些实用程序可以将 LIME 与非文本数据和任意黑盒分类器一起使用，但此功能目前是实验性的。

*   __Permutation Importance__ (置换重要性方法) 
    
    可用于计算黑盒估计器的特征重要性。

