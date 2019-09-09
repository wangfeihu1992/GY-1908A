#! /user/bin/env python

i = 1
while (i < 101):
    print(i)
    i += 1

def jia_fa(a,b):
    print(a+b)
jia_fa(4,9)

def jia_fa(a,b):
    return a + b
c = jia_fa(4,26)
print(c)

def  bb(a,b=10):
    return a+b
print(bb(10,40))


def ww(*args,**kwargs):
    print(args)
    print(kwargs)
ww({'name':'王飞虎'},2,3,4,5,6,a=100,b=22)











