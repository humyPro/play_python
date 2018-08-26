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

#上面的定义方式，使用的时候可以不受限制的传入参数，可以使用命名关键字参数做限定
#如此使用的时候就必须传入city='',job=''
def new_person_1(name,age,*,city,job):
	print(name,age,city,job)

new_person_1('humy',23,city='chengdu',job='jialidun')

#如果定义了可变参数，那么久不需要*做分隔符了，可以直接写关键字参数
def new_person_2(name,age,*args,city,job):
	print(name,age,args,city,job)

new_person_2('humy',23,'可变参数1','可变参数2',city='chengdu',job='jialidun')

#可以给关键字参数设置缺省值，传参的时候不写就默认是缺省值
def new_person_3(name,age,*args,city='chengdu-sichuan',job):
	print(name,age,args,city,job)

new_person_3('humy',23,'可变参数1','可变参数2',job='jialidun')

'''
参数组合:
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
这5种参数都可以组合使用。
但是请注意，
参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''

#记住映射规则：python解释器会自动按照参数位置和参名把对应的参数传进去
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
#最后打印的结果是：a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
#因为*args表示取出元组中的值(也可以用list替换tuple),赋值给参数，当然只能赋值给必选参数和默认参数以及可变参数；
#对于关键字参数，则可以传入一个字典。

#
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
#这个方法定义了两个必选参数，一个默认参数，一个明明关键字参数，一个关键字参数，
#如果传入一个字典，那么会先分配一个key为d的值给d，然后才把剩下的分配给kw
#也就是说字典中必须包含命名关键字参数的key，顺序无所谓






