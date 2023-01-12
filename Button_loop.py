import tkinter as tk


def secondbtnAct():
    button.pack_forget()
    fourthbtn.pack_forget()
    secondbtn.pack()


def thirdbtnAct():
    secondbtn.pack_forget()
    thirdbtn.pack()


def fourthbtnAct():
    thirdbtn.pack_forget()
    fourthbtn.pack()


root = tk.Tk()
root.geometry("600x600")

button = tk.Button(root, text="First button", command=secondbtnAct)
secondbtn = tk.Button(root, text="Second", command=thirdbtnAct)
thirdbtn = tk.Button(root, text="Third", command=fourthbtnAct)
fourthbtn = tk.Button(root, text="fourth", command=secondbtnAct)

button.pack()

root.mainloop()
