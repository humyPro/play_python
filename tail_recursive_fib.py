#!/use/bin/env python
#-*- coding: utf-8 -*-

#在网上看到一个尾递归，感觉很强大，不就是n作计数器一直递减么？和用循环写一个道理。
#但是这种尾递归的思想很重要，来试一试
#1,1,2,3,5,8...

#调用的时候，需要使before_yesterday=1，yesterday=1，n就是需要求出的位置的数字
def tail_recursive_fib(n,before_yesterday=1,yesterday=1):
	if n<=0:
		return -1
	if n==1:
		return before_yesterday
	if n==2:
		return yesterday
	return tail_recursive_fib(n-1,yesterday,yesterday+before_yesterday)
	
	
#测试代码
print('尾递归计算斐波拉契数~')
n=input('请输入位数：')
x=tail_recursive_fib(int(n))
print(x)
	