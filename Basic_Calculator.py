from tkinter import *
root=Tk()
root.title("Calculator")

e=Entry(root, width=35, borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def numbers(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    if number=="clear":
        e.delete(0,END)

def add():
    global first_num
    first_num = int(e.get())
    e.delete(0, END)
    global result
    result="+"
def subtract():
    global first_num
    first_num = int(e.get())
    e.delete(0, END)
    global result
    result = "-"
def divide():
    global first_num
    first_num = int(e.get())
    e.delete(0, END)
    global result
    result = "/"
def multiply():
    global first_num
    first_num = int(e.get())
    e.delete(0, END)
    global result
    result = "*"
def equal():
    second_num=e.get()
    e.delete(0,END)
    if result=="+":
        e.insert(0, int(second_num) + first_num)
    elif result=="-":
        e.insert(0, first_num - int(second_num))
    elif result=="*":
        e.insert(0, int(second_num) * first_num)
    elif result=="/":
        e.insert(0, first_num / int(second_num))

button1=Button(root,text="1", padx=40, pady=20,command=lambda: numbers(1))
button2=Button(root,text="2", padx=40, pady=20,command=lambda: numbers(2))
button3=Button(root,text="3", padx=40, pady=20,command=lambda: numbers(3))
button4=Button(root,text="4", padx=40, pady=20,command=lambda: numbers(4))
button5=Button(root,text="5", padx=40, pady=20,command=lambda: numbers(5))
button6=Button(root,text="6", padx=40, pady=20,command=lambda: numbers(6))
button7=Button(root,text="7", padx=40, pady=20,command=lambda: numbers(7))
button8=Button(root,text="8", padx=40, pady=20,command=lambda: numbers(8))
button9=Button(root,text="9", padx=40, pady=20,command=lambda: numbers(9))
button0=Button(root,text="0", padx=40, pady=20,command=lambda: numbers(0))
buttonadd=Button(root, text="+",padx=39, pady=20,command= add)
buttonclear=Button(root, text="Clear",padx=81, pady=20,command= lambda: numbers("clear"))
buttonequal=Button(root, text="=",padx=91,pady=20,command= equal)
buttonsubtract=Button(root, text="-",padx=40, pady=20,command= subtract)
buttondivide=Button(root, text="/",padx=40, pady=20,command= divide)
buttonmultiply=Button(root, text="*",padx=40, pady=20,command= multiply)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
buttonequal.grid(row=4,column=1, columnspan=2)

buttonadd.grid(row=5,column=0)
buttonclear.grid(row=5,column=1,columnspan=2)

buttonsubtract.grid(row=6,column=0)
buttonmultiply.grid(row=6,column=1)
buttondivide.grid(row=6,column=2)

root.mainloop()
