class Person:
    class_attribute = 'this is class attribute'
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    # 自定义方法 给实例添加行为
    # 自定义方法收到的参数是调用这个方法的实例对象 self 之后的是其他参数
    def say_hello(self,msg):
        print(f'my name is {self.name},i said : {msg}')

p = Person('hank',29,'man')
p.say_hello("fuck you!!")
print(f'there is class attribute {Person.class_attribute}')
print(Person.__dict__)



'''

'''