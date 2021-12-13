print('一共有多少阶呢？\n')
print('哈哈，答案就是：')
for a in range(700):
    if (a%2==1) and (a%3==2) and (a%5==4) and (a%6==5) and (a%7==0):
        print(a,end='阶啦~\n')
        
