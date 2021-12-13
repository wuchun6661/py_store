while 1:
    num = int(input('请输入一个数字：'))
    for a in range(num):
        print(' '*(num-a-1) + '*'*(num-a))
