#!/use/bin/env python
# -*- coding: utf-8 -*-
def calc(*nums):
	sum=0;
	for n in nums:
		sum+=n*n
	return sum

print('这里定义了一个计算a^2+b^2+....+n^2的函数')
print('函数签名是calc(*nums)')
print('可以传入一个list或者tuple，这样：nums=[1,2,3] -> cale(*nums)')