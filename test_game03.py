import tkinter as tk


def start_game():
    new_window = tk.Tk()
    # do your stuff in the new window
    new_window.mainloop()


def pause_button_callback():
    # Code to open the second menu with two buttons, back and Exit App
    pass


def exit_game_callback():
    root.destroy()
    pass


root = tk.Tk()
pause_button = tk.Button(root, text="Pause2", command=pause_button_callback)
quit_button = tk.Button(root, text="Exit Game2", command=exit_game_callback)
pause_button.pack()
quit_button.pack()
root.mainloop()
