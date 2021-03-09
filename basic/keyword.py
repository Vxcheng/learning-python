'''函数
可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
    不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
    可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
python 函数的参数传递：
    不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
    可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响
python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
'''

def change(a):
    print(id(a), end=" ")   # 指向的是同一个对象
    a=10
    print(id(a), end=" ")   # 一个新对象
a=1;print(id(a), end=" ");change(a);print(id(a), end=" ");print()

def changeme( mylist ): mylist.append([1,2,3,4]); print ("函数内取值: ", mylist)
mylist = [10,20,30];changeme( mylist );print ("函数外取值: ", mylist)
def area(width, height): return width * height
def print_welcome(name): print("Welcome", name)
print_welcome("Runoob");w = 4; h = 5; print("width =", w, " height =", h, " area =", area(w, h))

'''
以下是调用函数时可使用的正式参数类型：

必需参数
关键字参数
默认参数
不定长参数
'''
def printinfo(name, age =10): print(name, age, end=" ")
printinfo(name="xiaoming"); print()

def printinfo( arg1, *vartuple ): # tuple
   "打印任何传入的参数"
   print (arg1, end=" ")
   for var in vartuple:
      print (var, end=" ")
 
# 调用printinfo 函数
printinfo( 10)
printinfo( 70, 60, 50 ); print()

def printinfo(args, **dicts): print (args, end=" "); print(dicts)
printinfo(1, a=2,b=3, c=4)

def f(a,b,*,c): return a+b+c
print(f(1,2,c=3))


'''
python 使用 lambda 来创建匿名函数。
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数
'''
sum = lambda a, b: a+b; print(sum(2,3))

# Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式
def f(a, b, /, c, d, *, e, f):print(a, b, c, d, e, f)
f(1,2, 3, d=4, e=5, f=6)



# 异常
try:
    print("exception")
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('这句话，无论异常是否发生都会执行。')

# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise
# 关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法: