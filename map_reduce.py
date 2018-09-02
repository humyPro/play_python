#!/use/bin/env python
#-*- coding:utf-8 -*-
#生成一个列表
l=[x for x in range(10)]
#print(l)

#平方函数
def f(x):
    return x*x

#map函数
r=map(f,l)
r=list(r)
print(r)

#函数2
def f2(x,y):
    return x+y
print('reduce')
#reduce方法
from functools import reduce
r=reduce(f2,r)
print(r)


#利用map/reduce实现字符串转数字
#str2int
def fn(x,y):
    return x*10+y

def char2num(x):
    digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
             '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[x]

def str2int(str):
    return reduce(fn,map(char2num,str))

i=str2int('123431')
print(i+1)


#利用map()函数，把用户输入的不规范的英文名字，
#变为首字母大写，其他小写的规范名字
def normalize(name):
    return name[0].upper()+name[1:len(name)].lower()
#测试
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
  
