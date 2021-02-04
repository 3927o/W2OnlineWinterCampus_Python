# Problem1
year = input("Please enter a year: ")
year = int(year)

if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:  # 闰年判定条件请自行百度
    print("yes")
else:
    print("no")

# Problem2
length = int(input("Please enter the length of the list: "))
li = [input("Please enter one of the value of the list: ") for i in range(length)]
cnt_need_iter = length  # 还未遍历的元素个数
while cnt_need_iter:
    i = len(li) - cnt_need_iter
    if li[i].isdigit():  # 判断li[i]是否为整数
        li[i] = int(li[i])
    else:
        li.remove(li[i])  # 从列表删除元素后列表长度会相应减少
    cnt_need_iter -= 1
print(sum(li))

# Problem3
string = input("Please enter a string: ")
d = dict()
for i in range(len(string)):
    d[i] = string[i]
print(d)

# Problem4
li = input("Please enter a list(using ',' to separate different elements): ")
li = li.split(",")
len_li = len(li)

# 将列表中的元素从字符串转化为整形
for i in range(len_li):
    li[i] = int(li[i])

# 选择排序
for i in range(len_li-1):
    min_index = i
    for j in range(i+1, len_li):
        if li[j] < li[min_index]:
            min_index = j
    li[i], li[min_index] = li[min_index], li[i]
print(li)
