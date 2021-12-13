import random
secret = random.randint(1,10)
print('******************啦啦啦啦啦********************')
temp = input("猜一猜我心中想的数字:")
guess = int(temp)
while guess != secret:
    temp = input("猜错了哦~再来一次:")
    guess = int(temp)
    if guess == secret:
        print("我草，你是蛔虫？")
        print("哼，猜中了也没奖")
    else:
        if guess > secret:
            print("大了")
        else: 
            print("小了~")
print("游戏结束！")
