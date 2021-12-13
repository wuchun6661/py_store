while 1:
    year = int(input('请输入年份：'))
    if ((year%4==0) and (year%100!=0)) or (year%400==0):
        print('厉害，这都算的对，是闰年')
    else:
        print('不是闰年哦~')
    print('\n')
