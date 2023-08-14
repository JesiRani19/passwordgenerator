from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)
    temp_edit.delete(0, "end")

def editTask():
    edit_task = temp_edit.get()
    for item in lb.curselection():
        lb.delete(item)
        lb.insert("end", edit_task)
    temp_edit.delete(0, "end")

def items_selected(event):
    # get all selected indices
    selected_indices = lb.curselection()

    # get selected items
    selected_langs = ",".join([lb.get(i) for i in selected_indices])
    temp_edit.delete(0,END)
    temp_edit.insert(0,selected_langs)
    

ws = Tk()
ws.geometry('700x550+500+200')
ws.title('Todo-App')
ws.config(bg='black')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

task_list = []

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)
lb.bind('<<ListboxSelect>>', items_selected)
my_entry = Entry(
    ws,
    font=('times', 24)
    )

my_entry.pack(pady=20)

temp_edit = Entry(
ws,
font=('times', 24),
textvariable=ANCHOR
)
temp_edit.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

editTask_btn = Button(
    button_frame,
    text='Edit Task',
    font=('times 14'),
    bg='blue',
    padx=30,
    pady=10,
    command=editTask
)
editTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()
