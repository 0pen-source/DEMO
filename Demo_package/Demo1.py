#-*- coding:utf-8 -*-
' a test module '
#
# __author__ = 'Michael Liao'
#
# import sys
#
# def test():
#     args = sys.argv
#     if len(args)==1:
#         print 'Hello, world!'
#     elif len(args)==2:
#         print 'Hello, %s!' % args[1]
#     else:
#         print 'Too many arguments!'
#
# if __name__=='__main__':
#     test()
# print 10//3
# class Student(object):
#
#     def __init__(self, name, score,age):
#         self.__name = name
#         self.__score = score
#         self._age=age
#
#     def print_score(self):
#         print '%s: %s' % (self.__name, self.__score)
# stu1=Student()
# stu1._age=100
# s=Student()
# def set_age(self, age): # 定义一个函数作为实例方法
#      self.age = age
# from types import MethodType
# s.set_age = MethodType(set_age, s, Student) # 给实例绑定一个方法
# s.set_age(25) # 调用实例方法
# s.age # 测试结果
# 25

# class Student(object):
#
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
# s=Student()
# s.score=90
# print s.score


# class Student(object):
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return 'Student object (name: %s)' % self.name
#
# print Student('Michael')









class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

print Fib()[5]
for i in Fib():
    print i