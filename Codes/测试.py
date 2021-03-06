import os

def search_file(start_dir, target) :
    os.chdir(start_dir)

    try:
        for each_file in os.listdir(os.curdir) :
            ext = os.path.splitext(each_file)[1]
            if ext in target :
                vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep) # 使用os.sep是程序更标准
            if os.path.isdir(each_file) :
                search_file(each_file, target) # 递归调用
                os.chdir(os.pardir) # 递归调用后切记返回上一层目录
    except:
        os.chdir(os.pardir)

start_dir = input('请输入待查找的初始目录：')
program_dir = os.getcwd()

target = ['.mp4', '.avi', '.rmvb']
vedio_list = []

search_file(start_dir, target)

f = open(program_dir + os.sep + 'vedioList.txt', 'w')
f.writelines(vedio_list)
f.close()
