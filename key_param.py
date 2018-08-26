#!/use/bin/env python
# -*- coding: utf-8 -*-
print('关键字参数使用，定义了一个person(name,age,**kw)')
print('定义关键字参数后，传入参数时，需要以key=value的形式，传入任意的关键字参数；')
print('这些关键字参数在函数内部自动组装为一个dict，也可以事先准备好一个dict，然后以**dict的形式传入')
def person(name,age,**kw):
	print('name:',name,',age:',age,',other:',kw)
'''
>>> person('humy',23,gender='男')
name: humy ,age: 23 ,other: {'gender': '男'}
>>> person('humy',23,gender='男')
name: humy ,age: 23 ,other: {'gender': '男'}
>>> dict={'gender':'male','addr':'sichuan-chengdu'}
>>> person('humy',23,**dict)
name: humy ,age: 23 ,other: {'gender': 'male', 'addr': 'sichuan-chengdu'}
>>>
'''