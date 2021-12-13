import easygui as g
import random

g.msgbox('嗨，欢迎进入第一个界面小游戏')
secret = random.randint(1,10)

msg = '不妨猜一下小卷毛现在心里想的是哪个数字(1-10)'
title = '猜数字'
guess = g.integerbox(msg,title,lowerbound = 1,upperbound = 10)

while True:
    if guess == secret:
        g.msgbox('我草，你是卷毛心里的蛔虫？！')
        g.msgbox('哼，猜中了也没有奖励哦')
        break
    else:
        if guess>secret:
            g.msgbox('大了大了~')
        else:
            g.msgbox('小了小了！')
        guess = g.integerbox(msg,title,lowerbound=1,upperbound=10)

g.msgbox('游戏结束不玩啦~')
