# Main Core



## 中途被略过的内容

被略过不是说它不重要，而是遵循 `Know how to use first` 的原则.

1. V1和V2版本Hadoop MapReduce和YARN的集群运行原理(架构和设计原理)图  -- 单独深入deep
2. 



## 核心摘要

(按照段落划分)

Hadoop安装的核心组件HDFS和YARN资源管理。

Hadoop应用程序(包括使用 MapReduce引擎的)，都作为YARN智商的应用程序框架运行。

Hadoop部分灵感来自Google GFS，MapReduce算法。

小规模下，Hadoop解决一些问题的方法的效率可能并不高(这是为伸缩扩展性所做的牺牲)。

大数据适宜的起点值110G(10^9字节)，一般公司常见的数据量是10~30T(兆兆字节)。

数据湖(data lake)作为多种数据源的数据存储库大部分数据按照原始形式存储，区别于RDB和数据仓库。

传统ETL为写时模式(schema on write)，预先设计数据格式；而hadoop为读时模式，按其原始格式或者读时才要求格式。

![image-20211115142613485](assets/imgs/image-20211115142613485.png)



V2版本的Hadoop把MapReduce单独分离出来作为一个运行在YARN上的应用程序框架。

MapReduce通过把任务应用到多个磁盘上，每个磁盘都有整体数据的不同部分或者切片，解决单磁盘的瓶颈。

MapReduce既可以在单机也可以在集群中运行，它是一种范式(单指令多数据SIMD算法)，不受执行方式的影响。

MapReduce虽然是两步算法，即Map和Reduce，但执行MapReduce查询之前还有一个透明步骤，把数据复制到HDFS上并执行切片。（然后才是在每个节点/切片上执行Map，然后执行Reduce）

![image-20211115144336372](assets/imgs/image-20211115144336372.png)

![image-20211115144352095](assets/imgs/image-20211115144352095.png)

映射(Map)：把映射函数应用于所有节点；输入列表是切片，输出列表是相应的运行结果

缩减(Reduce): 映射过程的输出列表编程缩减过程的输入列表，列表数据经过处理变为结果数据；汇总只是Reduce的一种形式。

MapReduce的优势：(过程中)不改变原始数据 (因为使用了函数方法)，仅创建新数据。





![image-20211115132456865](assets/imgs/image-20211115132456865.png)Hadoop核心组件:

* HCatalog: 让用户不用关心数据存储在哪。
* HBase: 类似于Google的BigTable，列式存储，Hadoop数据库。
* MapReduce查询工具:
  * Pig: 使用简单的脚本语言编写复杂的MapReduce转换，适用于ETL，快速研究数据，迭代数据处理。
  * Hive: 交互式SQL，HiveQL类似于SQL，透明地把在HBASE中执行的查询转换为MapReduce作业。
* 数据导入导出
  * Sqoop: 在RDB和Hadoop之间传输大量数据的工具。
  * Flume: 收集，聚集，移动可串行化数据（例如日志数据）的服务。
  * Avro: 连接 Flume 数据流，让数据能在不同语言编写的程序之间交换的**序列化格式**。
* 工作流自动化:
  * Oozie: 设计和管理Hadoop工作流的工具或者协调系统。
  * Falcon: 数据移动，插入，管道操作自动化工具，可触发作业启动。
* 管理:
  * Ambari: 集群资源调配，管理，监控的GUI工具



Hadoop YARN应用程序框架替代品有:

* Giraph 图形处理
* Spark 内存处理
* Storm 流处理
* Flink ? 



其他:

* ZooKeeper: 集群协调管理工具
* Mahout: 可扩展的机器学习库

