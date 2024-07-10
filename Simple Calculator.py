#TASK 3
#CALCULATOR PROGRAM

import tkinter as tk
from tkinter import messagebox

#FUNCTIONS
def add():
    try:
        n1=float(entryl1.get())
        n2=float(entryl2.get())
        answer=n1+n2
        resultlabel.configure(text='RESULT:'+str(answer))
    except ValueError:
        messagebox.showerror('ERROR!', 'Please enter valid numbers')
def substract():
    try:
        n1=float(entryl1.get())
        n2=float(entryl2.get())
        answer=n1-n2
        resultlabel.configure(text='RESULT:'+str(answer))
    except ValueError:
        messagebox.showerror('ERROR!', 'Please enter valid numbers')
def multiply():
    try:
        n1=float(entryl1.get())
        n2=float(entryl2.get())
        answer=n1*n2
        resultlabel.configure(text='RESULT:'+str(answer))
    except ValueError:
        messagebox.showerror('ERROR!', 'Please enter valid numbers')
def divide():
    try:
        n1=float(entryl1.get())
        n2=float(entryl2.get())
        if n2==0:
            messagebox.showerror('ERROR!', 'Division by 0 is not possible')
        else:
            answer=n1/n2
            resultlabel.configure(text='RESULT:'+str(answer))
    except ValueError:
        messagebox.showerror('ERROR!', 'Please enter valid number')        
    
#UI
root=tk.Tk()
root.title('SIMPLE CALCULATOR')
root.geometry('300x350')

label1=tk.Label(root,text='Enter first number:',fg='blue',font=('Arial',15))
label1.pack()
entryl1=tk.Entry(root,width=10,font=('Helvetica', 15),justify='center')
entryl1.pack()
label2=tk.Label(root,text='Enter second number:',fg='blue',font=('Arial',15))
label2.pack()
entryl2=tk.Entry(root,width=10,font=('Helvetica', 15),justify='center')
entryl2.pack()
entryl1.bind("<Return>",lambda event: entryl2.focus_set())
addbutton=tk.Button(root,text='ADD: + ',command=add,bg='white',width=11)
addbutton.pack(padx=5,pady=5)
subbutton=tk.Button(root,text='SUBSTRACT: -',command=substract,bg='white',width=11)
subbutton.pack(pady=5)
multiplybutton=tk.Button(root,text='MULTIPLY: *',command=multiply,bg='white',width=11)
multiplybutton.pack(pady=5)
dividebutton=tk.Button(root,text='DIVIDE: /',command=divide,bg='white',width=11)
dividebutton.pack(pady=5)
resultlabel=tk.Label(root,text='RESULT:',fg='dark red',bg='light cyan', font=('Times new roman', 22, 'bold'))
resultlabel.pack(padx=17, pady=22)
root.mainloop()
