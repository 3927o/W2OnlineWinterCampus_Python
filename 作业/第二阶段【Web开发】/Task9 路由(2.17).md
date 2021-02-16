# Task9 路由(2.17)

### 学习目标

- 了解Flask的路由规则



### 学习任务

1. 请设计一个网站，要求如下
   1. 当访问URL"http://127.0.0.1:5000/"时，网页显示"Hello Flask"字样。
   2. 当访问URL“http://127.0.0.1:5000/index”时，网页显示"Index Page"字样。
   3. 当访问URL“http://127.0.0.1:5000/hello/\<username>”时，网页显示“Hello, username”字样，其中username为字符串变量。
   4. 当访问URL“http://127.0.0.1:5000/hello/\<float>”时，网页显示URL中浮点数变量与39相乘的值。如访问URL“http://127.0.0.1:5000/hello/2.5”时，网页会显示”97.5“
   5. 当访问URL“http://127.0.0.1:5000/get_welcome_url/\<username>”时，网页会显示上述第三点题目的url。如当我访问URL"http://127.0.0.1:5000/get_welcome_url/lin"时，网页显示“http://127.0.0.1:5000/hello/lin”字样
   6. 当访问URL“http://127.0.0.1:5000/delete”时，网页返回“POST SUCCEED”字样，并且该网页只接受HTTP请求方法“POST”



### 参考资料

1. [Flask中文文档](https://dormousehole.readthedocs.io/en/latest/)（本次作业主要用到“快速上手”章节的“路由”小节）
2. [Flask宝藏学习网站](http://www.pythondoc.com/)
3. [HTTP请求方法](https://www.cnblogs.com/weibanggang/p/9454581.html)



### 提交方式

- 将py文件提交给自己的小老师



### 截止日期

- 2.17 24:00（暂定）