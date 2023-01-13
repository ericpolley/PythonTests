import tkinter as tk
import pickle


def save_data(counter):
    with open("pickle/counter.pickle", "wb") as f:
        pickle.dump(counter, f)


def load_data():
    try:
        with open("pickle/counter.pickle", "rb") as f:
            return pickle.load(f)
    except:
        return 0


def on_button_click():
    global counter
    counter += 1
    counter_label.config(text="Counter: " + str(counter))
    save_data(counter)


app = tk.Tk()
app.title("Counter App")
app.geometry("600x600")

counter = load_data()

counter_label = tk.Label(app, text="Counter: " +
                         str(counter), bg="white", font=("Arial", 36), fg="black")
counter_label.pack()

button = tk.Button(app, text="Click me!",
                   command=on_button_click, bg="black", fg="white", font=("Arial", 36))
button.pack()

app.mainloop()
