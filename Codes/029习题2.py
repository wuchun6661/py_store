def file_compare(file1,file2):
    f1 = open('C:\\Users\\55450\\Desktop\\py_test\\' + file1)
    f2 = open('C:\\Users\\55450\\Desktop\\py_test\\' + file2)
    count = 0
    differ = []

    for line1 in f1:
        line2 = f2.readline()
        count += 1
        if line1 != line2:
            differ.append(count)

    f1.close()
    f2.close()

    if len(differ) == 0:
        print('两个文件完全一样!')
    else:
        print('有【',count,'】处不一样')
        for a in differ:
            print('第',a,'行不一样')
            
  

