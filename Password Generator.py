#TASK 3
#PASSWORD GENERATOR

import random
import string
import tkinter as tk

#FUNCTION
def generate():
    try:
        length=int(entry.get())
        characters=string.ascii_letters+string.digits+string.punctuation
        password=''
        for i in range(length):
            password+=random.choice(characters)
        label.configure(text='PASSWORD: '+password,fg='dark green',font=('Verdana', 15))
    except ValueError:
        label.configure(text="Error! Enter interger Value")

#UI        
root=tk.Tk()
root.geometry('320x320')
root.title("PASSWORD GENERATOR")
l1=tk.Label(root,text='PASSWORD GENERATOR',bg='light yellow',fg='dark red',\
            font=('Arial',17,'bold'),padx=10,pady=10)
l1.pack(pady=10)
l2=tk.Label(root,text='Enter Length:',fg='green',bg='light gray',font= ('Verdana', 15))
l2.pack(padx=10, pady=10)
entry=tk.Entry(root,width=10,font=('Tahama',15),justify='center')
entry.pack(padx=7, pady=7)
button=tk.Button(root,text='GENERATE',font=('Times new roman', 15, 'bold'),\
                 command=generate,width=12,bg='lightsteelblue')
button.pack(padx=7, pady=7)
label=tk.Label(root,text='PASSWORD:',fg='dark green',bg='silver',font=('Verdana',15,'bold'))
label.pack(padx=10, pady=10)
root.mainloop()

