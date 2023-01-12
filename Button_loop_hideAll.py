import tkinter as tk


def secondbtnAct():
    hideAll()
    txt02.pack()
    secondbtn.pack()


def thirdbtnAct():
    hideAll()
    txt03.pack()
    thirdbtn.pack()


def fourthbtnAct():
    hideAll()
    txt04.pack()
    fourthbtn.pack()


def hideAll():
    txt01.pack_forget()
    txt02.pack_forget()
    txt03.pack_forget()
    txt04.pack_forget()
    button.pack_forget()
    secondbtn.pack_forget()
    thirdbtn.pack_forget()
    fourthbtn.pack_forget()


root = tk.Tk()
root.geometry("600x600")

button = tk.Button(root, text="First button", command=secondbtnAct)
secondbtn = tk.Button(root, text="Second", command=thirdbtnAct)
thirdbtn = tk.Button(root, text="Third", command=fourthbtnAct)
fourthbtn = tk.Button(root, text="fourth", command=secondbtnAct)
txt01 = tk.Label(root, text="one")
txt02 = tk.Label(root, text="Two")
txt03 = tk.Label(root, text="three")
txt04 = tk.Label(root, text="fourth")

txt01.pack()
button.pack()


root.mainloop()
