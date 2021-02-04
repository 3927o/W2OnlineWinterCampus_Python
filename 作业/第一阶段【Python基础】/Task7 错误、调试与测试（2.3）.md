# Task7 错误、调试与测试（2.3）

### 学习目标

- Python错误处理
- Python程序调试的几种方法
- Python的几种程序测试方法



### 学习任务

1. 编写一个函数calu(a, b, op)。要求：

   - op表示加减乘除某一运算，函数要求返回a与b的运算结果

   - 当运算出现错误时，捕获该错误并在控制台输出相关错误信息，输出格式要求如下

   - ```python
     Caught an Exception:
     Exception Type: {错误类型}
     Exception Info: {错误提示信息}
     ```

2. 编写一个函数devide(a, b)，要求：
   
   - 以a为被除数，b为除数，返回a除b的结果
   - 当b为0时，手动抛出异常
   
3. 写一个单元测试来测试你第二题编写的devide函数。测试内容：

   - 测试devide(5, 1)与devide(6, 4)的返回值是否正确
   - 测试devide(5, 0)是否会抛出异常
   - 运行单元测试

4. 为第一题的calu函数编写一个文档测试，测试内容：

   - ```bash
     >>> calu(1, 2, "+")
     3
     >>> calu(1, 2, "-")
     -1
     >>> calu(1, 2, "*")
     2
     >>> calu(1, 2, "/")
     0.5
     >>> calu(1, 0, "+")
     Caught an Exception:
     Exception Type: ZreoDivisionError
     Exception Info: division by zero
     ```

   - 运行程序，确保测试成功



### 参考资料

- [廖雪峰Python教程之【错误、调试和测试】](https://www.liaoxuefeng.com/wiki/1016959663602400/1017598814713792)
- 百度
- BiliBili
- 小师傅
- 我



### 提交方式

- 将以上题目放到一个.py文件中并交给自己的小师傅（或者以小师傅要求的其他形式提交）



### 截止日期

- 2.3 24:00（暂定）