i=5
while i>0: 
    x=int(input('输入分数啦：'))
    if 90<x<=100:
        print('A')
    elif 80<x<=90:
        print('B')
    elif 60<=x<=80:
        print('C')
    elif x<60:
        print('D')
    i -= 1
    if(i==1):
        print('最后一次机会啦\n')
    if(i==0):
        print('游戏结束！\n')
