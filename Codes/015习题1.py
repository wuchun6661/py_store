flag = 1
while flag:
    num = input('请输入一个整数(输入Q程序结束)：')
    if num != 'Q':
        num = int(num)
        print('十进制 -> 十六进制 ：%d -> 0x%x' % (num,num))
        print('十进制 -> 八进制 ：  %d -> 0o%o' % (num,num))
        print('十进制 -> 二进制 ：  %d ->'      % num,bin(num) )
    else:
        flag = 0
    
