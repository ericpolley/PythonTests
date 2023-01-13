import tkinter as tk
import subprocess

global score
score = 0


def run_game():
    subprocess.run(["python", "pyglet_test02.py"])


def firstbtnAct():
    hideAll()
    countbtn.pack()
    subbtn.pack()
    txt01.pack()
    button.pack()
    txt01.place(relx=.5, rely=.3, anchor="center")
    countbtn.place(relx=.4, rely=.1, anchor="center")
    button.place(relx=.5, rely=.6, anchor="center")
    subbtn.place(relx=.6, rely=.1, anchor="center")


def secondbtnAct():
    hideAll()
    txt02.pack()
    secondbtn.pack()
    txt02.place(relx=.5, rely=.3, anchor="center")
    secondbtn.place(relx=.5, rely=.6, anchor="center")


def thirdbtnAct():
    hideAll()
    txt03.pack()
    thirdbtn.pack()
    txt03.place(relx=.5, rely=.3, anchor="center")
    thirdbtn.place(relx=.5, rely=.6, anchor="center")


def fourthbtnAct():
    hideAll()
    txt04.pack()
    fourthbtn.pack()
    txt04.place(relx=.5, rely=.3, anchor="center")
    fourthbtn.place(relx=.5, rely=.6, anchor="center")


def add():
    global score
    score += 1
    txt01.config(text=score)


def sub():
    global score
    score -= 1
    txt01.config(text=score)


def hideAll():
    txt01.pack_forget()
    txt02.pack_forget()
    txt03.pack_forget()
    txt04.pack_forget()
    txt01.place_forget()
    txt02.place_forget()
    txt03.place_forget()
    txt04.place_forget()
    button.pack_forget()
    secondbtn.pack_forget()
    thirdbtn.pack_forget()
    fourthbtn.pack_forget()
    button.place_forget()
    secondbtn.place_forget()
    thirdbtn.place_forget()
    fourthbtn.place_forget()
    countbtn.place_forget()
    subbtn.place_forget()


root = tk.Tk()

root.title("Game title the game")
root.geometry("1000x600")
root.config(bg='#BBBBBB')

countbtn = tk.Button(root, text="add", command=add,  bg="red", font=(
    "Helvetica", 32), justify="center", fg="white")
countbtn.pack()
countbtn.place(relx=.4, rely=.1, anchor="center")
subbtn = tk.Button(root, text="subtract", command=sub,  bg="red", font=(
    "Helvetica", 32), justify="center", fg="white")
subbtn.pack()
subbtn.place(relx=.6, rely=.1, anchor="center")

button = tk.Button(root, text="Start", command=secondbtnAct,
                   bg="blue", font=("Helvetica", 32), justify="center", fg="white")
secondbtn = tk.Button(root, text="Red", command=thirdbtnAct, bg="green", font=(
    "Helvetica", 32), justify="center", fg="white")
thirdbtn = tk.Button(root, text="Continue", command=fourthbtnAct, bg="red", font=(
    "Helvetica", 32), justify="center", fg="white")
fourthbtn = tk.Button(root, text="Okay", command=firstbtnAct, bg="orange", font=(
    "Helvetica", 32), justify="center", fg="black")
txt01 = tk.Label(root, text=score, bg="#BBBBFF", font=(
    "Helvetica", 32))

txt02 = tk.Label(root, text="What is red?", bg="#BBBBBB", font=(
    "Helvetica", 32))
txt03 = tk.Label(root, text="Great job!", bg="#BBBBBB", font=(
    "Helvetica", 32))
txt04 = tk.Label(root, text="Back to Menu?", bg="#BBBBBB", font=(
    "Helvetica", 32))

txt01.pack()
txt01.place(relx=.5, rely=.3, anchor="center")
button.pack()
button.place(relx=.5, rely=.6, anchor="center")

game_button = tk.Button(root, text="Open Game", command=run_game, bg="red", font=(
    "Helvetica", 32), justify="center", fg="white")
game_button.pack()
game_button.place(relx=.5, rely=.9, anchor="center")
root.mainloop()
