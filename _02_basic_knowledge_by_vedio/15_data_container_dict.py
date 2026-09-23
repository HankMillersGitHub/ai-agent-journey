# ! 字典 dict
# 定义字典
'''dict1 = {
    'name':'zhangsan',
    'age':19,
    'gender':'nan'
}'''
# 定义空字典
'''dict2 = {}
dict3 = dict()'''

# * 字典的增上改查
'''student = {"name":"hank","age":29}
# 查
# 1. 使用字典[key]的方式直接取值
print(student['name'])
# 2. 使用字典.get(key)安全取值，如果key不存在则返回默认值或none
print(student.get('age','there is no age'))

# 增
student['gender'] = 'man'
print(student)

# 改
# 1. 修改dict中的某个值和新增该键值对的写法一致
student['gender'] = 'female'
# 2. 批量修改
student.update({'name':'miller','age':89})
print(student)

# 删
# 删除指定key所对应的那一组键值对
del student['gender']
print(student)
# 删除指定key所对应的那一组键值对，返回这个key所对应的值
# pop方法可以设置默认值，当要删除的key不存在时，会返回该默认值
print(student.pop('hobby', 'there is no hobby'))
print(student.pop('age'))
# 清空字典
student.clear()
print(student)'''

# * 字典的常用方法
'''people = {
    'name':'hank',
    'age':18,
    'gender':'man',
    'hobby':['basketball','football','cornball']
}
# keys 获取字典中的所有键 这里返回的结构和列表类似但是不能使用索引访问
print(people.keys())
# values 获取字典中的所有值 这里返回的结构和列表类似但是不能使用索引访问
print(people.values())
# items 获取字典中所有的键值对，每一个键值对以一个元组的形式呈现
print(people.items())
# ? 可以结合list() 将以上三个方法的返回值转为list进行后续处理
'''

# * 字典的循环遍历
'''teacher = {
    'name':'hank',
    'age':18,
    'gender':'man',
    'major':'Math'
}
# 直接遍历字典
for key in teacher:
    print(f"{key} is {teacher[key]}")
# 遍历字典中的key
for key in teacher.keys():
    print(f"{key} is {teacher[key]}")'''

# * 字典的特点
'''
1. 字典是键值对形式的数据
2. 字典中的键是唯一的
3. 字典中的键是不可变类型(数字、字符串、元组等)
4. 不能使用索引
5. 支持增删改查，支持for循环
'''

