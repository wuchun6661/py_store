from tkinter import *

root = Tk()

GIRLS = ["李嘉豪","肖勇","章万里","屈兴武"]

v = []

for girls in GIRLS:
    v.append(IntVar())
    b = Checkbutton(root,text=girls,variable=v[-1])
    b.pack(anchor=NW)

mainloop()
