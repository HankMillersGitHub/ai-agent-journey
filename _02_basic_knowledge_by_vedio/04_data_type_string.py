"""专注于string类型的文件"""
# 以下两个字符串等价，都不能直接换行，因为单引号简单，所以用的较多
# message1 = 'this is first string'
# message2 = "this is second string"
# 三个单/双引号既可以作为可换行字符串使用，也可以作为注释使用
# message3 = '''this is third string'''
# message4 = """this is forth string"""


# ! 字符串的格式化输出
# region
# name = 'hank'
# age = 18
# gender = 'man'
# weight = 75.0
# todo 第一种写法 直接使用+拼接
# info1 = "my name is " + name + ",i am " + str(age) + " years old,i am a " + gender + " and my weight is " + str(weight)
# print(info1)

# todo 第二种写法 使用占位符
# ? %s占位string %f占位float %i占位int %d占位decimal %s相对万能
# info2 = "my name is %s,i am %d years old,i am a %s, my weight is %f" % (name,age,gender,weight)
# print(info2)

# todo 第三种写法 使用f-string (format-string) 格式化字符串
# info3 = f"my name is {name},i am {age} years old,i am a {gender}, my weight is {weight}"
# print(info3)
# endregion


# ! 转义字符
# region
# print('python中可以使用\'包裹一个字符串')
# print('python中也可以使用\"包裹一个字符串')
# print('注册会员需要如下信息:\n姓名\n年龄\n手机号')
# print('C:\\project\\workspace')
# print('hello\b')  # 删除\b之前的一个字符
# print('\r')  # 让光标回到本行开头，覆盖输出
# print('\t')  # 一个水平制表符
# endregion

# ! 数据类型转换
# region
# 转字符串 str() 任何类型都能转为str类型
a = 111
print(type(str(a)))
# 转整数 int()
b = '111'
print(type(int(b)))
# 转浮点数 float()
c = 111
print(type(float(c)))
# endregion
