"""函数"""


# ! 函数的基本使用
# 函数定义
"""
def welcome():
    print("welcome to python world!")
    print("hank miller")
"""
# 函数调用
# welcome()

# todo 参数的使用
# 基本使用
"""
def order(num, dish):
    print(f"your order is {num} {dish}")
order(3,"cola")
"""

# todo 关键字参数 调用时使用形参=实参的形式调用 优势是可以乱序传入
"""
def order(num, dish):
    print(f"your order is {num} {dish}")

order(num=3, dish="cola")
"""

# todo 限制传参的方式
# 通过 / * 分割形参来达到 /前只能使用位置参数 *后使用关键字参数的形式
"""
def order(num,/,dish):
    print(f"your order is {num} {dish}")
    
order(1,dish=3)
"""

# todo 参数默认值
# 如果调用函数时没有传入实参则默认值参数使用默认值
# 如果传入实参则使用实参
"""
def order(num, dish,msg="welcome to dragon restaurant"):
    print(f"your order is {num} {dish}")
    print(msg)
order(3,"cola",'123')
"""

# todo 可变参数
"""
# 以下两种可变参数可以一起使用，但是必须把可变位置参数写在前面
# 同样的，两种可变参数可以和其他参数同时使用
# 可变位置参数
def test01(*args):
    print(args)
test01(1,2,3,4)

# 可变关键字参数 调用时必须使用关键字参数调用
def test02(**kwargs):
    print(kwargs)
test02(a=1,b=2,c=3,d=4,e=5)
"""

# todo 一个特殊的字面量 None

# todo 函数的返回值
# 函数执行结束之后返回给调用者的值就是函数的返回值，没有返回值就是返回None

# todo 简单的递归
# 输出n个hello
"""
def welcome(n):
    if n > 1:
        welcome(n - 1)
    print(f"hello {n}")
welcome(10)
"""
# 小案例 使用递归求n的阶乘
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n
print(factorial(5))
"""
# 小案例 使用递归解决爬台阶的问题
"""
def to_bar(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n ==3:
        return 3
    else:
        return to_bar(n - 1) + to_bar(n - 2)
print(to_bar(5))
"""

# todo 函数的说明文档
"""
def func1(a,b):
    '''接受两个参数a,b，返回二者相加的结果'''
    return a + b
print(func1(1, 2))
"""











