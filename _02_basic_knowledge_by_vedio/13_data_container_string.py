# ! 字符串

# * 字符串的常用方法 都会返回新字符串，不会对原字符串进行修改
"""str1 = "hello world!"
# 1. index 返回指定字符在字符串中第一次出现的位置
print(str1.index('h'))
# 2. split 将字符串按照指定字符进行分割，并返回一个列表
print(str1.split(" "))
# 3. replace 将字符串中的某个字符串片段，替换成目标字符串
print(str1.replace("world", "hank"))
# 4. count 返回指定字符在字符串中出现的次数
print(str1.count('h'))
# 5. strip 从字符串两端开始 删除指定字符串， 一般用于去掉两端空格
# PS: 规则：从字符串两端开始删除，直到遇到第一个不在指定字符串中的字符就停下
print(str1.strip("h"))
print(str1.strip("oleh")) # world!
print(str1.strip()) # 不传参用于去掉空格"""

# * 字符串的常用内置函数
"""str2 = "hello world!"
# 1. len 返回字符串的个数
print(len(str2))
# 2. max 返回字符串中Unicode编码最大的字符
print(max(str2))
# 3. min 返回字符串中unicode编码最小的字符
print(min(str2))
# 4. sorted 返回字符串按Unicode编码排序后的新列表
print(sorted(str2))"""

# ! 序列的切片
"""list1 = [1,2,3,4,5,6,7,8,9,0]
tuple1 = (1,2,3,4,5,6,7,8,9,0)
str1 = "1234567890"
# 切片语法 序列[起始索引:结束索引:步长]
print(list1[0:9:2])
print(tuple1[0:9:2])
print(str1[0:9:2])
# 如果三个参数都没有传 则按照默认[0:len(序列):1]计算
print(list1[::])
print(tuple1[::])
print(str1[::])
# 当起始索引大于结束索引时，步长必须为负数，否则会报错
print(list1[9:0:-2])
print(tuple1[9:0:-2])
print(str1[9:0:-2])
# 特殊的：如果同时省略起始和结束索引，并且步长为负数，python会自动对调默认的起始和结束位置
print(list1[::-1])
print(tuple1[::-1])
print(str1[::-1])"""

# ! 序列的相加和相乘
# 相加 只有两个同类型的序列才能相加
list1 = [1,2,3]
list2 = [4,5,6]
tuple1 = (1,2,3)
tuple2 = (4,5,6)
str1 = "123"
str2 = "456"
print(list1 + list2)
print(tuple1 + tuple2)
print(str1 + str2)
# 序列相乘 只能乘以整数 意味着列表重复n次
print(list1 * 3)
print(tuple1 * 3)
print(str1 * 3)











