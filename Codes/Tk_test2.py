import tkinter as tk

class APP:
    def __init__(self,master):
        master.title("小卷毛！")
        frame = tk.Frame(master)#形成一个Frame的对象
        frame.pack(side=tk.RIGHT,padx=100,pady=100)#包装
        #front_ground/back_ground/
        self.hi_there = tk.Button(frame,text="hello",fg="blue",bg="pink",command=self.say_hi)
        self.hi_there.pack()
    def say_hi(self):
        print("哈喽呀，大迷糊！")

root = tk.Tk()    
app = APP(root)

root.mainloop()
