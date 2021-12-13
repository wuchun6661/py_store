import os

def search_file(start_dir,target) :
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir):
        if each_file == target:
            print(os.getcwd() + os.sep + each_file)
        if os.path.isdir(each_file):
            search_file(each_file,target)
            os.chdir(os.curdir)

start_dir = input('请输入待搜查的初始目录：')
target = input('请输入要寻找的文件名：')
search_file(start_dir,target)
