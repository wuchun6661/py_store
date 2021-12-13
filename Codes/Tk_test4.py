from tkinter import *

root = Tk()

photo = PhotoImage(file="美女.gif")
theLabel = Label(root,
                 text="老姐你看，\nPython也可以P图哦~",
                 justify=RIGHT,
                 image=photo,
                 compound=CENTER,
                 font=("华康少女字体",20),
                 fg="red")
theLabel.pack()

mainloop()
