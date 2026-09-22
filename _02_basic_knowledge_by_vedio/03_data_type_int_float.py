"""关于数据类型的学习"""
import sys

# 使用 type(x) 返回 x 的数据类型
# print(type("a"))

# py中的变量没有数据类型， type(variable) 这里的variable其实是变量的值


# 整型
# age = 18
# temp = -15
# score = 0

# 当一个数字很大的时候，可以使用下划线将数字分组，来让数字变得更加易读
# salary = 300_000
# house_price = 3_200_000
# graduates = 12_000_000
# print(salary)

# py中整数的上限，取决于执行代码的计算机的内存和处理能力
# a = 9 ** 9999
# b = a + 100
# sys.set_int_max_str_digits(0) # 不限制print函数的位数
# print(a)


# 浮点型
# weight = 75.2
# balance = 1231.123
# print(type(weight))
# print(type(balance))

# 浮点型的科学计数法表示
# speed_of_sound = 3.4e+2  # 表示3.4 * 10^2
# print(speed_of_sound)
# humans_of_earth = 8e9  # 表示8 * 10^9
# print(humans_of_earth)
# distance_sun_earth = 1.496E8
# print(distance_sun_earth)
# speed_of_light = 2.998E+8
# print(speed_of_light)
# one_ml = 1e-3  # 表示1的-3次
# one_mg = 1E-3
# print(one_ml)
# print(one_mg)