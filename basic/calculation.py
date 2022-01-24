'''
Python 语言支持以下类型的运算符:

算术运算符
比较（关系）运算符
赋值运算符
逻辑运算符
位运算符
成员运算符              in/not in
身份运算符              is/not is
运算符优先级

以下表格列出了从最高到最低优先级的所有运算符：
运算符	描述
**	指数 (最高优先级)
~ + -	按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //	乘，除，求余数和取整除
+ -	加法减法
>> <<	右移，左移运算符
&	位 'AND'
^ |	位运算符
<= < > >=	比较运算符
== !=	等于运算符
= %= /= //= -= += *= **=	赋值运算符
is is not	身份运算符
in not in	成员运算符
not and or	逻辑运算符
'''
import re

a = 12
values = re.findall(r"\d{1,}?\.\d{2}", str(a))
if values is not None:
    print(values[0])


def bytes_to_human(n):
    symbols = ('K','M','G','T','P','E','Z','Y')
    prefix = {}
    for i,s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value,s)
    return '%sB' % n
value = bytes_to_human(2*1024*1024)
print(value)