def file_save(boy,girl,count):
    file_name_boy = 'C:\\Users\\55450\\Desktop\\py_test\\boy_' + str(count) + '.txt'
    file_name_girl = 'C:\\Users\\55450\\Desktop\\py_test\\girl_' + str(count) + '.txt'

    boy_file = open(file_name_boy,'x')
    girl_file = open(file_name_girl,'x')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()


def split_file(file_name):
    f = open(file_name,'r')
    boy = []
    girl = []
    count = 1

    for each_line in f:
        if each_line[:4] != '====':
            (role,line_spoken) = each_line.split(':',1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)
        else:
            file_save(boy,girl,count)

            boy = []
            girl = []
            count += 1
    file_save(boy,girl,count)

    f.close()


