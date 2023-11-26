import re
from tkinter import *
from tkinter import ttk, messagebox

from client import client


def validate(*args):
    result = client(alphabet_input.get())

    if "Goodbye" in result:
        show_message_box(result, "Game Over")
        exit()
    else:
        show_message_box(result, "Correct")
        prev_label.set(f"Previous Letter: {alphabet_input.get()}")
        alphabet_input.set("")


def show_message_box(message, title=""):
    messagebox.showinfo(title, message)


def limitInputSize(*args):
    value = alphabet_input.get()

    p = re.compile('[a-zA-Z]')

    if len(value) > 1:
        alphabet_input.set(value[:1])

    if p.match(value) is None:
        alphabet_input.set("")


root = Tk()
root.title('Alphabet "Game"')
root.resizable(False, False)

window_height = 100
window_width = 280

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

validate_cmd = root.register(limitInputSize)

previous_letter = "Previous letter: "

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

alphabet_input = StringVar()
alphabet_input.trace("w", limitInputSize)
alphabet_entry = ttk.Entry(mainframe, width=7, textvariable=alphabet_input, validatecommand=(validate_cmd, '%P'))
alphabet_entry.grid(column=2, row=1, columnspan=2, sticky=(W, E))

ttk.Button(mainframe, text="Validate", command=validate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Enter your alphabet: ").grid(column=1, row=1, sticky=W)

prev_label = StringVar()
prev_label.set("")
label = ttk.Label(mainframe, textvariable=prev_label).grid(column=1, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

alphabet_entry.focus()
root.bind("<Return>", validate)

root.mainloop()
