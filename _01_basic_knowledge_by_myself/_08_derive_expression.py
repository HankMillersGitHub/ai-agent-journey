# 推导表达式是一种能让代码更易读易写的语法糖
# 1. 列表推导
# list1 = [1,2,3,4]
# result = [i * 2 for i in list1] # 对列表进行统一处理
# 上下二者等价
# for i in list1:
#     i = i * 2
# result1 = [i for i in list1 if i % 2 == 0] # 对列表进行过滤
# 上下二者等价
# for j in list1:
#     if j % 2 == 0:
#         result1.append(j)
# print(result)
# print(result1)

# 2. 字典推导
# dict1 = {1:1,2:2,3:3}
# dict2 = {
#     "name":"hank",
#     "age":18
# }
# result = {key:value for key,value in dict2.items()}
# print(result)

# 3. 集合推导
# set1 = {1,2,3,4}
# result1 = {i * 2 for i in set1}
# print(result1)
# for i in result1:
#     print(i)

# 4. 嵌套列表
out = [1,2,3,4]
inner = [5,6,7,8]
result = [i * j for i in out if i <= 3 for j in inner if j % 2 == 0]
print(result)