"""
类就是一个模板，用来描述一类对象应该由那些属性那些方法
"""

# 定义最小简单类
'''# class 是定义类的关键字，类名一般使用大驼峰格式
class Person:
    pass
# 创建最小简单类的实例
p = Person() # 创建实例 这里的p就是Person的实例
print(p) # <__main__.Person object at 0x000001A957C02E40>
'''

# 自定义方法
'''# 在类中定义的函数就是方法，方法的第一个参数通常是self 表示当前调用此方法的实例
class Person:
    def say_hello(self):
        print('hello world!!')
p = Person()
p.say_hello()'''

# 实例属性
'''# 实例属性属于每个实例自己，通常定义在__init__方法中，用self.属性 = 属性值 定义
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
p1 = Person("hank",18,'man')
p2 = Person("miller",37,'female')
# 实例属性是各自独立的
print(p1.name,p1.age,p1.gender)
print(p2.name,p2.age,p2.gender)'''

# 类属性
'''# 类属性定义在方法外 类内 所有实例共享
class Person:
    exemple_class_attribute = 10

# 给类新增类属性
Person.exemple_class_attribute_2 = 20

print(Person.exemple_class_attribute)
print(Person.exemple_class_attribute_2)

# 修改实例的类属性
p = Person()
p.exemple_class_attribute = 99
print(p.exemple_class_attribute)'''

# 实例方法
'''class Person:
    # 在类中定义的普通方法就是实例方法 通过实例.方法调用
    def say_hello(self):
        print("hello world!!")
p = Person()
p.say_hello()'''

# 类方法
'''class Person:
    class_attribute = 10
    # 类方法用@classmethod修饰 第一个参数是cls 表示该类本身
    @classmethod
    def get_attribute_of_class(cls):
        return cls.class_attribute
# 类方法可以通过类调用，也可以通过实例调用，常用于工厂方法
print(Person.get_attribute_of_class())'''

# 静态方法
'''class Person:
    # 静态方法一般用于和类相关，但是不用访问类和类的实例的工具函数
    @staticmethod
    def add(a,b):
        return a + b

print(Person.add(1, 2))'''

# 继承
'''class Person:
    def __init__(self,name):
        self.name = name
    def say_hello(self):
        print(f'my name is {self.name}')

class Student(Person):
    def __init__(self,name,grade):
        # 调用父类的初始化方法进行初始化
        super().__init__(name)
        self.grade = grade
    # 子类中定义和父类同名的方法就会重写父类方法
    def say_hello(self):
        print(f"my name is {self.name}, i'm {self.grade} grade")

s = Student('hank',9)
s.say_hello()'''

# 两个常用方法
'''class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    # __str__  给用户看的字符串
    def __str__(self):
        return f'Person(name={self.name},age={self.age},gender={self.gender})'
    # __repr__ 给开发者看的字符串
    def __repr__(self):
        return f'Person({self.name,self.age,self.gender})'

p = Person('hank',18,'man')
print(repr(p))
print(str(p))
'''

# 多重继承  一个类可以继承多个父类
'''class Animal:
    def __init__(self,animal_type):
        self.animal_type = animal_type
    def say_hello(self):
        print(f"hello i'm a Animal,and i'm belong to {self.animal_type}")

class Dog:
    def __init__(self,name):
        self.name = name
    def say_hello(self):
        print(f"hello i'm a Dog ,and my name is {self.name}")

class Husky(Animal,Dog):
    def __init__(self,name,animal_type,gender,age):
        super().__init__(animal_type)
        super().__init__(name)
        self.gender = gender
        self.age = age

h = Husky('旺财','哈士奇','male',2)
# 调用最近的同名方法
h.say_hello()
# 查看类的继承顺序
print(Husky.mro())'''

# 三种访问权限
class Demo:
    def __init__(self):
        self.public = 'public'
        self._protected = 'protected'
        self.__private = 'private'
    def show(self):
        print(self.__private)

d = Demo()
# print(d.public)
# print(d._protected)
# print(d.__private) # 报错AttributeError
print(d._Demo__private) # private 改成_类名__private才能在外部访问
d.show()