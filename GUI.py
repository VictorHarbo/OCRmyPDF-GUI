import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# TODO:
# Input field - takes input pdf with full path
# Output field - Choose where to put output file
# Language option - Choose languages of input - can take multiple
# Advanced options - what should be included?
window = tk.Tk()

window.title("OCR my PDF")

label = ttk.Label(text="OCR my PDF!", background="")
label.pack()

def select_file():
    filetypes = (
        ('PDF files', '*.pdf'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='~/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )

open_button = ttk.Button(
    window,
    text='Open a File',
    command=select_file
)


open_button.pack(expand=True)

entry = tk.Entry(fg="yellow", bg="white", width=50)
entry.pack()

window.mainloop()


