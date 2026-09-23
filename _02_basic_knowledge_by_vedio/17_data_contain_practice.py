# case1 : fruit list
"""fruits  = {
    'apple':18,
    'banana':17,
    'pear':29
}
# print all fruit name
for key in fruits.keys():
    print(key)
# find the most expensive fruit
# here is my function
'''prices = fruits.values()
expensive = max(prices)
for key in fruits.keys():
    if fruits[key] == expensive:
        print(key)'''
# here is simple function
# 以下写法的解释：想比较value值 然后获取key
expensive = max(fruits,key=fruits.get)
print(f'the most expensive is {expensive}')"""

# case2 : student scores
students = [
    {"name":'hank','age':19,'score':{"english":97,"math":97,"chinese":19}},
    {"name":'miller','age':19,'score':{"english":97,"math":97,"chinese":18}},
    {"name":'white','age':19,'score':{"english":97,"math":97,"chinese":79}}
]
# calculate average score
for i in students:
    i['sum_score'] = sum(i.get('score').values())
    i['average'] = i['sum_score'] / len(i.get('score').values())
# find max score student
sum_scores = []
for i in students:
    sum_scores.append(i.get('sum_score'))
print(max(sum_scores,students['sum_score']))