import tkinter as tk


def back_button_callback():
    root.withdraw()
    import test_game01
    test_game01

    # Code to open the second menu with two buttons, back and Exit App
    pass


def exit_game_callback():
    root.withdraw()
    pass


root = tk.Tk()
back_button = tk.Button(root, text="back", command=back_button_callback)
quit_button = tk.Button(root, text="Exit Game", command=exit_game_callback)
back_button.pack()
quit_button.pack()
root.minsize(width=600, height=400)
root.maxsize(width=800, height=600)
