#!/usr/bin/env python3
# -*- coding: utf-8 -*-

height=input('请输入你的身高(cm):')
weight=input('请输入你的体重(kg):')
height=float(height)/100
weight=float(weight)
#print(height)
bmi=weight/(height*height)
#print(bmi)
print('你的BMI指数是:%.2f' % bmi)
if bmi<18.5:
	print('体重过轻~')
elif bmi<25:
	print('正常~')
elif bmi<28:
	print('偏重')
elif bmi<32:
	print('肥胖')
else:
	print('严重肥胖')
