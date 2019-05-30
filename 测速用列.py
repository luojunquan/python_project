#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/24 16:13
# @Author  : 罗小贱
# @email: ljq906416@gmail.com
# @File    : 测速用列.py
# @Software: PyCharm
'''
class Adder:
     def __call__(self, *args, **kwargs):
        ret = 0
        for x in args:
            ret += x

        self.ret= ret
        return ret

adder = Adder()
print(adder(1,2,3))
'''

'''斐波那契数列'''
'''
class Fib:
    def __init__(self):
        self.items = [0,1,1]

    def __call__(self, n):
        l = len(self.items)
        if n < 0:
            raise IndexError
        elif n < len(self.items):
            return self.items[n]

        for i in range(l,n+1):
            x = self.items[i - 1] + self.items[i - 2]
            self.items.append(x)
        return x

fib = Fib()
print(fib(10))
print(fib(3))
'''
'''
完成Point类的设计吧，实现断点相等的方法，并完成向量的加法
'''
'''
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point:({},{})'.format(self.x,self.y)
        # return str((self.x,self.y))
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x+other.x,self.y+other.y)

    def add(self,other):
        return self.x+other.x,self.y+other.y
p1 = Point(3, 4)
p2 = Point(3, 5)
p3 = (p1,p2)
print(p1 == p2)
print(p3[0].add(p3[1]))
print(p1 + p2)
'''
'''乘法口诀'''
'''
for i in range(1,10):
    for j in range(1,i+1):
        print('%s*%s=%s' %(i,j,i*j),end = ' ')
    print()
'''
'''
随机生成整数
1、普通类实现
2、作为工具类实现，提供类方法
3、生成器随机生成整数
'''
import random
'''
class RandomGen:
    def __init__(self,start=1,stop=100,count=10):
        self.start = start
        self.stop = stop
        self.count = count

    def generate(self,start=1,stop=100,count=10):
        return [random.randint(self.start,self.stop) for x in range(self.count)]

r = RandomGen()
print(r.generate())
'''
'''
class RandomGen:
    @classmethod
    def generate(cls,start=1,stop=100,count=5):
        return [random.randint(start,stop) for x in range(count)]

r = RandomGen()
print(r.generate())
'''
'''生成器随机生成整数'''
'''
import random
class RandomGenerator:
    def __init__(self, start=1, stop=100, patch=10):
        self.start = start
        self.stop = stop
        self.patch = patch
        self._gen = self._generate()
    def _generate(self):
        while True:
            yield [random.randint(self.start,self.stop) for _ in range(self.patch)]
    def generate(self,count=10):
        if count > 0:
            self.patch = count
        return next(self._gen)

# a = RandomGenerator()
# print(a.generate())
'''
'''和上个类，两两配对生成二维坐标系的坐标'''
'''
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

points = [Point(x,y) for x,y in zip(RandomGenerator(10).generate(),RandomGenerator(10).generate())]
for p in points:
    print('{}:{}'.format(p.x,p.y))
'''
'''记录车的品牌、颜色、价格、速度等特征。并实时增加车辆信息，显示全部车辆信息的功能'''
'''
class Car:
    def __init__(self,mark,speed,color,price):
        self.mark = mark #品牌
        self.speed = speed #速度
        self.color = color #颜色
        self.price = price #价格

class CarInfo:
    def __init__(self):
        self.info = []
    def addcar(self,car):
        self.info.append(car)
    def getall(self):
        return self.info

ci = CarInfo()
car = Car('audi',400,'red',100)
ci.addcar(car)
'''
import time,datetime
from functools import wraps
'''
class TimeIt:
    def __init__(self,fn):
        self._fn = fn
        wraps(fn)(self)  #@TimeIt
    def __call__(self, *args, **kwargs):
        start = datetime.datetime.now()
        ret = self._fn(*args,**kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print("dec {} took {}".format(self._fn.__name__,delta))
        return ret

# @TimeIt  #add = TimeIt(add)
#如果不用装饰器，需要再__init__中增加wraps(fn)(self)，两个相等
def add(x,y):
    time.sleep(2)
    return x + y

print(add(4,6))
'''
'''
def TimeIt(fn):
    # @wraps(fn)
    def wrapper(*args,**kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print("dec {} took {}".format(fn.__name__, delta))
        return ret
    return wrapper

@TimeIt
def add(x,y):
    time.sleep(2)
    return x + y

print(add(3,5))
'''
'''反射'''
'''
class Ponint:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point({},{})".format(self.x,self.y)

    def show(self):
        print(self.x,self.y)

p1 = Ponint(4,5)
p2 = Ponint(10,20)
# print(repr(p1),repr(p2),sep='\n')
print(p1.__dict__)
setattr(p1,'y',16)
setattr(p2,'z',30)
print(getattr(p1,'__dict__'))
if hasattr(p1,'show'):
    getattr(p1,'show')()

# if not hasattr(Ponint,'add'):
#     setattr(Ponint,'add',lambda self,other:Ponint(self.x + other.x,self.y + other.y))
#
# print(Ponint.add)
# print(p1.add)
# print(p1.add(p2))
if not hasattr(p1,'sub'):
    setattr(p1,'sub',lambda self,other:Ponint(self.x - other.x,self.y - other.y))

print(p1.sub(p1,p1))
print(p1.sub)

print(p1.__dict__)
print(Ponint.__dict__)
'''
'''
class Dispatcher:
    def __init__(self):
        self._run()
    def cmd1(self):
        print('I am cmd1')
    def cmd2(self):
        print('I am cmd2')
    def _run(self):
        while True:
            cmd = input("input a command:").strip()
            if cmd == 'quit':
                break
            getattr(self,cmd,lambda : print("Unown Command {}".format(cmd)))()

Dispatcher()
'''
'''
class Base:
    n = 0

class Point(Base):
    z = 6
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x,self.y)

    def __getattr__(self, item):
        return 'missing {}'.format(item)

    def __setattr__(self, key, value):
        print("setter {} = {}".format(key,value))
p1 = Point(4,5)
# print(p1.x)
# print(p1.z)
# print(p1.n)
# print(p1.t)
p1.x = 30
print(p1.__dict__)
p1.__dict__['x'] = 60
print(p1.__dict__)
print(p1.x)
'''
from functools import partial
class StaticMethod:
    def __init__(self,fn):
        print(fn)
        self.fn = fn

    def __get__(self, instance, owner):
        # print(self,instance,owner)
        return self.fn

class ClassMethod:
    def __init__(self,fn):
        self.fn = fn

    def __get__(self, instance, owner):
        return partial(self.fn,owner) #partial返回一个函数
class A:
    @StaticMethod
    def foo():
        print('static')

    @ClassMethod
    def bar(cls):
        print(cls.__name__)

f = A.bar
# print(f)
f()
























































































































