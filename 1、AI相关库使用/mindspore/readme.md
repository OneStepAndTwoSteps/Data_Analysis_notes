# mindspore 框架的使用


## config introduce


* https://gitee.com/mindspore/mindformers/tree/dev/configs


## .yaml 配置文件关键参数：

* runner_config: 运行配置
    
    * epochs: 迭代次数
    * <font color  = orange>**batch_size:**</font> 数据批次大小，当前在使用yaml初始化训练时，会覆盖数据集配置中的batch_size，后面会删除改配置
    * sink_mode: 是否开启数据下沉模式
    * sink_size: 每次下沉数据大小，-1代表全量下沉

</br>

* parallel_config: 并行策略配置，可以参考mindformers.modules.transformer.TransformerOpParallelConfig

    * <font color  = orange>**data_parallel:**</font> 数据并行
    * <font color  = orange>**model_parallel:**</font> 模型并行
    * <font color  = orange>**pipeline_stage:**</font> 流水线并行
    * <font color  = orange>**optimizer_shard:**</font> 是否开启优化器切分。优化器并行开关，通常在半自动并行模式下生效，与parallel中的enable_parallel_optimizer保持一致，默认将模型权重参数切份data_parallel份
    * <font color  = orange>**micro_batch_num:**</font> 流水线并行的微批次大小。pipeline_satge大于1时，开启流水并行时使用，此处需满足micro_batch_num >= pipeline_satge
    * <font color  = orange>**gradient_aggregation_group:**</font> 梯度通信算子融合组的大小

</br>

* <font color  = orange>**micro_batch_interleave_num：**</font>batch_size的拆分份数，多副本并行开关，通常在模型并行时使用，用于优化model_parallel时产生的通信损耗，纯流水并行时不建议使用。可以参考mindspore.nn.MicroBatchInterleaved

global_batch_size = batch_size * data_parallel * micro_batch_num * micro_batch_interleave_num

半自动并行的模式下 parallel_config 下的参数都生效

## 训练脚本的启用：


## 模型的训练command

