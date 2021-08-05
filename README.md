# DEA-analysis-based-on-StockData
使用DEA分析新浪财经部分股票数据，内含文件下载爬虫，本DEA分析模块基于pyDEA，输出综合效率，纯技术效率，规模效率

## 安装

本项目需要安装pyDEA模块，项目地址：https://github.com/jzuccollo/pyDEA

## 使用方法

### 1. 爬取新浪财经网上的股票数据

使用语法：python spyderForStockData.py [股票代码]
使用例子：python spyderForStockData.py 601318

输出：

该股票的资产负债表.csv

该股票的利润表.csv

该股票的现金流量表.csv

### 2. 使用DEA分析以上股票数据

根据论文《林业上市公司融资效率的DEA分析_省略_林业上市公司与吉林森工融资的视角_李颂》

本次DEA分析的输入数据读取：总资产（X1）、负债总额（X2）、所有者权益（X3）、营业总成本（X4）、筹资活动的现金流入量（X5）

输出数据读取：营业收入（Y1） 和净利润（Y2）

使用语法：python deaAnayisis.py [股票代码]
使用例子：python python deaAnayisis.py 601318

输出：

一个csv表，内容如下：

![9471320bd17cceb1ad62d7b63884f89](https://user-images.githubusercontent.com/54057111/128315526-7212832d-82d6-4219-afe3-1bcaae0406a3.png)
