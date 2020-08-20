# Grid and Random Search

超参数调整有几种方法:

* `Manual`：根据直觉/经验/猜测选择超参数，使用超参数训练模型，并在验证数据上评分。 重复此过程，直到您忍不住或对结果满意为止。

* `Grid Search`：建立一个超参数值网格，并为每个组合训练模型并在验证数据上评分。 在这种方法中，尝试使用超参数值的每个单个组合，这可能非常低效！

* `Random search`：设置超参数值的网格并选择随机组合以训练模型和得分。 搜索迭代次数是根据时间/资源设置的。

* `Automated Hyperparameter Tuning`：使用诸如梯度下降，贝叶斯优化或进化算法之类的方法对最佳超参数进行指导搜索。


## Random Search

与网格搜索相比，随机搜索的效率令人惊讶。尽管网格搜索最终会找到超参数的最佳值（假设它们在网格中），但随机搜索通常会在少得多的迭代中找到“足够接近”的值。为什么会这样呢：因为网格搜索花了太多时间来评估超参数搜索空间中没有希望的区域，因为它必须评估网格中的每个单个组合。相反，随机搜索在探索搜索空间方面做得更好，因此通常可以在更少的迭代中找到超参数的良好组合。


定义超参数：

    # Hyperparameter grid
    param_grid = {
        'boosting_type': ['gbdt', 'goss', 'dart'],
        'num_leaves': list(range(20, 150)),
        'learning_rate': list(np.logspace(np.log10(0.005), np.log10(0.5), base = 10, num = 1000)),
        'subsample_for_bin': list(range(20000, 300000, 20000)),
        'min_child_samples': list(range(20, 500, 5)),
        'reg_alpha': list(np.linspace(0, 1)),
        'reg_lambda': list(np.linspace(0, 1)),
        'colsample_bytree': list(np.linspace(0.6, 1, 10)),
        'subsample': list(np.linspace(0.5, 1, 100)),
        'is_unbalance': [True, False]
    }

### Random Search Function

    def random_search(param_grid, out_file, max_evals = MAX_EVALS):
        """随机搜索超参数优化。
         每次搜索迭代将搜索结果写入CSV文件."""
        
        
        # 结果数据框
        results = pd.DataFrame(columns = ['score', 'params', 'iteration'],
                                    index = list(range(MAX_EVALS)))
        for i in range(MAX_EVALS):
            
            # 选择随机超参数
            random_params = {k: random.sample(v, 1)[0] for k, v in param_grid.items()}
            random_params['subsample'] = 1.0 if random_params['boosting_type'] == 'goss' else random_params['subsample']

            # 评估随机选择的超参数
            eval_results = objective(random_params, i)
            results.loc[i, :] = eval_results

            # 打开连接（附加选项）并写入结果
            of_connection = open(out_file, 'a')
            writer = csv.writer(of_connection)
            writer.writerow(eval_results)
            
            # 确保关闭连接
            of_connection.close()
            
        # 得分排序
        results.sort_values('score', ascending = False, inplace = True)
        results.reset_index(inplace = True)

        return results 





