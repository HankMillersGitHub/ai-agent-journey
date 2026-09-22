"""运算符"""

# ! 算术运算符
# region
# + - * /
# // 取整除
# print(3 // 2) # 1
# % 取余
# print(3 % 2) # 1
# ** 乘方
# print(3 ** 3) # 27
# endregion


# ! 赋值运算符和复合赋值运算符
'''
+=      ->      a += x   ~   a = a + x
-=      ->      a -= x   ~   a = a - x
*=      ->      a *= x   ~   a = a * x
/=      ->      a /= x   ~   a = a / x
//=     ->      a //= x  ~   a = a // x
%=      ->      a %= x   ~   a = a % x
**=     ->      a **= x  ~   a = a ** x
'''


# ! 比较运算符
# region
'''
==  等于
!=  不等于
>   大于
<   小于
>=  大于等于
<=  小于等于
以上比较结束返回bool类型 只有True和False
字符串之间进行比较，py会先把字符串变成unicode编码，然后依次比较
如果有如下情况，py会比较字符串的长度
abc < abcde         True
我爱你 < 我爱你中国    True
'''
# 使用ord()查看字符的unicode编码 只能接受一个字符
# print(ord('a'))
# 使用char()将unicode转为字符
# print(chr(98))
# endregion


# ! bool类型
# region
# 只有两个值 True False
# boolean类型是int的子类型，底层使用1表示True，0表示False
# 使用bool()将指定内容转为boolean类型
# py中除0/''/""/None之外的任何值转为bool都为True
# print(bool(None))
# endregion


# ! 逻辑运算符
# region
# and与 or或 not非
"""
and具备短路功能
False and 3 / 0     =>  False 并不会报ZeroDivisionError错
print(False and 3 / 0) => False
and 返回的不一定是bool值，可能是参与计算的值本身
print(100 / 2 and 100 / 4) # 25.0
故而：and会先看左边的值，如果左边值为假，就返回左边的结果，反之返回右边的结果
"""
"""
or 用于判断两侧，至少有一个True(只要有其中一个是True，就是True)
同样的，也具备短路的功能
"""
# endregion







