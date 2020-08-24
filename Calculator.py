from tkinter import *
root=Tk()
def calculate():
    x=int(Value1.get())
    y=int(Value.get())
    if(value2.get()=='+'):
        ans=x+y
        label=Label(root,text=ans)
    elif(value2.get()=='-'):
        ans = x-y
        label = Label(root, text=ans)
    elif (value2.get() == '*'):
        ans = x*y
        label = Label(root, text=ans)
    elif (value2.get() == '/'):
        ans = x/y
        label = Label(root, text=ans)
    label.pack()
mylabel=Label(root,text="Enter First Value")
Value=Entry(root)

mylabel2=Label(root,text="Enter Operator")
value2=Entry(root)

mylabel1=Label(root,text="Enter Second Value")
Value1=(Entry(root))


mylabel.pack()
Value.pack()


mylabel2.pack()
value2.pack()


mylabel1.pack()
Value1.pack()
#button1.pack()

button3=Button(root,command=calculate,text="Submit")
button3.pack()

root.mainloop()