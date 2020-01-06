#coding=utf-8

from operator import *

#实现计算器

def calculator(a,b,k):
    return {
        '+' : add,
        '-' : sub,
        '*' : mul,
        '/' : truediv,
        '**' : pow
    }[k](a,b)

print(calculator(1,2,'+'))
print(calculator(3,4,'**'))