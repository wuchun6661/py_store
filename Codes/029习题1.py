def file_new_write():
    
    '#新建一个文件夹，并且写入内容'
    file_name = input('请输入文件名：')
    file_name ='C:\\Users\\55450\\Desktop\\'+file_name
    f = open(file_name,'x')
    print('请输入内容【单独输入\':w\'保存退出】：')

    while 1:
        write_some = input()
        if write_some != ':w':
            f.write('%s\n' % write_some)
        else:
            break
    f.close()
