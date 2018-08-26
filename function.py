# -*- coding: utf-8 -*-
def my_abs(x):
	if x>=0:
		print('是正数')
		return x
	else:
		return -x
		
a=input('请输入:')
print(my_abs(int(a)))