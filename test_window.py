import tkinter as tk

# Create the main window
window = tk.Tk()
window.geometry('400x400')
window.configure(bg="blue")

# Add a label to display text
label = tk.Label(text='Click the button to close the window')
label.pack()

# Add a button to close the window
button = tk.Button(text='Close', command=window.destroy)
button.configure(height=8)
button.pack()

# Run the Tkinter event loop
window.mainloop()
