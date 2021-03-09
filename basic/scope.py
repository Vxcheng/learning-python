import sys
from process import *
# 目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包
print(dir(sys))
print(sys.argv)
print(count, fibonacci(5))
# print(keyword.area(2,3))
if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')



'''
A namespace is a mapping from names to objects.Most namespaces are currently implemented as Python dictionaries。
命名空间(Namespace)是从名称到对象的映射，大部分的命名空间都是通过 Python 字典来实现的。
般有三种命名空间：
内置名称（built-in names）， Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等。
全局名称（global names），模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
局部名称（local names），函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）
局部的命名空间去 -> 全局命名空间 -> 内置命名空间

A scope is a textual region of a Python program where a namespace is directly accessible. "Directly accessible" here means that an unqualified reference to a name attempts to find the name in the namespace.
作用域就是一个 Python 程序可以直接访问命名空间的正文区域
规则顺序： L –> E –> G –>gt; B

当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。

'''
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    num = 123
    print(num)
fun1()
print(num)



def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()
