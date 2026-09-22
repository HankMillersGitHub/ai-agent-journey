# ! 列表
# 定义列表
# list1 = [元素1,元素2......]

# todo 列表的常用操作
'''
# list1 = [1,2,3,4,5,6]
# 1. 新增元素
# 1.1 调用列表的append方法
# list1.append(7)
# print(list1)
# 1.2 调用列表的insert方法
# list1.insert(0,0)
# print(list1)
# 1.3 调用列表的extend方法将可迭代对象的内容依次取出，追加到列表的尾部
# list2 = [8,9,10]
# list1.extend(list2)
# print(list1)

# 2. 删除元素
# 2.1 调用列表的pop方法 删除指定位置的元素并返回被删除的元素
# print(list1.pop(0))
# print(list1)
# 2.2 调用列表的remove方法 删除列表中第一次出现的指定值 不存在则报ValueError 无返回值
# print(list1.remove(1))
# print(list1)
# 2.3 调用列表的clear方法 将列表变为空列表
# list2.clear()
# print(list2)
# 2.4 删除指定位置的元素
# del list1[0]
# print(list1)

# 3. 使用索引修改列表指定位置的元素值
# list1[0] = 11
# print(list1)

# 4. 使用索引查询指定位置的列表元素
# print(list1[1])
'''
from operator import ixor

# todo 列表的常用方法
"""
list1 = [8,3,15,1,9,22,7,14,5,11]
# 1. index 查找指定元素在列表中第一次出现的索引，返回该索引
print(list1.index(9))
# 2. count 统计某个元素在列表中出现的次数 返回元素出现的次数
print(list1.count(1))
# 3. reverse 反转列表，会直接将列表反转，无返回值
list1.reverse()
print(list1)
# 4. sort 对列表进行排序 会直接影响原列表 可以传入关键字参数reverse 值为bool值
list1.sort()
print(list1)
"""

# todo 常用的内置函数
"""
list1 = [8,3,15,1,9,22,7,14,5,11]
# 1. sorted(数据容器,reverse=bool) 对给定容器进行排序，返回排序后的新容器
print(sorted(list1))
# 2. len(数据容器) 获取容器中元素的个数，返回元素个数
print(len(list1))
# 3. max(数据容器) 返回容器中或多个值的最大值
print(max(list1))
# 4. min(数据容器) 返回容器中或多个值的最小值
print(min(list1))
# 5. sum(数据容器) 返回容器中所有值的和 这里的容器只能是数值类型的元素
print(sum(list1))
"""

# todo 列表的遍历
scores = [67,24,91,5,48,73,16,88,32,59]
# while遍历
'''
index = 0
while index < len(scores):
    print(scores[index])
    index += 1
'''
# for遍历
# 1. 第一种写法
"""for i in scores:
    print(i)"""
# 2. 第二种写法
"""for i in range(len(scores)):
    print(scores[i])"""
# 3. 第三种写法 这种写法可以同时得到值和索引 或者切片输出
# enumerate 的start参数，可以让计数器从指定值开始(改变的是循环时的编号，不是真正的索引值)
for index,item in enumerate(scores,start=3):
    print(index,item,scores[index])