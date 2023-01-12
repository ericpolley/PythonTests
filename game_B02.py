import tkinter as tk


def firstbtnAct():
    hideAll()
    txt01.pack()
    button.pack()
    txt01.place(relx=.5, rely=.3, anchor="center")
    button.place(relx=.5, rely=.6, anchor="center")


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


root = tk.Tk()

root.title("Game title the game")
root.geometry("900x600")
root.config(bg='#BBBBBB')

button = tk.Button(root, text="Start", command=secondbtnAct,
                   bg="blue", font=("Helvetica", 32), justify="center", fg="white")
secondbtn = tk.Button(root, text="Red", command=thirdbtnAct, bg="green", font=(
    "Helvetica", 32), justify="center", fg="white")
thirdbtn = tk.Button(root, text="Continue", command=fourthbtnAct, bg="red", font=(
    "Helvetica", 32), justify="center", fg="white")
fourthbtn = tk.Button(root, text="Okay", command=firstbtnAct, bg="orange", font=(
    "Helvetica", 32), justify="center", fg="black")
txt01 = tk.Label(root, text="Game Title - the game", bg="#BBBBFF", font=(
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

root.mainloop()
