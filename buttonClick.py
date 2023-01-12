import tkinter as tk


def on_button_click():
    button.destroy()
    new_button = tk.Button(root, text="New button", command=lambda: None)
    new_button.pack()


root = tk.Tk()
root.geometry("600x600")

button = tk.Button(root, text="Old button", command=on_button_click)
button.pack()

root.mainloop()
