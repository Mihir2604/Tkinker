from tkinter import *
root=Tk()
def funct():
    mylabel=Label(root,text="I Clicked Button")
    mylabel.pack()

button=Button(root,text="Mihir",bg="black",fg="green",command=funct)
button.pack()
root.mainloop()