while 1:
    str1 = input('请输入你当前想写入的内容：')
    f = open(r'G:\text.txt','a+',encoding = 'UTF-8')
    f.write('\n' + str1)
    f.seek(0,0)
    f_now = f.read()
    f.close()
    print('修改完的内容为：\n',f_now)
    print('')
