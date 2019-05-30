#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/112 15:20
# @Author  : 罗小贱
# @email: ljq906416@gmail.com
# @File    : 冒泡排序
# @Software: PyCharm
list = [3, 7, 2, 5, 20, 11]
for i in range(len(list)):
    for j in range(i + 1,len(list)):
        if list[i] > list[j]:
            list[i],list[j] = list[j],list[i]

print(list)
