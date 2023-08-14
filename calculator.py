import tkinter
from tkinter import *
window=Tk()
window.title("calculator")
window.geometry("400x350")
window.config(bg="white")

equation=""
def clear():
    global equation
    equation=""
    lab.config(text=equation)
def show(value):
    global equation
    equation+=value
    lab.config(text=equation)
def calculate():
    global equation
    res=""
    if equation!="":
        try:
            res=eval(equation)
        except:
            res="error"
            equation=""
    lab.config(text=res)

lab=Label(window,text="",bg="white",width=25,height=2,font=("arial",30))
lab.pack(fill=X)


Button(window,text="AC",bg="white",fg="blue",width=10,height=1,font=("arial",15,"bold"),command=lambda:clear()).place(x=10,y=100)
Button(window,text="%",bg="white",fg="blue",width=5,height=1,font=("arial",15,"bold"),command=lambda:show("%")).place(x=200,y=100)
Button(window,text="/",bg="white",fg="blue",width=5,height=1,font=("arial",15,"bold"),command=lambda:show("/")).place(x=300,y=100)

Button(window,text="7",bg="white",fg="blue",width=5,height=1,font=("arial",15,"bold"),command=lambda:show("7")).place(x=10,y=150)
Button(window,text="8",bg="white",fg="blue",width=5,height=1,font=("arial",15,"bold"),command=lambda:show("8")).place(x=100,y=150)
Button(window,text="9",bg="white",fg="blue",width=5,height=1,font=("arial",15,"bold"),command=lambda:show("9")).place(x=200,y=150)
Button(window,text="*",bg="white",fg="blue",width=5,height=1,font=("arial",15,"bold"),command=lambda:show("*")).place(x=300,y=150)

Button(window,text="4",bg="white",fg="blue",width=5,height=1,font=("arial",15,"bold"),command=lambda:show("4")).place(x=10,y=200)
Button(window,text="5",bg="white",fg="blue",width=5,height=1,font=("arial",15,"bold"),command=lambda:show("5")).place(x=100,y=200)
Button(window,text="6",bg="white",fg="blue",width=5,height=1,font=("arial",15,"bold"),command=lambda:show("6")).place(x=200,y=200)
Button(window,text="-",bg="white",fg="blue",width=5,height=1,font=("arial",15,"bold"),command=lambda:show("-")).place(x=300,y=200)


Button(window,text="1",bg="white",fg="blue",width=5,height=1,font=("arial",15,"bold"),command=lambda:show("1")).place(x=10,y=250)
Button(window,text="2",bg="white",fg="blue",width=5,height=1,font=("arial",15,"bold"),command=lambda:show("2")).place(x=100,y=250)
Button(window,text="3",bg="white",fg="blue",width=5,height=1,font=("arial",15,"bold"),command=lambda:show("3")).place(x=200,y=250)
Button(window,text="+",bg="white",fg="blue",width=5,height=1,font=("arial",15,"bold"),command=lambda:show("+")).place(x=300,y=250)

Button(window,text=".",bg="white",fg="blue",width=5,height=1,font=("arial",15,"bold"),command=lambda:show(".")).place(x=10,y=300)
Button(window,text="0",bg="white",fg="blue",width=5,height=1,font=("arial",15,"bold"),command=lambda:show("0")).place(x=100,y=300)
Button(window,text="=",bg="white",fg="blue",width=10,height=1,font=("arial",15,"bold"),command=lambda:calculate()).place(x=200,y=300)


window.mainloop()
