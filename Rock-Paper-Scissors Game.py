#TASK 4
#ROCK-PAPER-SCISSORS GAME

import random
import tkinter as tk
from tkinter import messagebox

#GAME
def game(user):
    global pscore,cscore
    choices = ["ROCK", "PAPER", "SCISSORS"]
    computer= random.choice(choices)
    if user==computer:
        label1.configure(font=('verdana',17),text=f"GAME TIED \n YOU : {user} \n \
COMPUTER : {computer}",bg='white',fg='dark olive green')
    elif (user=='ROCK' and computer=='PAPER')or\
         (user=='SCISSORS' and computer=='ROCK') or\
         (user=='PAPER' and computer=='SCISSORS'):
        label1.configure(text=f"YOU LOSE \n YOU : {user} \n COMPUTER : {computer}",\
                         font=('verdana',17),bg='white',fg='dark olive green')
        cscore+=1
    else:
        label1.configure(text=f"YOU WON \n YOU : {user} \n COMPUTER : {computer}",\
                         font=('verdana',17),bg='white',fg='dark olive green')
        pscore+=1
    l2.configure(text=f"Your Score: {pscore}",bg='ivory3',padx=7,pady=7,fg='navy',font=('Helvetica',15),width=18)
    l3.configure(text=f"Computer Score: {cscore}",bg='ivory3',padx=7,pady=7,fg='navy',font=('Helvetica',15),width=18)
    result=messagebox.askquestion("Question","Do you want to play again?")
    if result=='no':
        if pscore>cscore:
            messagebox.showinfo("Scorecard","CONGRATULATIONS! YOU WON!")
        elif pscore==cscore:
            messagebox.showinfo("Scorecard","  GAME TIED!   ")
        else:
            messagebox.showinfo("Scorecard","SORRY! YOU LOSE!")
        root.destroy()
    else:
        label1.configure(text='CLICK to PLAY!',font=('verdana',17),bg='white',fg='dark olive green')
def resetgame():
    global pscore,cscore
    pscore=0
    cscore=0
    l2.configure(text=f"Your Score: {pscore}",bg='ivory3',padx=7,pady=7,fg='navy',font=('Helvetica',15),width=18)
    l3.configure(text=f"Computer Score: {cscore}",bg='ivory3',padx=7,pady=7,fg='navy',font=('Helvetica',15),width=18)
    label1.configure(text='CLICK to PLAY!',font=('verdana',17),bg='white',fg='dark olive green')
        
pscore=0
cscore=0

#UI
root=tk.Tk()
root.geometry('450x470')
root.title('ROCK PAPER SCISSOR')
root.configure(bg='rosy brown')
l1=tk.Label(root,text='ROCK-PAPER-SCISSORS!',bg='light gray',fg='Brown',\
            font=("Courier New", 22, "bold"),padx=10,pady=10)
l1.pack(padx=10,pady=10)
label1=tk.Label(root,text='CLICK to PLAY!',font=('verdana',17),bg='white',fg='dark olive green')
label1.pack(padx=10,pady=10)
frame=tk.Frame(root,height=100,bg='rosy brown')
frame.pack(padx=10,pady=10)
rock=tk.Button(frame,text='ROCK',font=('arial',15,'bold'),padx=8,pady=8,\
               bg='thistle3',fg='violetred4',command=lambda :game("ROCK"))
paper=tk.Button(frame,text='PAPER',font=('arial',15,'bold'),padx=8,pady=8,\
                bg='lightpink1',fg='purple4',command=lambda :game("PAPER"))
scissor=tk.Button(frame,text='SCISSOR',font=('arial',15,'bold'),padx=8,pady=8,\
                  fg='brown4',bg='azure3',command=lambda:game("SCISSORS"))
rock.pack(side=tk.LEFT,padx=10,pady=10)
paper.pack(side=tk.LEFT,padx=10,pady=10)
scissor.pack(side=tk.LEFT,padx=10,pady=10)
l2=tk.Label(root,text=f"Player Score: {pscore}",bg='ivory3',padx=7,\
            pady=7,fg='navy',font=('Helvetica',15),width=18)
l2.pack()
l3=tk.Label(root,text=f"Computer Score: {cscore}",bg='ivory3',padx=7,\
            pady=7,fg='navy',font=('Helvetica',15),width=18)
l3.pack()
reset=tk.Button(root,text='RESET GAME',font=('Times new roman',20,'bold'),\
                width=12,padx=5,pady=5,bg='lightblue3',fg='red4',command=resetgame)
reset.pack(padx=10,pady=20)

root.mainloop()


