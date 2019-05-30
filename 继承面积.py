#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/10 09:51
# @Author  : 罗小贱
# @email: ljq906416@gmail.com
# @File    : 继承.py
# @Software: PyCharm

class Shape:
    def area(self):
        pass

class Triangle(Shape):
    '''三角形面积'''
    def __init__(self,bottom,high):
        self.bottom = bottom
        self.high = high

    def area(self):
        return self.high * self.bottom / 2

class Rectangle(Shape):
    '''长方形面积'''
    def __init__(self,long,width):
        self.long = long
        self.width = width

    def area(self):
        return self.long * self.width

t = Triangle(10,5)
print(t.area())