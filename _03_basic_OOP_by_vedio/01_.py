class Person:
    # 类的初始化方法
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    # 类的自定义方法
    def say_hello(self):
        print(f"my name is {self.name},i'm {self.age} years old,i'm a {self.gender}")

# 创建类的实例对象p
p = Person('hank',28,'man')
# 调用实例的自定义方法
p.say_hello()