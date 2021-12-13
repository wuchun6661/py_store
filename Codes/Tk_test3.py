from tkinter import *

root = Tk()

textLabel = Label(root,text="您所下载的影片含有未成年人禁止内容，\n请满18周岁后再点击观看")
textLabel.pack(side=LEFT)

photo = PhotoImage(file="滑稽.gif")
imgLabel = Label(root,image=photo)
imgLabel.pack(side=RIGHT)

mainloop()
