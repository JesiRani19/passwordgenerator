


from tkinter import *
from tkinter import messagebox
import random
import string

window=Tk()
window.title("PasswordGenerator")
window.geometry("500x570")
window.config(bg="white")
topic=Label(window,text="Password Generator",fg="black",height=1,font=("times",15,"bold"))
topic.pack()
name=Label(window,text="Enter user name:",bg="white",fg="black",font=("times",15,"bold"))
name.place(x=10,y=100)
name_entry=Entry(window,bg="white",fg="black")
name_entry.place(x=200,y=100)

password_length=Label(window,text="Password Length:",bg="white",fg="black",font=("times",15,"bold"))
password_length.place(x=10,y=200)
password_length_entry=Entry(window,bg="white",fg="black")
password_length_entry.place(x=200,y=200)

password=Label(window,text="Genreated Password:",bg="white",fg="black",font=("times",15,"bold"))
password.place(x=10,y=300)
password_entry=Entry(window,bg="white",fg="black")
password_entry.place(x=200,y=300)

def pgFunc():
    n = password_length_entry.get()
    try:
        n = int(n)
    except:
        messagebox.showwarning("warning", "Please enter an digit.")
        return
    alphabet = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
    temp = alphabet + numbers + symbols
    result = "".join(random.choices(temp,k=n))
    # print(result)	
    password_entry.delete(0, END)
    password_entry.insert(0, result)

genpasswrd=Button(window,text="GENERATE PASSWORD",bg="blue",fg="white",padx=15,pady=5,font=("times",15,"bold"), command=pgFunc)
genpasswrd.place(x=200, y=400)

accept=Button(window,text="ACCEPT",bg="white",fg="Green",padx=10,pady=1,font=("times",15)).place(x=200,y=470)
reset=Button(window,text="RESET",bg="white",fg="green",padx=10,pady=1,font=("times",15)).place(x=200,y=530)


window.mainloop()
