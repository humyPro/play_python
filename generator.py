#!/use/bin/env python
#-*- coding: utf-8 -*-

#generator生成器产生斐波拉契数列
def fib(max):
	if max<=0:
		return -1
	n,a,b=1,0,1
	while n<=max:
	#yield关键字，遇到这个关键字就中断，并返回b，下次又从下一句开始
		yield b 
		a,b=b,a+b
		n=n+1

		

###测试代码###
len=input('请输入斐波拉契数列的长度:')
fib_gen=fib(int(len))

list=[]
for i in fib_gen:
	list.append(i)
print(list)
	