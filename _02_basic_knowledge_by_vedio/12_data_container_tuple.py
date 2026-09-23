# ! 元组 tuple
# 是一种和列表类似的数据容器，元组中的元素不可修改
"""tuple1 = (1,2,3,4,[1,1,1])
tuple1[4][0] = 0
print(tuple1)"""
# 如果定义只有一个元素的元组也要写逗号
# tuple2 = (11,)

# * 元组的常用方法
# tuple1 = (1,2,3,4)
# index 返回指定元素在元组中第一次出现的索引
# print(tuple1.index(3))
# count 返回指定元素在元组中出现的次数
# print(tuple1.count(3))

# * 元组的常用内置函数
# region
# tuple3 = (4,1,5,6,2,7)
# max 返回元组中的最大值
# print(max(tuple3))
# min 返回元组中的最小值
# print(min(tuple3))
# len 返回元组的长度
# print(len(tuple3))
# sorted 返回排序后的列表 如果一定要使用元组，用tuple转为元组
# print(tuple(sorted(tuple3,reverse=True)))
# sum 返回元组所有元素的和
# print(sum(tuple3))
# endregion

# ! 实际开发中 一般在可变参数的位置使用元组
"""def test(*args):
    print(type(args),args)
test(1,2,3,4) # <class 'tuple'> (1, 2, 3, 4)"""

# * 元组的遍历
"""tuple4 = (1,2,3,4,5,6)
# while
index = 0
while index < len(tuple4):
    print(tuple4[index])
    index += 1
    
# for
for i in tuple4:
    print(i)"""

# * 函数的解包列表或元组传参
"""def test(*data):
    print(data)

list1 = [1,2,3]
tuple1 = (4,5,6)
# 以下是正常的调用
test(list1)
test(tuple1)
# 以下是解包后调用
test(*list1)
test(*tuple1)"""

# ! 元组的总结
"""
1. 元组可以存放不同类型的元素
2. 元素是有序存储的
3. 元组中的元素允许重复
4. 元素不许修改
5. 元组的长度在定义好以后就是不可变的
"""