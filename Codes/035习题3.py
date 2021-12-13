import os
import easygui as g

file_path = g.fileopenbox(default='*.txt')

with open(file_path) as f:
    msg = '文件【%s】的内容是：' % os.path.basename(file_path)
    title = os.path.basename(file_path)
    text = f.read()
    g.textbox(msg,title,text)
