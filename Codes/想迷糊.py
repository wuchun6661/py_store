import easygui as g
import sys

while 1:
    choice = ['学习的时候想迷糊','闲的时候想迷糊','无时无刻想迷糊']
    reply = g.choicebox('卷毛什么时候想迷糊呢？',choices = choice)
    if reply == None:
        sys.exit(0)
    elif reply == choice[2]:
        g.msgbox('你可真是个小机灵鬼')
    else:
        g.msgbox('你个铁憨憨，会说话就多说点')
    if g.ccbox('你希望继续玩吗？','请选择'):
        pass
    else:
        sys.exit(0)
    
