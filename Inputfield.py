from tkinter import *
root=Tk()
def myc():
    lab=Label(root,text="Hello " + hel.get())
    lab.pack()
hel=Entry(root)
hel.insert(0,"Insert Name")
but=Button(root,text="Click here",command=myc)
hel.pack()
but.pack()
root.mainloop()