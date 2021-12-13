import os

all_files = os.listdir(os.curdir)
type_dict = dict()
catalog_now = os.getcwd()

for each in all_files:
    each = os.path.join(catalog_now,each) #为了防止文件没有目录信息
    if os.path.isdir(each):
        type_dict.setdefault('文件夹',0)
        type_dict['文件夹'] += 1
    else:
       ext = os.path.splitext(each)[1]
       type_dict.setdefault(ext,0)
       type_dict[ext]  += 1

for each_type in type_dict.keys():
    print('该文件夹下共有文件类型为【%s】的文件 %d 个' % (each_type,type_dict[each_type]))
