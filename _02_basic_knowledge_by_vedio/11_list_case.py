"""
实现一个成绩统计程序，可以对多名学生的成绩进行统计和分析
用户可以连续输入学生成绩，直到用户输入end结束
要求可以统计：总人数，最高分，最低分，合格人数，合格率，优秀人数，优秀率平均分
"""
from numpy.ma.extras import average

def total_number_of_people(people_list):
    """
        :param people_list[]
        :return int
    """
    return len(people_list)

def max_score(people_list):
    """
    :param people_list:
    :return int
    """
    return max(people_list)

def min_score(people_list):
    """
    :param people_list:
    :return: int
    """
    return min(people_list)

def number_of_qualified_people(people_list):
    """
    :param people_list:
    :return: int
    """
    count = 0
    for score in people_list:
        if score > 60:
            count += 1
    return count

def qualification_rate(people_list):
    """
    :param people_list:
    :return:  string
    """
    rate = number_of_qualified_people(people_list) / len(people_list)

    return f"{rate * 100}%"

def number_of_excellent_people(people_list):
    """
    :param people_list:
    :return: int
    """
    count = 0
    for people in people_list:
        if people > 90:
            count += 1
    return count

def excellence_rate(people_list):
    """
    :param people_list:
    :return: string
    """
    rate = number_of_excellent_people(people_list) / len(people_list)
    return f"{rate * 100}%"

def average_score(people_list):
    """
    :param people_list:
    :return: float
    """
    return average(people_list)

def menu():
    print("1. 添加学生")
    print("2. 总人数")
    print("3. 最高分")
    print("4. 最低分")
    print("5. 合格人数")
    print("6. 合格率")
    print("7. 优秀人数")
    print("8. 优秀率")
    print("9. 平均分")

student_list = []
while True:
    menu()
    function_choice = int(input("please input your choice:"))
    if function_choice == 1:
        while True:
            user_input = input("please input student score")
            if user_input == "end":
                break
            else:
                student_list.append(int(user_input))
    elif function_choice ==2:
        print(f"total number of people is {total_number_of_people(student_list)}")
    elif function_choice ==3:
        print(f"the max score is {max_score(student_list)}")
    elif function_choice ==4:
        print(f"the min score is {min_score(student_list)}")
    elif function_choice ==5:
        print(f"number of qualified is {number_of_qualified_people(student_list)}")
    elif function_choice ==6:
        print(f"qualification rate is {qualification_rate(student_list)}")
    elif function_choice ==7:
        print(f"number of excellent is {number_of_excellent_people(student_list)}")
    elif function_choice ==8:
        print(f"excellence rate is  {excellence_rate(student_list)}")
    elif function_choice ==9:
        print(f"average score is {average_score(student_list)}")
    else:
        break
