#  Normal Data Player

**Name**: 普通数据玩家养成计划。

**Language**: Chinese. 

**Archive**: No. 

## 01. Preface

>  **Main Target:** to be a Data Player without master degree learning experience.

> 定义 `数据玩家` : 可以handle从底层基础设施到上层数据统计分析所有的专业人士。

究竟应该 from bottom to top or reverse？我也不太清楚。

以我的基础而言，应该从底层到上层会快一些，但也未必，如果只是做数据采集，那么我现有的Python和SQL知识应该足够了。嗯，总而言之，言而总之，顺其自然吧。

**从底层到上层会慢一些，因为底层各家都针对原始的开源(比如Hadoop, Storm, Flink/Blink等)做修正，打补丁，技术方案百家齐放（腾讯的不同于华为的，和IBM的，Google的，AWS的，Twitter的又不一样了，怎一个乱子了得）。上层则总是那几种采集，分析工具，可能变的也就是一些算法，但算法又是一个独立的领域，不仅限于 Data Engineer(数据工程领域)**。再者，如果你不知道数据究竟如何被使用就开始倒腾基础设施，往往枯燥，换句话说，如果我知道每天进出的数据量，知道这些内容存为文件不方便实时分析，那么再去倒腾Blink之类的技术框架或者PipeLine工具是不是更加有针对性了？



我的基本情况(backgroud)：

* **我并不是零基础，但如果零基础其实也可以按我的方式来**(只不过可能行进的慢一点？我猜的)。

* 之前我已经对整个 `数据领域` (包含大数据)有了一定的认识了, [Round 1](https://www.derekactions.com/post/23e8e883/#Round-1-Familiar-with-Off).
* **经过试验和探索，目前已经修改Path为From Top to Bottom; (原因见上)**

**本文(该folder)全部都是期间的笔记**(writen in Typora based on filesystem). **完整笔记**.(包括问题记录)

* 因为这个学习和训练期间的笔记，其实对于我没有太多了价值 (它不同于工作期间的 Handbook, Toolbox)
* 请用 **Typora 打开本目录/repo**

*下面步入正文*.

## 02. Normal Require

底层的基本要求：

1. 本科及以上学历(计算机，数学，统计)
2. 熟悉大数据技术栈 (HDFS、Kafka、Hive、HBase、Flink、Spark、Clickhouse)
3. 熟悉 Java/Scala语言，具有相关的开发经验
4. 熟悉 SQL，包括 Hadoop/Hive、Spark SQL相关经验
5. 对数据敏感，具备一定的数据分析能力

(来自某大券商的任职要求)



上层(数据挖掘、数据分析)的基本要求:

* 略。(目前我只盯着数据采集这一块)

## 03. Tips from pioneer

前辈建议: 

* 最关键的hadoop、hive入手，熟练使用框架后跟着demo看源码会很有帮助

* 要是想找一份高薪的工作，就不仅要掌握如Hadoop全家桶之类的大数据处理框架的使用，还需要掌握底层的原理及其调优方法

* 现在金融、保险、证券类公司基本都是阿里云的框架，不需要这么多开源的……
  举个栗子：离线数据分析基本用的是 polardb，通过用数据集成（底层就是datax）到maxcomptue（也就是odps）。可以导入后用分区字段动态分区，也可以设置变量，跑T+1模式，然后就是ODS—DWD—DWS—DWT—ADS。聚合计算出结果后，使用quickbi或者datav出BI，这样一个简单技术选型，但是很实用，也不贵，一般CTO应该会同意的……
* 至于实时数据处理，直接读RDS的数据，用DTS读到datahub（等于是缓存吧），再用阿里云的实时计算（其实底层就是flink，阿里应该是收购了flink，自己重构了一个框架，叫做blink），聚合计算后，再存入RDS。至于是否采用RDS，或者采用其它阿里云的数据库，完成可以根据公司的并发情况去选择。

... (懂得自然懂，不懂的后面也会懂)

总之，用好，然后学习其原理，然后有机会接触大平台，再来举一反三。

## 04. Core

**指导思想**就一条：**抓住核心，然后遇到问题解决问题**。

**具体来说**: <mark>直接上手，然后期间遇到问题解决问题</mark>。


## 05. Environment Explain

本地环境玩清楚了，再去玩云，而且一定要玩云，国际国内都要玩。

* 国际： AWS，GCP
* 国内：阿里云，腾讯云

主要是Windows和macOS作为客户端(分析)平台。

## 06. Check Specification

验收标准：

* Have **有足够多的案例练手 (必须)**

* Can 考取国内外知名大企业的 Certificate

* Can 找一份符合市场薪资的相关工作

## 07. Action List

> 指导思想：直接上手，然后期间遇到问题解决问题。

上手的意思是：**一丝不苟的吃透，步步为营**。

### Special Step INSERT HERE

**经过试验和探索(以及该领域的朋友建议)，目前已经修改Path为From Top to Bottom; (原因见上)**

详细的 Action List，请参考[steps_t2b](./steps_t2b/)以及[demos_for_job](./demos_for_job/)。

---

--TMP STOP -- START 2021.11.25--


### Step 1: Start Small (on Hadoop)

请参考目录(folder/director, `step1`).

摘要：通过一本简短且权威的实战类书籍，上手Hadoop。

概括：**预热**。

[step1 HERE](/steps/step1)

### Step 2: Repeat Hadoop

请参考目录(folder/director, `step2`).

摘要：通过大量的官方的，非官方的材料，系统吸收，确保自己没有理解错，真正理解并熟悉了。

概括：**系统吸收**。

[step2 HERE](/steps/step2)

### Step 3: Again Repeat Hadoop

请参考目录(folder/director, `step3`).

摘要：Review，整合，重新组织到自己的知识架构中。

概括：**深入，重组**。

[step3 HERE](/steps/step3)

### Step4: Start Spark & Repeat Spark & Again Repeat Spark

do the same thing on spark just like hadoop.

请参考目录(folder/director, `step4`).

[step4 HERE](/steps/step4)

### Step 5: Review Hadoop and Spark

请参考目录(folder/director, `step5`).

摘要：优化自己的该部分的知识架构。

概括: **深入并扩展**。

[step5 HERE](/steps/step5)

### Step 7: Checkpoint(Amend and Archive)

三遍的Hadoop；Hadoop基本没有问题了，这里要停一下；这里要确保拆解Hadoop这个框架的时候，周边的技术，需要的技术，比如linux系统，计算机网络，进程知识，涉及到的设计模式，相关语言(Java啊，C++啊，Python啊，SHELL啊)等等，在进入下一个大数据框架比如Flink的时候不会成为阻碍，使得你可以用上一个框架。

**略**.

(下面要做项目或者大量实践；在这里查漏补缺：该考证考证，考刷题就刷题)

### Step 8: Multiple Capstone Project

**网上找或者购买一些实践项目，确保自己有足够的练手素材，实际的Case经验**。

[step8 HERE](/steps/step8)。

*只有项目介绍、视频，结果。具体实验代码，仅在面试时展现(不上传了)*。



--TMP STOP -- END 2021.11.25--

---



## 08. Timeline

| 序号 | 所属阶段 |     时间(start)     |      时间(end)      | 主要事项                                                     | 补充说明                                                     |
| :--: | :------: | :-----------------: | :-----------------: | :----------------------------------------------------------- | ------------------------------------------------------------ |
| 001  |  Step1   | 2021-11-14 08:22:48 | 2021-11-15 00:10:48 | Setup Learning Framework<br />建立快速学习计划，构建模型框架. | Create Repo 'data-player' and Initiate.<br />Fix Some formats problem. |
| 002  |  Step1   | 2021-11-15 07:25:24 |                     | Hands on <写给大忙人的Hadoop2>                               | 看两遍，所有案例完全跑通，期间涉及到的所有没有熟悉的技术记录下来，预留案底，直至Step5 一并解决。 |
| 003  |          |                     |                     |                                                              |                                                              |
| 004  |          |                     |                     |                                                              |                                                              |
| 005  |          |                     |                     |                                                              |                                                              |
| 006  |          |                     |                     |                                                              |                                                              |
| 007  |          |                     |                     |                                                              |                                                              |
| 008  |          |                     |                     |                                                              |                                                              |
| 009  |          |                     |                     |                                                              | *个人还是习惯于用 excel 或者 numbers 记录，后续不再更新该表格* |

因为我有 DailyTrack 类似于下面这样，所以记录上面的表格，**冗余**。

![an example](assets/imgs/image-20211114233645459.png)

*如果最后由于隐私问题没有公开 daily track，请参考 `Task List`，目标导向的也比较详细。*

*具体 Task 请单独参考文件[`CheckList`](./CheckList.md)。*

## 09. Troubles

中途遇到的问题，以及浪费时间的地方。详细请单独参考文件[`CheckList`](./CheckList.md)。

## 10. Refs & Materials

详细请单独参考文件[`CheckList`](./CheckList.md)。

## 11. Acknowledgement

中途咨询过的前辈，先驱，从业者，同行等:

*(排名不分先后)*

*(为他们的防骚扰考虑，暂不公开)*

## 12. Postfix

Will you a pleasant life.

See ya.

