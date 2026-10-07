# 类方法和静态方法
'''from datetime import datetime
class Person:
    # 通过@classmethod修饰的方法就是类方法
    @classmethod
    def class_method(cls):
        print('this is a class method')
    # 通过@staticmethod修饰的方法就是静态方法
    # 只是单纯的定义在类中，不收到参数，只收到自定义参数
    # 内部不会访问任何的类和实例的内容
    # 静态方法用于定义与类相关的工具方法
    @staticmethod
    def is_adult(year):
        # 获取当前年份
        current_year = datetime.now().year
        return (current_year - year) >= 18
    @staticmethod
    def mask_idcard(idcard):
        return idcard[:6] + '*' * 8 + idcard[-4:]
# 静态方法保存在类上 所以直接类.静态方法调用
print(Person.is_adult(1998))
print(Person.mask_idcard('141023199805150012'))

# 通过类的实例也能调用到这个静态方法，但是不推荐'''
from shiboken6.Shiboken import Object

# 继承
'''class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def speak(self):
        print(f"my name is {self.name}")

class Student(Person):
    def __init__(self,name,age,gender,identity):
        super().__init__(name,age,gender)
        self.identity = identity
    # 方法重写
    def speak(self):
        print("this is method of son class")

s = Student('hank',29,'male','student')
s.speak()
print(Student.__dict__)'''


# 两个常用方法
'''class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
class Worker:
    def __init__(self,compony):
        self.compony = compony

class Student(Person,Worker):
    def __init__(self,name,age,gender,compony,identity):
        Person.__init__(self,name,age,gender)
        Worker.__init__(self,compony)
        self.identity = identity
# isinstance(instance,class) 判断某个对象是否为指定类或其子类的实例
s = Student('name',29,'male','mcdonald','student')
print(isinstance(s, Person))
# issubclass(class1,class2) 判断某个类是否是另一个类的子类
print(issubclass(Student, Person))

# __mro__ 用来记录属性和方法的查找顺序
print(Student.__mro__)'''

# 三种访问权限
'''class Person:
    def  __init__(self,name,age,gender):
        self.name = name # 公有属性，当前类，子类，类的外部都可以访问
        self._age = age # 受保护的属性，当前类，子类中可以访问
        self.__gender = gender # 私有属性，只有当前类中可以访问
    def inner_class(self):
        print(self.name,self._age,self.__gender)
class Student(Person):
    def __init__(self,name,age,gender,identity):
        super().__init__(name,age,gender)
        self.identity = identity
    def inner_son_class(self):
        # 只能访问到name和age gender是私有属性所以子类中访问不到
        print(self.name,self._age)

p = Person('hank',29,'male')
print(p.name,p._age)'''

# getter & setter
'''class Person:
    def __init__(self,name,age,gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
    # 注册name属性的getter方法，当访问Person实例的name属性时，就会自动调用以下方法
    @property
    def name(self):
        return self.__name
    # 注册name属性的setter方法，当Person的实例需要修改name属性时，就会自动调用以下方法
    @name.setter
    def name(self,value):
        self.__name = value
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        self.__age = value
    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self,value):
        self.__gender = value
    
p1 = Person('hank',18,'male')
p1.name = 'miller'
print(p1.name)'''

# 魔法方法
"""# 以__xxx__命名的特殊方法就是魔法方法
# 不需要手动调用，只需要定义好，py在特定场景下会自动调用
class Person:
    def __init__(self,name,age,gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    # 当执行print(Person的实例对象)或str(Person的实例对象)时调用以下方法
    def __str__(self):
        return f"'name':{self.__name},'age':{self.__age},'gender':{self.__gender}"
    # 以下是常用的魔法方法
    # 调用len(类的实例对象)
    '''def __len__(self):
        return len(self)'''

    # 当执行 对象1 < 对象2 时
    '''def __lt__(self, other):
        return self < other'''

    # 当执行 对象1 > 对象2 时
    '''def __gt__(self, other):
        return self > other'''

    # 当执行 对象1 == 对象2 时
    '''def __eq__(self, other):
        return self == other'''

    # 当访问不存在的属性时
    '''def __getattr__(self,attribute):
        if attribute in self:
            return True
        else:
            return False'''

p1 = Person("hank",18,'male')
print(str(p1))"""

# object类
# 在py中 所有的类都继承了object类，它是所有类的顶层父类
class Person:
    def __init__(self,name):
        self.name = name
# 验证 所有的类都继承了object类
print(issubclass(Person, object))  # True
print(issubclass(int, object))  # True
print(issubclass(float, object))  # True
print(issubclass(tuple, object))  # True
print(issubclass(list, object))  # True
print(issubclass(dict, object))  # True
print(issubclass(str, object))  # True

