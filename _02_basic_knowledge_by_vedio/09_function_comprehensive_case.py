"""
根据用户输入的挑战项目和挑战时间
每天收集用户完成的数量
最终统计成为总结
"""
def summarized(s,f,c):
    """用来总结用户的健身表现,接受三个参数，sport，fate,count"""
    print(f"【{s}】【{f}】summarize")
    print(f"total:{c},average:{c / f}")
    print("🎉congratulation！challenge complete！！")
# 从键盘接受用户的输入
# 表示用户要进行练习的运动项目
sport = input("please input your choice:")
# 表示用户要坚持的天数
fate = int(input("please input your fate:"))
print(f"【{sport}】【{fate} days】👊CHALLENGE(please enter your quantity):")
# 表示最终做的总数
count = 0
for i in range(fate):
    count += int(input(f"the {i + 1} day:"))

summarized(sport,fate,count)







