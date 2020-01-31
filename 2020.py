import turtle as t
t.screensize(300,600)
def ears(dir):  # 耳朵，dir用来设置方向，左右耳对称
    #大圈
    t.pu()
    t.goto((0 - dir) * 150, 120)
    t.setheading(0)
    t.pd()
    t.fillcolor('#F2D391')
    t.begin_fill()
    t.circle(80)
    t.end_fill()
    #小圈
    t.pu()
    t.goto((0 - dir) * 120, 120)
    t.setheading(0)
    t.pd()
    t.fillcolor('#F9ECF5')
    t.begin_fill()
    t.circle(60)
    t.end_fill()
def face():  # 画脸
    #加底图
    t.pu()
    t.goto(-45,216)
    t.pd()
    t.color("#FFE4B5","#FFE4B5")#前一个是笔的颜色，后一个是填充的颜色
    t.begin_fill()
    t.goto(45,216)
    t.goto(65, -20)
    t.goto(-65, -20)
    t.end_fill()
    t.color("black","#FFE4B5")#底图增加完毕，笔的颜色置回黑色
    #右边脸颊
    t.pu()
    t.goto(65,-20)
    t.pd()
    t.fillcolor('#FFE4B5')
    t.begin_fill()
    t.setheading(10)
    t.circle(120,180)
    #左边脸颊
    t.pu()
    t.goto(-65,-20)
    t.pd()
    t.setheading(170)
    t.circle(-120,180)
    #下巴
    t.pu()
    t.goto(-65,-20)
    t.pd()
    t.goto(65,-20)
    t.end_fill()
def mouth(): # 嘴巴
    #右边嘴巴
    t.pu()
    t.goto(0, 30)
    t.pd()
    t.setheading(-70)
    t.circle(30,180)
    #左边嘴巴
    t.pu()
    t.goto(0, 30)
    t.pd()
    t.setheading(-110)
    t.circle(-30,180)
def eyes(dir):  # 画眼睛，dir用来设置方向，左右眼对称
    #大圈
    t.pu()
    t.goto((0 - dir) * 30, 140)
    t.setheading(90)
    t.pd()
    t.fillcolor('white')
    t.begin_fill()
    t.circle(dir * 30)
    t.end_fill()
    #小圈
    t.pu()
    t.goto((0 - dir) * 40, 135)
    t.setheading(90)
    t.pd()
    t.fillcolor('#AAC9E3')
    t.begin_fill()
    t.circle(dir * 17)
    t.end_fill()
    #小小圈
    t.pu()
    t.goto((0 - dir) * 45, 135)
    t.setheading(90)
    t.pd()
    t.color("white","white")
    t.begin_fill()
    t.circle(dir * 5)
    t.end_fill()
    t.color("black","white")
def nose():  # 画鼻子
    t.pu()
    t.goto(14, 80)
    t.setheading(90)
    t.pd()
    t.fillcolor('red')
    t.begin_fill()
    t.circle(14)
    t.end_fill()
def beard(): #画胡须
    #右边胡须
    t.pu()
    t.goto(90, 80)
    t.pd()
    t.setheading(-15)
    t.fd(150)
    t.pu()
    t.goto(90, 60)
    t.pd()
    t.setheading(-30)
    t.fd(150)
    #左边胡须
    t.pu()
    t.goto(-90, 80)
    t.pd()
    t.setheading(-165)
    t.fd(150)
    t.pu()
    t.goto(-90, 60)
    t.pd()
    t.setheading(-150)
    t.fd(150)
def hat(): #帽子
    #小的半圆
    t.pu()
    t.goto(50, 265)
    t.pd()
    t.setheading(90)
    t.fillcolor('red')
    t.begin_fill()
    t.circle(50,180)
    t.end_fill()
    #大的半圆
    t.fillcolor('red')
    t.begin_fill()
    t.pu()
    t.setheading(0)
    t.goto(-80, 210)
    t.pd()
    t.fd(160)
    t.setheading(90)
    t.circle(80,180)
    t.end_fill()
    #铜钱大圆
    t.fillcolor('yellow')
    t.begin_fill()
    t.pu()
    t.goto(0, 220)
    t.setheading(0)
    t.pd()
    t.circle(30)
    t.end_fill()
    #铜钱小方块
    t.fillcolor('red')
    t.begin_fill()
    t.pu()
    t.goto(-15, 235)
    t.setheading(0)
    t.pd()
    t.fd(30)
    t.lt(90)
    t.fd(30)
    t.lt(90)
    t.fd(30)
    t.lt(90)
    t.fd(30)
    t.end_fill()
def clothes(): #衣服
    #下边衣角
    t.pu()
    t.goto(-120,-168)
    t.pd()
    t.setheading(-90)
    t.fillcolor('red')
    t.begin_fill()
    t.fd(40)
    t.lt(90)
    t.fd(240)
    t.lt(90)
    t.fd(40)
    t.end_fill()
    #加底图
    t.color("red","red")##+42
    t.pu()
    t.goto(-110, -3)
    t.pd()
    t.begin_fill()
    t.goto(-110, -188)
    t.goto(110, -188)
    t.goto(110, -3)
    t.end_fill()
    t.color("black","red")
    #左边袖子
    t.pu()
    t.goto(-110, -3)
    t.pd()
    t.setheading(-150)
    t.begin_fill()
    t.circle(100,160)
    t.setheading(90)
    t.fd(100)
    t.lt(60)
    t.fd(70)
    t.end_fill()
    #右边袖子
    t.pu()
    t.goto(110, -3)
    t.pd()
    t.setheading(-30)
    t.begin_fill()
    t.circle(-100,160)
    t.setheading(90)
    t.fd(100)
    t.rt(60)
    t.fd(70)
    t.end_fill()
    #中间条纹
    t.pu()
    t.goto(-20, -8)
    t.pd()
    t.fillcolor('yellow')
    t.begin_fill()
    t.setheading(-90)
    t.fd(200)
    t.lt(90)
    t.fd(40)
    t.lt(90)
    t.fd(200)
    t.lt(90)
    t.fd(40)
    t.end_fill()
    #袖口条纹
    t.pu()
    t.goto(-43, -188)
    t.pd()
    t.setheading(90)
    t.begin_fill()
    t.fd(100)
    t.lt(60)
    t.fd(40)
    t.setheading(-90)
    t.fd(120)
    t.end_fill()
    t.pu()
    t.goto(43, -188)
    t.pd()
    t.setheading(90)
    t.begin_fill()
    t.fd(100)
    t.rt(60)
    t.fd(40)
    t.setheading(-90)
    t.fd(120)
    t.end_fill()
def hand(): #手
    #左手
    t.pu()
    t.goto(-43, -168)
    t.pd()
    t.setheading(0)
    t.fillcolor('#FFE4B5')
    t.begin_fill()
    t.circle(40,180)
    t.end_fill()
    #左手手指条纹
    t.pu()
    t.goto(-5, -118)
    t.pd()
    t.fd(28)
    t.pu()
    t.goto(-3, -128)
    t.pd()
    t.fd(30)
    t.pu()
    t.goto(-5, -138)
    t.pd()
    t.fd(28)
    #右手
    t.pu()
    t.goto(43, -88)
    t.pd()
    t.setheading(180)
    t.begin_fill()
    t.circle(40,180)
    t.end_fill()
    #右手手指条纹
    t.pu()
    t.goto(5, -118)
    t.pd()
    t.fd(28)
    t.pu()
    t.goto(3, -128)
    t.pd()
    t.fd(30)
    t.pu()
    t.goto(5, -138)
    t.pd()
    t.fd(28)
def trousers(): #裤子
    #左边裤子
    t.pu()
    t.goto(-110,-208)
    t.pd()
    t.setheading(-100)
    t.fillcolor('red')
    t.begin_fill()
    t.fd(100)
    t.setheading(0)
    t.fd(90)
    t.goto(0,-208)
    #右边裤子
    t.pu()
    t.goto(110,-208)
    t.pd()
    t.setheading(-80)
    t.fd(100)
    t.setheading(180)
    t.fd(90)
    t.goto(0,-208)
    t.end_fill()
def shoes(): #鞋子
    #左边鞋子
    t.pu()
    t.goto(-125,-307)
    t.pd()
    t.setheading(-90)
    t.fillcolor('yellow')
    t.begin_fill()
    t.circle(40,180)
    t.end_fill()
    #左边鞋子条纹
    t.pu()
    t.goto(-85,-347)
    t.pd()
    t.setheading(90)
    t.fd(30)
    #右边鞋子
    t.pu()
    t.goto(125,-307)
    t.pd()
    t.setheading(-90)
    t.begin_fill()
    t.circle(-40,180)
    t.end_fill()
    #右边鞋子条纹
    t.pu()
    t.goto(85,-347)
    t.pd()
    t.setheading(90)
    t.fd(30)
def Originator(): #就系我啦
    t.pu()
    t.goto(0,-350)
    t.pd()
    t.write("庚子年正月初七", move=False, align="center", font=("Arial", 10, "normal"))
    t.pu()
    t.goto(0,-360)
    t.pd()
    t.setheading(90)
t.pensize(2)
clothes()
hand()
trousers()
shoes()
ears(1)
ears(-1)
face()
mouth()
eyes(1)
eyes(-1)
nose()
beard()
hat()
Originator()
t.done()