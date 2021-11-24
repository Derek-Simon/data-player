# Main Core



## 核心摘要



### HDFS组件

1. HDFS 没有随机写入，所有的写入都限制为追加，字节总是追加到流的末尾；一次写，多次读。
2. 批量，顺序，数据库(64MB/128MB)读取，无需缓存机制。
3. 集群节点往往既是计算节点，又是存储节点。
4. 跨集群维护多个副本数据。
5. NameNode就像一个买办，客户端的读写操作先要和它确认，然后它给出具体的DataNode，然后客户端才能通过DataNode进行读写，且写的时候DataNode完成写后还要完成拷贝，再通知NameNode操作完成。
6. NameNode再内存中存储数据库和DataNode映射关系。
7. NameNode发送检测信息给DataNode，DataNode每隔10个信号会主动发送数据块的报告给NameNode。
8. SecondNameNode，即 CheckPointNode，执行定期检查/评估NameNode状态的操作，而非故障切换点。
9. NameNode通过 `fsimage_*`和`edit_*`两个磁盘文件来跟踪元数据的修改。
10. CheckPointNode总是下载、编辑、合并 `fsimage_*`文件，并把它们上传到NameNode，供其启动时读取。(事实上，通过这种方式确保NameNode总是读取到的最新的元数据，即数据库和DataNode的映射)(并且由于CheckPointNode的代劳，NameNode启动时仅读取最新的元数据即可)



### HDFS块

1. 默认块为64MB(而操作系统一般是4或者8KB)，但还是根据文件大小而改变创建块的大小；20KB文件，则创建20KB左右的块，80MB则创建64MB和16MB的块。
2. 超过8个节点的集群，一般复制因子是3；1~8节点(包含8)一般是2。
3. 复制因子的大小表示，所有集群中总共保留数据块的个数



### HDFS安全模式

1. 安全模式，在NameNode启动，等待更多的DataNode注册(块与数据建立联系)，此时不能复制或者删除块。
2. 安全模式也是重建文件系统状态的过程(加载fsimage)。
3. 管理员可以手动进入安全模式对 HDFS 进行维护。 `hdfs dfsadmin-safemode`。



### NameNode HA

1. 活动的NameNode负责所有的客户端HDFS操作，待机的NameNode保持足够的状态，以便提供快速故障切换的
2. 活动的NameNode将所有的FS编辑信息发送到日志节点仲裁器
3. 在HA中不需要CheckPointNode，因为备用的NameNode本身就执行活动NameNode相关状态的记录了
4. JournalNodes也是需要多个独立的节点方便做故障转移，备用的JournalNodes从活动的读取状态(同步)
5. HA配置中日志节点仅允许活动NameNode写入，即备用的NameNode只能从其读取状态信息
6. ZooKeeper可用于保证NameNode的HA，比如备用到活动的NameNode选举。

![image-20211124154756148](assets/imgs/image-20211124154756148.png)





### NameNode联邦

分割总的命名空间，以扩展/提高文件系统的读写效率(吞吐量)。

![image-20211124155329207](assets/imgs/image-20211124155329207.png)





### 检查点和备份

1. 元数据存储在 fsimage 中，fs的编辑信息存储在日志中，CheckPointNode编辑合并它们，返回一个信息的fsimage供NameNode启动时读取。
2. BackupNode和CheckPointNode类似，但它同时在内存和磁盘上保持NameNode的最新副本(所以不需要再去获取fsimage和编辑信息)
3. NameNode同一时间仅支持一个BackupNode，且工作时CheckPointNode无法注册



### HDFS网关

通过本地文件系统或者挂载点来操作HDFS的一种机制。(网关，下一站的入口点)



### HDFS用户命令

hdfs命令。用户命令，一般命令。

用户命令，比如 `hdfs dfs`, `hdfs namenode`,`hdfs dfsadmin`，基本每个用户命令针对一个组件或者大功能。

一般命令，在用户命令的每个命令里面还有很多子命令，这里以 genericOptions的形式给出，比如 `hdfs dfs -ls`, `hdfs dfs -cp`等，具体就是用来操作每个组件的。



### HDFS编程接口

1. 接口是抽象的，所以从 HDFS 读写数据和从其他文件系统读写数据并没有本质区别。
2. 在 hadoop 内编译和运行相应的文件区别于一般文件系统(主要是要导环境或者路径)
3. 因为Hadoop基本是用Java写的，所以如要要用C API操作HDFS，那么需要借用 JNI 库, libhdfs。