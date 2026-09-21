# 函数参数传递使用的是引用传递
# 基本形式是
# def func1(posArg1,keywordArg=1,....)
# attention ! 关键字参数必须跟在位置参数之后
# 使用函数时  如果只有函数名没有括号表示该函数对象本身
#           如果有函数名() 表示调用该函数
# 函数可以作为参数进行传递 例如：
# def calculator(a,b,func):
#     return func(a,b)
# def sum(a,b):
#     return a + b
# def sub(a,b):
#     return a - b
# def multiply(a,b):
#     return a * b
# def division(a,b):
#     if b == 0:
#         return None
#     else:
#         return a / b
# print(calculator(1, 2, division))

# 函数的返回值，如果没有返回值 那该函数的返回值就是none 如果有多个则返回由返回值组成的元组

# 匿名函数 lambda函数
# region
# 只包含一条语句的而简单函数
# 以下二者等价
# lambda a,b: a + b
# def func1(a,b): return a + b
# 匿名函数的应用
# def add(a,b): return a + b
# def add(a):
#     def inner(b):
#         return b + a
#     return inner
# add2 = lambda a : lambda b: a + b
# print(add(4)(3))
# print(add2(4)(3))
# def addT(a):
#     def inner1(b):
#         def inner2(c):
#             return a + b + c
#         return inner2
#     return inner1
# print(addT(1)(2)(3))
# add3 = lambda a :lambda b : lambda c : a + b + c
# print(add3(2)(4)(5))
# endregion

# 一些有用的函数
# 1. Enumerate 返回一个序列(i,value)的元组，i是当前item的索引
list1 = [1,2,3,4]
# for i,value in enumerate(list1):
#     print(i,value)
# 上下两段等价
# i = 0
# for value in list1:
#     print(i,value)
#     i += 1
# enumerate应用 创建值 -> 索引的字典映射
# list2 = ["apple","banana","pear"]
# value_to_index = {value:i for i ,value in enumerate(list2)}
# print(value_to_index)

# 2. sorted 从任意序列返回一个排序好的序列、
# list1 = [2,4,1,5,2,6]
# print(sorted(list1))
# 应用 返回一个字符串排序后的无重复字母序列
# print(sorted(set('abc cba')))

# 3. zip 把列表元组或者其他序列的元素配对组合成元组 大小取决于短序列的长度
# set1 = (1,2)
# list1 = [4,5,6]
# dict1 = {1:3,2:4}
# tuple1 = zip(set1, list1,dict1.items())
# print(tuple1)
# for i in tuple1:
#     print(i)
#
# set2 = ((1,2),(3,4))
# a,b = zip(*set2)
# print(a)
# print(b)

# 4. reversed 将一个序列逆序迭代
# reversed函数返回逆序 list格式化为一个列表
# print(list(reversed(range(10))))











