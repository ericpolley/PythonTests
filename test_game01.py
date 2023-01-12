import tkinter as tk


def start_button_callback():
    root.withdraw()
    import test_game02
    test_game02
    pass


def exit_app_callback():
    root.destroy()
    pass


root = tk.Tk()
root.minsize(width=600, height=400)
root.maxsize(width=800, height=600)
start_button = tk.Button(root, text="Start", command=start_button_callback)
exit_button = tk.Button(root, text="Exit App", command=exit_app_callback)
start_button.pack()
exit_button.pack()

root.mainloop()
