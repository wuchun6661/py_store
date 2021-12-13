def file_view(file_name,line_num):
    f = open('C:\\Users\\55450\\Desktop\\py_test\\' + file_name)
    for each in range(int(line_num)):
        print(f.readline(),end = '') # 为了不重复打印'\n'

    f.close()
