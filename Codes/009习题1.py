print('问题：卷毛最爱谁？')
#print('请输入密码：')
password = '最爱大迷糊'
count = 3
while count:
    word = input('请输入密码：')
    if '*' in word:
        print('密码中不能有‘*’号！您还有',count,'次机会！',end=' ')
        continue
    elif word!=password:
        print('密码错误！您还有',count-1,'次机会！',end=' ')
    else:
        print('猜对啦！你可真是卷毛肚子里的蛔虫呢~')
        break
    count -=1
