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
'''students = [
    {"name":'hank','age':19,'scores':{"english":97,"math":97,"chinese":19}},
    {"name":'miller','age':19,'scores':{"english":97,"math":97,"chinese":18}},
    {"name":'white','age':19,'scores':{"english":97,"math":97,"chinese":79}}
    ,{"name":'candy','age':19,'scores':{"english":97,"math":97,"chinese":79}}
]
# calculate average score
for stu in students:
    # 获取当前学生的成绩列表
    score_list = stu['scores'].values()
    # 计算平均值
    avg = sum(score_list) / len(score_list)
    print(f'{stu.get("name")}的平均成绩是：{avg}')

# calculator max score
def find_the_max_score(s):
    # 记录总分最高的学生
    max_score_student = []
    # 记录最高分
    max_score = 0
    # 循环遍历
    for stu in s:
        sum_score = sum(stu.get('scores').values())
        if(max_score < sum_score):
            max_score = sum_score
            max_score_student = [stu['name']]
        elif max_score == sum_score:
            max_score_student.append(stu['name'])

    return max_score_student


print(find_the_max_score(students))'''

# case3 : 处理评论内容
'''comment = '这家奶茶真好喝，环境也不错，就是价格有点贵，好喝好喝好喝！！强烈推荐！'
# 统计 好喝 出现的次数
print(comment.count('好喝'))
# 将字符串中的贵替换为略高
print(comment.replace('贵', '略高'))
# 是否包含推荐两字
print(comment.index("推荐"))'''