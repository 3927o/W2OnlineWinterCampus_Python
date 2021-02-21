# Task11 操作请求数据(2.21)

- ### 学习目标

  - flask.request

  

  ### 学习任务

  1. 请设计一个网站，要求如下
     1. 当访问URL"http://127.0.0.1:5000/get_form_data"时，网页显示POST请求的表单数据。（request.form）
     2. 当访问URL"http://127.0.0.1:5000/get_args/"时，网页显示URL中的查询字符串（request.args）
     3. 当访问URL"http://127.0.0.1:5000/get_request_info/"时，网页显示当前请求的请求路径及请求方法
     4. 当以POST方法访问URL"http://127.0.0.1:5000/upload_file"时，将请求文件“the_file”保存。（request.files）
     5. 当访问URL"http://127.0.0.1/get_cookies"时，网页返回请求的cookies信息。（request.cookies）

  

  ### 参考资料

  1. [Flask中文文档](https://dormousehole.readthedocs.io/en/latest/)（本次作业主要用到“快速上手”章节的“操作请求数据”小节）
  2. [Flask宝藏学习网站](http://www.pythondoc.com/)
  3. [度娘](https://baidu.com)

  

  ### 提交方式

  - 将py文件提交给自己的小老师

  

  ### 截止日期

  - 2.21 24:00（暂定）

  

  ### Tips

  - 在开发环境下建议打开调试模式，即"app.run(debug=True)"