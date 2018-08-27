#!/use/bin/env python
#-*- coding: utf-8 -*-

#迭代器以及三目运算
#注意python没有 ?:这种三目运算

print('输入一个list，求出最大值和最小值~')
str=input('请输入一个list,数字之间用空格隔开:')

list=str.split(' ')
max=list[0]
min=list[0]

for val in list:
	max=max if max>=val else val
	min=min if min<val else val

print('最大值:',max)
print('最小值:',min)