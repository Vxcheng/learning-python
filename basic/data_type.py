#!
# python3
## -*- coding: UTF-8 -*-
 
print( "你好，世界" )


'''
标准数据类型
Python3 中有六个标准的数据类型：

Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）
'''
vec = [2, 4, 6]
values = [[x, x**2] for x in vec]
print(values)



matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]; print([[row[i] for row in matrix] for i in range(4)])



t = 12345, 54321, 'hello!'; u = t, (1, 2, 3, 4, 5); print(u)
a = set('abracadabra'); b = set('alacazam'); print(a & b )
tel = {'jack': 4098, 'sape': 4139}; tel['guido'] = 4127; del tel['sape']
print(list(tel.keys())); print('jack' not in tel)
d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]); print(d); print(dict(sape=4139, guido=4127, jack=4098))

for k, v in tel.items():print(k, ":", v, end=", ")
l = ['tic', 'tac', 'toe']
for i, v in enumerate(l):
    print(i, v)
questions = ['name', 'quest', 'favorite color'];answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers): print('What is your {0}?  It is {1}.'.format(q, a))
s = set(l); print(s)
for i in sorted(s):print(i, end=", ")
print()
for i in reversed(l):print(i, end=", ")
