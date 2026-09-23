# ! 集合 set
# * 集合基础
"""# 集合的特点，集合内部的元素不保证顺序，不能通过索引访问元素，会自动去除重复元素
# 只有不可变的东西才能放入集合
# 定义一个空集合
full_set = set()
# 定义一个空不可变集合
full_frozenset = frozenset()
# 可变集合 set
set1 = {1,2,3,4,5}
print(set1)
# 不可变集合 frozenset frozenset()接受的参数可以是任何可迭代对象，但是返回的一定是不可变集合
frozenset1 = frozenset({6,7,8,9,0})
print(frozenset1)"""

# * 集合的增删改查
"""set1 = {1,2,3,4,5,6}
# 增
# 集合.add(元素) 向集合中添加元素，没有返回值
set1.add(7)
print(set1)
# 集合.update(可迭代对象),向集合中批量添加元素
set1.update([8,9,0])
print(set1)

# 删
# 1. 集合.remove(元素) 从集合中删除指定元素，如果指定元素不存在会报错
set1.remove(1)
print(set1)
# 2. 集合.discard(元素) 从集合中删除指定元素，如果指定元素不存在不报错
set1.discard(2)
print(set1)
# 3. 集合.pop() 从集合中移除一个任意元素，返回被移除的元素
print(set1.pop())
# 4. 集合.clear() 清空集合
set1.clear()
print(set1)

# 改
# 因为集合的内容是不可变的，所以集合没有专门用于修改内容的方法，但是可以使用remove + add来达到修改的效果
set1.update({1,2,3,4,5,6,7,8,9,0})
set1.remove(9)
set1.add(10)
print(set1)

# 查
# 同样的 因为集合没有索引，也不支持切片，所以不具备按位置访问的能力
# 但是可以使用成员运算符判断某元素在不在集合中
set2 = {1,2,3}
print(1 in set2) # True
print(3 not in set2) # False
"""

# * 集合的常用方法
"""set1 = {1,2,3}
set2 = {3,4,5}
# 集合1.difference(集合2) 返回集合1中不同于集合2的元素
print(set1.difference(set2))
# 集合1.difference_update(集合2) 从集合1中删除集合2中存在的元素，集合1会被改变 集合2不变
set1.difference_update(set2)
print(set1) # {1,2}
print(set2) # {3,4,5}
# 集合1.union(集合2) 返回合并后的集合1 + 集合2
print(set1.union(set2))
# 集合1.issubset(集合2) 判断集合1是不是集合2的子集 返回bool值
print(set1.issubset(set2))
# 集合1.issuperset(集合2) 判断集合1是不是集合2的超集 返回bool值
print(set1.issuperset(set2))
# 集合1.isdisjoint(集合2) 判断集合1和集合2是否没有交集 返回bool值
print(set1.isdisjoint(set2))"""

# * 集合的数学运算
"""set1 = {1,2,3}
set2 = {3,4,5}
# 并集 |
print(set1 | set2)
# 交集 &
print(set1 & set2)
# 差集 -
print(set1 - set2)
# 对称差集 ^
print(set1 ^ set2)"""

# * 集合的遍历
"""# 集合只能使用for循环遍历
set1 = {1,2,3}
for i in set1:
    print(i)"""

# * 集合的特点
"""
1. 集合是无序的，无法通过索引访问
2. 集合内的元素都是不重复的，会自动去重
3. 集合有可变集合set和不可变集合frozenset
4. 集合的元素必须是不可变类型，因为集合的位置是使用元素内容计算出来的hash值
5. 集合支持交并差异或等数学操作
"""