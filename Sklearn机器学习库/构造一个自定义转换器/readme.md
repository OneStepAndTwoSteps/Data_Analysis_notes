## 构造一个自定义转化器

尽管 Scikit-Learn 提供了许多有用的转换器，你还是需要自己动手写转换器执行任务，比如自定义的清理操作，或属性组合。你需要让自制的转换器与 Scikit-Learn 组件（比如流水线）无缝衔接工作，因为 Scikit-Learn 是依赖鸭子类型的（而不是继承），你所需要做的是创建一个类并执行三个方法： fit() （返回 self ）， transform() ，和 fit_transform() 。

通过添加 TransformerMixin 作为基类，可以很容易地得到最后一个。另外，如果你添加 BaseEstimator 作为基类（且构造器中避免使用 *args 和 **kargs ），你就能得到两个额外的方法（ get_params() 和 set_params() ），二者可以方便地进行超参数自动微调。例如，一个小转换器类添加了上面讨论的属性：


*   构造一个自定义转换器用于生成新的特征(特征组合)

        from sklearn.base import BaseEstimator,TransformerMixin
        rooms_ix ,bedrooms_ix,population_ix,household_ix = 3,4,5,6

        class CombinedAttributesAdder(BaseEstimator,TransformerMixin):
            def __init__(self,add_bedroom_per_room=True):
                self.add_bedroom_per_room = add_bedroom_per_room
            def fit(self,x,y):
                return self
            def transform(self,x,y=None):
                # 求取每个房间平均的房间数
                rooms_per_household = x[:,rooms_ix]/x[:,household_ix]   

                # 求每个人拥有的平均房间数      
                population_per_household = x[:,population_ix]/x[:,household_ix] 

                if self.add_bedroom_per_room:
                    #bedrooms_per_room为可选的合成属性
                    bedrooms_per_room = x[:,bedrooms_ix]/x[:,rooms_ix]  
                    
                    # 将新组合的两个属性按列合并到传入的数据中，然后返回
                    return np.c_[x,rooms_per_household,population_per_household,bedrooms_per_room]
                else:
                    return np.c_[x, rooms_per_household, population_per_household]

        attr_adder = CombinedAttributesAdder(add_bedroom_per_room=False)
        housing_extra_attribs = attr_adder.transform(housing.values)


在这个例子中，转换器有一个超参数 add_bedrooms_per_room ，默认设为 True （提供一个合理的默认值很有帮助）。这个超参数可以让你方便地发现添加了这个属性是否对机器学习算法有帮助。更一般地，你可以为每个不能完全确保的数据准备步骤添加一个超参数。数据准备步骤越自动化，可以自动化的操作组合就越多，越容易发现更好用的组合（并能节省大量时间）。



源自 Hands on Machine Learning with Scikit Learn and TensorFlow - 中文版

