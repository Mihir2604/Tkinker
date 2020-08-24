from tkinter import *
root=Tk()
root.title("Calculator")
e=Entry(root,width=35)
e.grid(row=0,padx=10,pady=10,columnspan=3,column=0)
def button_add(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    return
def button_clear():
    e.delete(0,END)
def button_sum(operator):
    global s
    global op
    op=operator
    s=int(e.get())
    e.delete(0,END)
def button_eq():
    second=e.get()
    e.delete(0,END)
    if(op=="+"):
        e.insert(0,s+int(second))
    elif(op=="-"):
        e.insert(0, s + int(second))
    elif(op=="*"):
        e.insert(0, s * int(second))
    elif(op=="/"):
        e.insert(0,s/int(second))
def button_clear():
    e.delete(0,END)

button=Button(root,text="0",padx=40,pady=20,command=lambda:button_add(0))
button1=Button(root,text="1",padx=40,pady=20,command=lambda:button_add(1))
button2=Button(root,text="2",padx=40,pady=20,command=lambda:button_add(2))
button3=Button(root,text="3",padx=40,pady=20,command=lambda:button_add(3))
button4=Button(root,text="4",padx=40,pady=20,command=lambda:button_add(4))
button5=Button(root,text="5",padx=40,pady=20,command=lambda:button_add(5))
button6=Button(root,text="6",padx=40,pady=20,command=lambda:button_add(6))
button7=Button(root,text="7",padx=40,pady=20,command=lambda:button_add(7))
button8=Button(root,text="8",padx=40,pady=20,command=lambda:button_add(8))
button9=Button(root,text="9",padx=40,pady=20,command=lambda:button_add(9))
button10=Button(root,text="+",padx=40,pady=20,command=lambda:button_sum("+"))
button11=Button(root,text="-",padx=40,pady=20,command=lambda:button_sum("-"))
button12=Button(root,text="*",padx=40,pady=20,command=lambda:button_sum("*"))
button13=Button(root,text="/",padx=40,pady=20,command=lambda:button_sum("/"))
button14=Button(root,text="=",padx=40,pady=20,command=button_eq)
button15=Button(root,text="Clear",padx=130,pady=10,command=button_clear)



button.grid(row=1,column=0)
button1.grid(row=1,column=1)
button2.grid(row=1,column=2)
button3.grid(row=2,column=0)
button4.grid(row=2,column=1)
button5.grid(row=2,column=2)
button6.grid(row=3,column=0)
button7.grid(row=3,column=1)
button8.grid(row=3,column=2)
button9.grid(row=4,column=0)
button10.grid(row=4,column=1)
button11.grid(row=4,column=2)
button12.grid(row=5,column=1)
button13.grid(row=5,column=2)
button14.grid(row=5,column=0)
button15.grid(row=6,column=0,columnspan=3)






root.mainloop()