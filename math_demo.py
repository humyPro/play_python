#!/use/bin/env python
# -*- coding:utf-8 -*-
#Author humy
import math

#在python交互界面，通过from 文件名 import 方法名 导入方法


#根据步数和角度移动
def move(x,y,step,angle=0):
	nx=x+step*math.cos(angle)
	ny=y+step*math.sin(angle)
	return nx,ny

#求1元2次方程的解
#x1=(-b+sqr(b**2-4ac))/2a
def quadratic(a,b,c):
	list=[a,b,c]
	for p in list:
		if not isinstance(p, (int, float)):
			raise TypeError('bad operand type')
	if (b**2-4*a*c)<0:
		return '此方程在实数下无解'
	if a==0 and b!=0:
		return -c/b
	if a==0 and b==0:
		return c
		
	x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
	x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
	return x1,x2