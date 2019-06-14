'''
from prettytable import PrettyTable
a = {'张三': {'age':'23', 'sex':'女', 'tel':'13993845165', 'email':'a@qq.com'},
     '李四': {'age':'23', 'sex':'女', 'tel':'13993845165', 'email':'a@qq.com'}}
xb = PrettyTable()
xb.field_names = ['用户名', '年龄', '性别', '电话', 'E-mail']
for x in a.keys():
    xb.add_row([x,a[x]['age'],a[x]['sex'],a[x]['tel'],a[x]['email']])
print(xb)
'''
class A:
    X = 123
    __slots__ = ('p1','p2')
    def __init__(self):
        self.p1 = 1
        self.p2 = 2

    def showme(self):
        print('I am A. {}'.format(self.p2))

print(A.__dict__)
a = A()
print(a.__slots__)

A.X = 600
class B(A):
    def __init__(self):
        self.b1 = 500

print(B().__dict__)

