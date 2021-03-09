# 斐波拉契
a, b = 0, 1
while b < 10:
   print(b, end=', ')
   a, b = b, a+b
print()


# if
# num=int(input("输入一个数字："))
num = 10
if num%2==0:
    if num%3==0:
        print ("你输入的数字可以整除 2 和 3")
    else:
        print ("你输入的数字可以整除 2，但不能整除 3")
else:
    if num%3==0:
        print ("你输入的数字可以整除 3，但不能整除 2")
    else:
        print  ("你输入的数字不能整除 2 和 3")



# while
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n,sum))

count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")



# for
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

for i in range(0, 10, 3) :
    print(i)

print("range:", list(range(5)))

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('循环结束。')

for letter in 'Runoob': 
   if letter == 'o':
      pass
      print ('执行 pass 块')
   print ('当前字母 :', letter)
 
print ("Good bye!")



# 迭代器
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")
print ()

list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
print(next(it),next(it), end=" ")
print()

class MyNumbers:
   def __iter__(self):
       self.a = 1
       return self
   
   def __next__(self):
      if self.a < 5:
         x = self.a
         self.a += 1
         return x
      else:
          raise StopIteration         
     
myclass = MyNumbers(); myiter = iter(myclass)
count = 0
while count <= 2:
   print (next(myiter), end=" ")
   count += 1
print()
for item in myiter:
   print (item, end=" ")
print ("创建迭代器对象")



# 生成器，使用了 yield 的函数被称为生成器，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
def fibonacci(n):
   a, b, counter = 0, 1, 0
   while True:
      if counter > n:
         return
      yield a
      a, b = b, a+b
      counter += 1
f = fibonacci(5); count = 0; 
while (count < 5): print (next(f), end=" "); count += 1
print("生成器yield")
