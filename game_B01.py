import tkinter as tk


def myBtn():
    myBtn = tk.Button(root, text="MYBTN", command=myBtn2)
    myBtn.pack()


def myBtn2():
    myBtn2 = tk.Button(root, text="MYBTN2", command=myBtn)
    myBtn2.pack()


root = tk.Tk()
root.geometry("600x600")

button = tk.Button(root, text="Old button", command=myBtn)
button.pack()

root.mainloop()
