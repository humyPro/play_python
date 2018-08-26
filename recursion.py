#!/use/bin/env python
# -*- coding: utf-8 -*-
#递归练习

#阶乘factorial
def factorial(n):
	if n==1:
		return 1
	return n*factorial(n-1)
	
#尝试一下今天的汤=昨天的汤+前天的汤
def fibonacci(n):
	if n==1 or n==2:
		return 1
	return fibonacci(n-1)+fibonacci(n-2)
#使用缓存提高执行效率

'''
def cache_fibo(n,cache):
	if cache[n-1]!=0:
		return cache[n-1]
	else:
		cache[n-1]=cache_fibo(n-1,cache)+cache_fibo(n-2,cache)
		return cache[n-1]
'''		
def cache_fibo(n,cache):
	if cache[n-1]==0:
		cache[n-1]=cache_fibo(n-1,cache)+cache_fibo(n-2,cache)
	return cache[n-1]
	
####测试代码####
n=int(input('请输入斐波拉契数列的长度:'))
#创建缓存列表
cache=[]
i=0
while i<n:
	i=i+1
	cache.append(0)
cache[0]=1
cache[1]=1

result=cache_fibo(n,cache)
#缓存列表其实就是斐波拉契数列	
print(cache)	
print('第%d个数是:' % n,result)