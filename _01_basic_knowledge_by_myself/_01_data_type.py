# 查看变量的数据类型： type(variable)

# int / long 过大的int类型会自动转换为long类型 py3中已经删除了long类型
# num1 = 1000000000000000000000000000000010000000000000000000000000000000100000000000000000000000000000001000000000000000000000000000000010000000000000000000000000000000
# print(type(num1))


# float 64位浮点类型
# num2 = 1.123
# print(type(num2))


# bool 真值和假值
# truthNum = True
# falseNum = False


# str py2中的字符串默认ASCII编码 py3中的默认Unicode编码
# str类型的字符串可以置于单/双/三引号中
# str字符串是字符组成的序列，因此可以像处理其他序列一样处理str

# 特殊字符可以通过\或前缀r实现,前缀r用来让\不再作为转义字符使用 如下：
# str1 = r'this\f?ff'
# str2 = 'this\f?ff'
# print(str1)
# print(str2)

# 字符串可以通过多种方式格式化
# template = '%.2f %s haha $%d'
# str1 = template % (4.889,'hola',2)
# print(str1)


# NonType(None) python中的null值 None对象只存在一个实例
# None不是一个关键字，而是NoneType的唯一实例
# None通常是可选函数参数的默认值
# def func1(a,b,c=None):
# None的常见用法： if variable is None:


# from datetime import datetime
# datetime python内置的datetime模块提供了datetime、date以及time类型
# datetime组合了存储于date和time中的信息
# 从字符串创建datetime
# dt1 = datetime.strptime("20260921","%Y%m%d")
# 获取date对象
# print(dt1.date())
# 获取time对象
# print(dt1.time())
# 将datetime格式化为字符串
# print(dt1.strftime("%m/%d/%Y %H:%M"))
# 更改字段值
# dt2 = dt1.replace(minute=0,second=30)
# 做差 如果用靠前的时间减去靠后的时间 会显示负天数 正时间
# diff = dt1 - dt2
# print(diff)

# ! 注意： str bool int 和 float同时也是显示类型转换函数
# a = 10
# print(float(a)) # 输出为10.0