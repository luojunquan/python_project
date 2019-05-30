from prettytable import PrettyTable
a = {'张三': {'age':'23', 'sex':'女', 'tel':'13993845165', 'email':'a@qq.com'},
     '李四': {'age':'23', 'sex':'女', 'tel':'13993845165', 'email':'a@qq.com'}}
xb = PrettyTable()
xb.field_names = ['用户名', '年龄', '性别', '电话', 'E-mail']
for x in a.keys():
    xb.add_row([x,a[x]['age'],a[x]['sex'],a[x]['tel'],a[x]['email']])
print(xb)