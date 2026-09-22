# 一共三个关卡，答对进入下一关，三关通过挑战成功
# 1. 每道题三次答题机会，三次答错则失败
# 2. 输入为空，重新作答，不计入答题机会
# 3. 输入q，直接结束
first_question = 'how are you?'
second_question = 'do you love me?'
third_question = 'am i love you?'
first_answer = 'your lover'
second_answer = 'yes'
third_answer = 'yes'
answer = ''
quit_flag = False
for i in range(3):
    if quit_flag:
        break
    if i == 0:
        for j in range(3):
            print(first_question)
            answer = input()
            if answer == 'q':
                quit_flag == True
                break
            elif answer == first_answer:
                break
            else:
                if j == 3:
                    print("you are failed")
                    quit_flag = True
                    break
                print(f"there are {3 - j} more chances left")
                continue
    elif i == 1:
        for j in range(3):
            print(second_question)
            answer = input()
            if answer == 'q':
                quit_flag == True
                break
            elif answer == second_answer:
                break
            else:
                if j == 3:
                    print("you are failed")
                    quit_flag = True
                    break
                print(f"there are {3 - j} more chances left")
                continue
    else:
        for j in range(3):
            print(third_question)
            answer = input()
            if answer == 'q':
                quit_flag = True
                break
            elif answer == third_answer:
                break
            else:
                if j == 3:
                    print("you are failed")
                    quit_flag = True
                    break
                print(f"there are {3 - j} more chances left")
                continue
if not quit_flag:
    print("congratulation!! you are winner!!")