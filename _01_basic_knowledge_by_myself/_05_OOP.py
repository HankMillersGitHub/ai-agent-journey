# class FirstObject(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def func1(self,arg1):
#         pass
#     # 静态方法不需要传入self也就是说 如果是对象实例调用 不会将对象实例传进来
#     @staticmethod
#     def classFunc2(arg1):
#         pass
# obj1 = FirstObject("张三",18)
# obj1.func1(19)
# obj1.classFunc2(2)
# FirstObject.classFunc2(2)
# # 返回对象的所有可用方法
# print(dir(obj1))
