#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/09 15:05
# @Author  : 罗小贱
# @email: ljq906416@gmail.com
# @File    : 面向对象.py
# @Software: PyCharm

'''对name和age进行数据校验'''
'''1、写函数，在__init__中先进行检查'''
'''
class Person:
    def __init__(self,name,age):
        params = ((name,str),(age,int))
        if not self.checkdata(params):
            raise TypeError()
        self.name = name
        self.age = age

    def checkdata(self,params):
        for name,parm in params:
            if not  isinstance(name,parm):
                return False
        return True

p = Person('tom','14')
'''
import inspect
class Typed:   #描述器
    def __init__(self,type):
        self.type = type

    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        if not isinstance(value,self.type):
            raise ValueError(value)

class TypeAssert:
    def __init__(self,cls):
        self.cls = cls   #记录着被包装的Person类
        params = inspect.signature(self.cls).parameters    #检查参数，返回的是函数的初始化方法的参数注解，OrderedDict([('name', <Parameter "name:str">), ('age', <Parameter "age:int">)])
        for name, param in params.items():
            print(name, param.annotation)
            if param.annotation != param.empty:
                setattr(self.cls, name, Typed(param.annotation)) #注入类属性


    def __call__(self, name, age):
        p = self.cls(name,age)   #重新构建一个新的Person对象
        return p

@TypeAssert  #装饰器
class Person:  #Person=TypeAssert(Person)
    # name = Typed('name',str)
    # age = Typed('age',int)

    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age

p1 = Person('tom','12')