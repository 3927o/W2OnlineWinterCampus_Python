import math

# Problem1
print(eval("{'name': 'xiaoming'}"))


# Problem2
def 解一元二次方程(a, b, c):
    delta = math.sqrt(b*b - 4*a*c)
    x1 = (-1*b + delta) / 2*a
    x2 = (-1 * b - delta) / 2 * a
    if delta > 0:
        print(f"x1={x1}, x2={x2}")
    elif delta == 0:
        print(f"x={x1}")
    else:
        print("No solution")


# Problem3
def calu(*kwargs, op=0):
    """
    :param kwargs: 待计算的一系列实数
    :param op: 0:加法, 1:减法, 2:乘法, 3:除法
    :return: 计算结果
    """
    ans = 0
    if op == 0:
        for i in kwargs:
            ans += i
    elif op == 1:
        for i in kwargs:
            ans -= i
    elif op == 2:
        ans = 1
        for i in kwargs:
            ans *= i
    elif op == 3:
        ans = kwargs[0]
        kwargs = kwargs[1:]
        for i in kwargs:
            ans /= i
    else:
        print("Wrong parameter")
    print(f"ans is {ans}")
    return ans


# Problem4
def show_info(name, age, **args):
    print(f"name: {name}")
    print(f"age: {age}")
    for key in args:  # 如果看不懂该处的循环语句的话请自行百度"迭代"相关知识
        print(f"{key}: {args[key]}")


解一元二次方程(1, 2, 1)
calu(1, 2, 3, 4)
calu(1, 2, 3, 4, op=1)
calu(1, 2, 3, 4, op=2)
calu(1, 2, 3, 4, op=3)
show_info("lin", 19, school="fzu")
