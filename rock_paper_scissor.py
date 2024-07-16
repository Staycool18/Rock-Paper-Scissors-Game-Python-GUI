from tkinter import *
from PIL import Image,ImageTk
from random import randint

root=Tk()
root.title("Rock Paper Scissor")
root.config(bg="light yellow")
root.geometry("970x350+200+0")
root.resizable(height=False, width=False)

rock_user_img=ImageTk.PhotoImage(Image.open("rock_user.png"))
paper_user_img=ImageTk.PhotoImage(Image.open("paper_user.png"))
scissor_user_img=ImageTk.PhotoImage(Image.open("scissor_user.png"))
rock_comp_img=ImageTk.PhotoImage(Image.open("rock_computer.png"))
paper_comp_img=ImageTk.PhotoImage(Image.open("paper_computer.png"))
scissor_comp_img=ImageTk.PhotoImage(Image.open("scissor_computer.png"))
profile_img=ImageTk.PhotoImage(Image.open("profile.png"))

user_label=Label(root, image=profile_img, bg="black")
comp_label=Label(root, image=profile_img, bg="black")
user_label.grid(row=1, column=0)
comp_label.grid(row=1, column=4)

user_score=Label(root, text=0, bd=10, font=100, bg="light blue", fg="black")
comp_score=Label(root, text=0, bd=10, font=100, bg="light blue", fg="black")
user_score.grid(row=1, column=1)
comp_score.grid(row=1, column=3)

rock=Button(root, width=15, height=2, bd=10, text="ROCK", font=40, bg="sky blue", fg="blue", command=lambda:updateChoice("rock"))
paper=Button(root, width=15, height=2, bd=10, text="PAPER", font=40, bg="sky blue", fg="blue", command=lambda:updateChoice("paper"))
scissor=Button(root, width=14, height=2, bd=10, text="SCISSOR", font=40, bg="sky blue", fg="blue", command=lambda:updateChoice("scissor"))
rock.grid(row=2, column=1)
paper.grid(row=2, column=2)
scissor.grid(row=2, column=3)

user_indicator=Label(root, font=50, text="USER", bg="black", fg="white")
comp_indicator=Label(root, font=50, text="COMPUTER", bg="black", fg="white")
user_indicator.grid(row=0, column=1)
comp_indicator.grid(row=0, column=3)

msg=Label(root, font=50, bg="light yellow", fg="purple")
msg.grid(row=3, column=2)

def updateMessage(x):
    msg["text"]=x
    
def updateUserScore():
    score=int(user_score["text"])
    score+=1
    user_score["text"]=str(score)
    
def updateCompScore():
    score=int(comp_score["text"])
    score+=1
    comp_score["text"]=str(score)
    
def checkWin(user,computer):
    if user==computer:
        updateMessage("It's a TIE!!!")
    elif user=="rock":
        if computer=="paper":
            updateMessage("YOU LOSE")
            updateCompScore()
        else:
            updateMessage("YOU WIN")
            updateUserScore()
    elif user=="paper":
        if computer=="scissor":
            updateMessage("YOU LOSE")
            updateCompScore()
        else:
            updateMessage("YOU WIN")
            updateUserScore()
    elif user=="scissor":
        if computer=="rock":
            updateMessage("YOU LOSE")
            updateCompScore()
        else:
            updateMessage("YOU WIN")
            updateUserScore()
    else:
        pass
    
choices=["rock", "paper", "scissor"]
def updateChoice(x):
    
    compChoice=choices[randint(0,2)]
    if compChoice=="rock":
        comp_label.configure(image=rock_comp_img)
    elif compChoice=="paper":
        comp_label.configure(image=paper_comp_img)
    else:
        comp_label.configure(image=scissor_comp_img)
    
    if x=="rock":
        user_label.configure(image=rock_user_img)
    elif x=="paper":
        user_label.configure(image=paper_user_img)
    else:
        user_label.configure(image=scissor_user_img)

    checkWin(x,compChoice)
    
root.mainloop()