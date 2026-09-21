# ! attention! 所有的非只读函数调用，都是原地操作，除非特殊声明，不会创建新的数据结构

# 元组
# region
# 元组tuple
# python中任何类型对象的一个一维、固定长度，不可变的序列
# 创建元组的两种方式
# create tuple by two method
# tup1 = 4,5,6  # (4,5,6)
# tup1 = (6,7,8) # (6,7,8)
# 创建嵌套元组
# create nested tuple
# tup1 = (1,2,3),(4,5) # ((1,2,3),(4,5))
# 将序列或迭代器转化为元组
# tup2 = tuple([1,2,3])
# 连接元组
# print(tup1 + tup2)
# a,b,c = tup2 # a = 1 , b = 2 , c = 3
# * 元组的好用法(交换元素位置)
# a = 1
# b = 2
# a , b = b , a
# endregion

# 列表
# region
# list 是py中任何类型对象的一个一维、非定长、可变序列
# 创建列表
# list1 = [1,'2',3,True]
# list2 = list((4,2,3)) # 从元组转换
# 连接列表
# 使用 + 对列表进行连接会有比较大的开支，这个过程中会产生一个新的列表，然后才复制对象，所以推荐使用extend进行连接
# print(list1 + list2) # [1,'2',3,True,1,2,3]
# list1.extend(list2)
# print(list1) # [1,'2',3,True,1,2,3]
# insert相较于append开支更大 所以除非特殊情况 否则推荐使用append
# 追加到列表末尾
# list1.append('a')
# print(list1) # [1, '2', 3, True, 'a']
# 插入到指定位置
# list1.insert(1,'a')
# print(list1) # [1,'a','2',3,True]
# 删除指定位置的元素
# list1.pop() # 不传参数默认弹出最后一个元素
# print(list1) # [1,'2',3]
# list1.pop(1)
# print(list1) # [1,3]
# 移除列表的第一个值 使用的参数必须存在于list中并且必须为第一个参数
# list1.remove(1)
# print(list1) # ['2',3,True]
# 判断某元素是否存在于list中
# 在列表中检查是否包含一个元素会比在字典和集合中慢很多，因为前者需要遍历即线性扫描，后者基于哈希表，只需要花费常数时间
# print(1 in list1) # True
# 对列表排序
# list2.sort()
# print(list2) # [2,3,4]
# 按照特定方式排序
# list2.sort(reverse=True) # 倒序
# print(list2) # [4,3,2]
# list3 = ["Apple","Banana","Pear","Beach"]
# list3.sort(key=len) # 按照字符串长度排序
# print(list3)
# list3.sort(key= lambda x: x[1]) # 按照字符串中的第1个元素排序
# print(list3) # ['Banana', 'Pear', 'Beach', 'Apple']
# endregion

# 内置序列处理方式
# region
# 1. 内置的bisect模块
#     此模块中的函数不会检查列表是否被排序好，因为比较消耗时间，所以对未排序的列表使用也不会报错，但是可能返回不正确的结果
# import bisect
# 对一个有序列表进行二分查找或插入
# bisect.bisect找到元素在列表中的位置
# list1 = list(range(10))
# print(bisect.bisect(list1,3)) # 4
# bisect.insort将元素插入到指定位置
# bisect.insort(list1,3.5)
# print(list1) # [0, 1, 2, 3, 3.5, 4, 5, 6, 7, 8, 9]
# 2. 针对序列类型的切片
#   包含str、array、tuple、list等
#   用法：list[[start] : [stop] : [step]]
#   返回包含start位置不包含stop位置的list
# list1 = [1,2,3,4,5]
# print(list1[:]) # [1,2,3,4,5]
# print(list1[:1]) # [1]
# print(list1[::2])   # [1,3,5]
# print(list1[::-1]) # [5,4,3,2,1] 反转
# endregion

# 字典 dict hashtable
# region
# 常见报错
# 键不存在，keyError Exception
# 键不存在，get如果不提供默认值返回None
# 以相同的顺序返回键列表和值列表，但顺序不是特定的，也就是说极大可能非排序。
# 有效的字典键的类型都是可哈希的 可以用函数hash()来检查一个对象是否可哈希
# 创建字典
# dict1 = {"key1":None,"key2":"value2"}
# 从序列创建字典
# keyList = [1,2,3]
# valueList = [4,5,6]
# print(dict(zip(keyList, valueList))) # {1:4,2:5,3:6}
# 获取/设置/插入元素
# print(dict1["key1"]) # value1
# dict1["key2"] = ["value1","value2"] # 如果键不存在 就创建一个键
# print(dict1["key2"])
# get 提供键不存在时的默认值
# print(dict1.get("key3","DefaultValue"))
# 检查键是否存在
# print("key3" in dict1)
# 获取键的列表
# print(dict1.keys())
# 获取值的列表
# print(dict1.values())
# 更新值
# dict2 = dict(zip(valueList,keyList))
# dict1.update(dict2) # 将dict1的值换成dict2的值
# print(dict2)
# endregion

# 集合 set
# region
# 无序且唯一的元素的聚集 像一个只有键的字典
# 创建集合
# set1 = {1, 2, 3, 4, 3} # {1,2,3,4}
# set1_son = {1,2}
# set2 = set([23,23,23,41,41,12]) # {23,41,12}
# 子集测试
# print(set1_son.issubset(set1)) # 子集.issubset(父集)
# 超集测试
# print(set1.issuperset(set1_son)) # true
# 测试集合元素是否相同
# print(set1 == set1_son) # False
# 集合操作
# 交集
# print(set1 & set2) # set()
# 并集
# print(set1 | set2) # {1,2,3,4,23,41,12}
# 差集
# print(set1 - set1_son) # {3,4}
# 异或 各自只属于两个集合的元素集合
# print(set1 ^ set1_son) # {3,4}
# endregion