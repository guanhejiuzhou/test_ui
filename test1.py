#-*-coding:utf-8-*-

#序列封包：将10/20/30封装成元组后赋值给vals
vals=10,20,30
print(vals)#(10,20,30)
print(type(vals))#<class 'tuple'>
print(vals[1])#20
#序列解包：将a_tuple元组的各元素依次赋值给a,b,c,d,e变量
a_tuple=tuple(range(1,10,2))
a,b,c,d,e=a_tuple
print(a,b,c,d,e)#1 3 5 7 9
#如果在赋值中同时运用了序列封包和序列解包机制，就可以让赋值
#运算符支持同时将多个值赋给多个变量
#将10/20/30依次赋给x/y/z
x,y,z=10,20,30
print(x,y,z)#10 20 30

#序列解包时，可以只解出部分变量剩下的依然使用列表变量保存
#在左边被赋值的变量之前添加*
#first、second保存前两个元素，rest列表包含剩下的元素
first,second,*rest=range(10)
print(first)#0
print(second)#1
print(rest)#[2,3,4,5,6,7,8,9]
#first保存第一个元素，last保存最后一个元素，middle保存中间剩下的元素
first,*middle,last=range(10)
print(first)#0
print(middle)#[1,2,3,4,5,6,7,8]
print(last)#9



