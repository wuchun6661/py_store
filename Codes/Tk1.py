from tkinter import *

root = Tk()

v = IntVar()

c = Checkbutton(root,text="test",variable=v)
c.pack()

d = Label(root,textvariable=v)
d.pack()

mainloop()
