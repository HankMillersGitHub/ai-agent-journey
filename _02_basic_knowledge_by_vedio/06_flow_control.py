"""流程控制语句"""
from pymupdf import planish_line

# ! 输入语句
# 输入语句的返回值都是str类型
# input_number = input("please input your number:")


# ! 分支结构
# region
# todo 单分支结构
# 基于判断的结果决定最后执行的语句
"""
age = 19
if age >= 18:
    print("成年人")
if age < 18:
    print("未成年")
"""
# todo 双分支
"""
age = int(input("please input your age:"))
if age >= 18:
    print("you are adult!")
else:
    print("you are underage")
"""
#  todo 多分支
"""
age = int(input("please input your age:"))
if age < 18 :
    print("you are underage!")
elif age < 30:
    print('you are youth')
elif age < 50:
    print('you are midlife')
else:
    print('you are old-age')
"""

# todo 嵌套分支
"""
age = int(input("please input your age:"))
medical_report = input("please submit your medical report(yes/no):")
membership_level = int(input("please input your membership level(1-3):"))
if 18 <= age <= 45:
    if medical_report == 'yes':
        if membership_level == 1:
            print("you get a t-shirt")
        elif membership_level == 2:
            print("you get a sport-shoes")
        else:
            print("you get a sport-headset")
    else:
        print("you do not have medical report,prohibited from participating in the competition")
else:
    print("you age does not meet the requirements,prohibited from participating in the competition")
"""
# endregion


# ! 循环结构
# region
# todo while
"""
i = 0
while i < 10:
    print(i)
    i += 1
"""
# 小案例
"""
riddle = 'how you are?'
answer = 'your lover'
guess = ''
while guess != answer:
    print(riddle)
    guess = input()
    if guess == answer:
        print("i love you babe")
    else:
        print("fuck you ,you will be dead")
"""

# todo for
"""
for i in range(10):
    print(i)
"""
# 小案例
# 加密 戓爳佢
"""
plaintext = input("please input plaintext:")
ciphertext = ''
for c in plaintext:
    ciphertext += chr(ord(c) + 2)
print(f"the ciphertext is {ciphertext}")
"""
# 解密
"""
ciphertext = input("please input your ciphertext:")
plaintext = ''
for c in ciphertext:
    plaintext += chr(ord(c) - 2)
print(f"the plaintext is {plaintext}")
"""

# todo 对比for和while
"""
while                               for
条件驱动循环                      迭代驱动循环，遍历可迭代对象的每一项
只要条件为True就循环               语法简洁，处理可迭代对象的首选，不容易死循环
写法灵活，适合不确定循环次数的场景    适合一开始就知道循环多少次的场景
需要手动维护循环条件，容易造成死循环
"""

# todo 嵌套循环
"""
for i in range(30):
    print(f"📅today is the {i + 1} day.")
    for j in range(3):
        print(f"🏋️‍this is the {j} set of sit ups i did ")
    print("🎉mission complete!come on!!!")
"""

"""
i = 0
while i < 30:
    print(f"📅today is the {i + 1} day.")
    i += 1
    j = 0
    while j < 3:
        print(f"🏋️‍this is the {j} set of sit ups i did ")
        j += 1
    print("🎉mission complete!come on!!!")
"""

# 小案例 乘法表
for i in range(9):
    j = 0
    while j <= i :
        print(f"{j + 1} * {i + 1} = {(i + 1) * (j + 1)}\t",end='')
        j += 1
    print()