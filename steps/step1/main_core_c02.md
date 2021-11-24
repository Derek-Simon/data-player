# Main Core

安装其实是SCM或者运维人员的事情，或者有时候我们也没有权利选择服务器，动手去安装。

但，说不定呢？



## 被忽略的内容





## 核心摘要

核心服务(java进程): 

1. HDFS服务: 

   * NameNode和DataNode(至少一个)服务。

   * SecondaryNameNode服务  (定期从NameNode回迁内存中的HDFS编辑信息，然后合并返回给NameNode)。

2. YARN服务:

   * Resource Manager: 集群的所有作业的单独主调度程序，通过与工作节点上的NodeManager进行通信而发挥作用。Resource Manager以及NodeManager并不关心节点运行的是什么工作。

   * NodeManager: 管理节点实际完成的工作(至少要有一个NodeManager)；

   * Job/ApplicationHistoryServer可以作为YARN的一部分记录MapReduce的作业历史。



核心服务的配置文件配置文件都采用 XML 配置，例如 `hdfs-site.xml`, `yarn-site.xml`，均放置在`/etc/hadoop`下面。每个属性大致都采用如下格式：

```xml
<property>
  <name>dfs.replication</name>
  <value>1</value>
</property>
```

环境文件(`*.sh`)一般用于设置特定的服务的环境变量和Java选项。

XML文件和`*.sh`文件一般都需要重启才能生效。



集群配置并不是一件容易的事情，至少涉及一下几个需要考虑的方面：

* 网络性能设计
* 支持故障转移策略
* 服务器存储容量
* 处理器个数(核心数)
* 工作流策略



安装环境首先考虑，Linux操作系统(文件系统)和JDK版本对Hadoop的支持。

Hadoop默认运行在非安全模式下，即不需要身份验证。

安全模式需要通过Kerberos的身份验证才能使用Hadoop的服务。

Hadoop的安全功能包括身份验证、服务级别授权、Web控制台的身份验证以及数据的保密性。



Hadoop通过单个集群部署多个NameNode来显著提高HA，或者也可以通过QJM仲裁日志管理器的新功能引入HA。（备用NameNode可以手动或者自动激活）



## 安装Hadoop

大致分为3类：

1. 单机安装: 
   * HDP沙箱安装：Hadoop沙箱板和全套工具 （无法模拟集群环境）
   * 伪分布式安装: 安装Apache Hadoop完整版 (可以模拟集群环境)
2. Ambari集群安装:
3. Whirr云安装:



### 单机安装

HDP沙箱？

使用 VirtualBox 在 macOS 上运行 Hadoop沙箱。

1. VirtualBox：[link](https://download.virtualbox.org/virtualbox/6.1.28/)
2. Hortonworks 虚拟机(镜像): 去cloudera下载

太坑爹了，Cloudera不让下载了。

额，**直接源码单机安装算了**。(即伪分布式安装)



**伪分布式安装**:

1. 下载 hadoop安装包并解压到相关目录
2. 设置 环境变量 `JAVA_HOME` 和 `HADOOP_HOME`
3. 创建用户和组，用单独的用户去运行各类守护程序
4. 建立数据目录并分配其权限，建立日志目录分配写权限
5. 配置核心配置文件 `core-site.xml`,`hdfs-site.xml`,`mapred-site.xml`,`yarn-site.xml`
6. 修改java堆大小(每个进程的堆大小都可以单独配置，默认都是1G，这里调小)
7. 格式化 HDFS的name node目录



下面是具体步骤:

```bash
cd /root
wget https://archive.apache.org/dist/hadoop/common/hadoop-2.6.0/hadoop-2.6.0.tar.gz
cd /opt
tar xzvf /root/hadoop-2.6.0.tar.gz
```

然后设置 java 和 haoop 的环境变量文件:

```bash
# /etc/profile.d/hadoop.sh
export HADOOP_HOME=/opt/hadoop-2.6.0;
export PATH=$HADOOP_HOME/bin:$PATH
```

并导入：

```bash
source java.sh
source hadoop.sh
```

创建用户和组，用来运行守护进程:

```bash
# yarn, hdfs, mapred全部分配到hadoop组
groupadd hadoop
useradd -g hadoop yarn
useradd -g hadoop hdfs
useradd -g hadoop mapred
```

建立目录并分配其权限:

```bash
#创建数据目录(为各类node)
mkdir -p /var/data/hadoop/hdfs
cd /var/data/hadoop/hdfs
##各类node的数据目录
mkdir nn snn dn
chown -R hdfs:hadoop /var/data/hadoop/hdfs

# 创建日志目录(主要为yarn)
mkdir -p /var/log/hadoop/yarn
chown -R hdfs:hadoop /var/log/hadoop/yarn

# 还要为hadoop安装包里面设置 log 目录
cd /opt/hadoop-2.6.0
mkdir logs
chmod g+w logs
chown -R yarn:hadoop logs
```

配置核心配置文件 `/opt/hadoop-2.6.0/etc/hadoop/core-site.xml`:

```xml
<configuration>
  <property>                                                                                                                      
    <name>fs.default.name</name>
    <value>hdfs://localhost:9000</value>
  </property>

  <property>
    <name>hadoop.http.staticuser.user</name>
    <value>hdfs</value>
  </property>
</configuration>
```

然后配置 `/opt/haddop-2.6.0/etc/hadoop/hdfs-site.xml`文件，因为是单机，所以 replication 就设置为1(默认保留3个副本)，同时指定数据的数据目录。

```xml
<configuration>
  <property>                                                                                                                          
    <name>dfs.replication</name>
    <value>1</value>
  </property>
  <property>
    <name>dfs.namenode.name.dir</name>
    <value>file:/var/data/hadoop/hdfs/nn</value>
  </property>
  <property>
    <name>fs.checkpoint.dir</name>
    <value>file:/var/data/hadoop/hdfs/snn</value>
  </property>
  <property>
    <name>fs.checkpoint.edits.dir</name>
    <value>file:/var/data/hadoop/hdfs/snn</value>
  </property>
  <property>
    <name>dfs.datanode.data.dir</name>
    <value>file:/var/data/hadoop/hdfs/dn</value>
  </property>
</configuration>
```

然后配置 `mapred-site.xml`，把 MapReduce 作为 YARN 应用程序运行:

```bash
cp mapred-site.xml.template mapred-site.xml
```



```xml
<configuration>
  <property>                                                                                                                          
    <name>mapreduce.framework.name</name>
    <property>yarn</property>
  </property>

  <property>
    <name>mapreduce.jobhistory.intermediate-done-dir</name>
    <property>/mr-history/tmp</property>
  </property>

  <property>
    <name>mapreduce.jobhistory.done-dir</name>
    <property>/mr-history/hone</property>
  </property>
</configuration>
```

最后配置 `yarn-site.xml`，对非 MapReduce作业的数据进行随机化:

```xml
<configuration>
  <property>                                                                                                                          
    <name>yarn.nodemanager.aux-service</name>
    <value>mapreduce_shuffle</value>
  </property>

  <property>
    <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
    <value>org.apache.hadoop.mapred.ShuffleHandler</value>
  </property>
</configuration>
```

调整进程的堆大小，`/etc/hadoop/hadoop-env.sh`:

```bash
export HADOOP_HEAPSIZE="500"
export HADOOP_NAMENODE_INIT_HEAPSIZE="500"
```

`mapred-env.sh`:

```bash
export HADOOP_JOB_HISTORYSERVER_HEAPSIZE=250
```

`yarn-env.sh`:

```xml
JAVA_HEAP_MAX=-Xmx500m
YARN_HEAPSIZE=500
```

停止Hadoop库的某些原生警告，`hadoop-env.sh`:

```xml
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export HADOOP_OPTS="$HADOOP_OPTS -Djava.library.path=$HADOOP_HOME/lib/native"
```

格式化 HDFS 的 namenode 目录:

```bash
```







