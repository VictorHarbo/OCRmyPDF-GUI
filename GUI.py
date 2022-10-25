from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import tkinter.messagebox
from tkinter.ttk import Style
import customtkinter as ctk
import ocrmypdf

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Create an instance of tkinter frame or window
win = ctk.CTk()

# === GLOBAL VARIABLES ===
inputVariable = StringVar()
outputVariable = StringVar()

# Set the size of the window
win.geometry("700x350")
win.title("OCRmyPDF")

# Create leftframe for buttons
buttonFrame = ctk.CTkFrame(win)
buttonFrame.pack(side=LEFT, fill='both')

# Create two frames to the right in the window
startPage = ctk.CTkFrame(win)
advancedSettings = ctk.CTkFrame(win)

# === Functions ===
# Define a function for switching the frames
def change_to_start():
   startPage.pack(fill='both', expand=TRUE, side=RIGHT)
   advancedSettings.pack_forget()

def change_to_advancedSettings():
   advancedSettings.pack(fill='both', expand=TRUE, side=RIGHT)
   startPage.pack_forget()

def select_file():
   filetypes = (
     ('PFD files', '*.pdf'),
     ('All files', '*.*')
   )

   filename1 = fd.askopenfilename(
      title='Open a file',
      initialdir='~',
      filetypes=filetypes
   )

   inputVariable.set(filename1)

def save_file():
   filetypes = (
      ('PDF files', '*.pdf'),
      ('All files', '*.*')
   )

   filename2 = fd.asksaveasfilename(
      title='Open a file',
      initialdir='~',
      filetypes=filetypes
   )
   outputVariable.set(filename2)

# === Right frames ===
# Add content to right frames
# = Main frame =
label1 = ctk.CTkLabel(startPage, text="Basic usage here")
label1.pack(pady=5)

inputButton = ctk.CTkButton(
   startPage,
   text='Input file',
   command=select_file
)

outputButton = ctk.CTkButton(
   startPage,
   text='Output file',
   command=save_file
)

inputButton.pack(expand=True, side=LEFT)
outputButton.pack(expand=True, side=RIGHT)

inputEntry = ctk.CTkEntry(startPage, textvariable = inputVariable)
inputEntry.pack(pady=5, side=LEFT)

outputEntry = ctk.CTkEntry(startPage, textvariable= outputVariable)
outputEntry.pack(pady=5, side=RIGHT)

#TODO Add language drop down menu - should these be checkboxes?
#TODO Add RUN button
#TODO Send input and output to command line OCRmyPDF


# = Advanced settings =
label2 = ctk.CTkLabel(advancedSettings, text="Advanced settings here")
label2.pack(pady=20)
#TODO: Advanced options - what should be included?

# === Left frame ===
leftTitel = ctk.CTkLabel(buttonFrame, text="OCRmyPDF")
leftTitel.pack()
# Add buttons to left frame tat switch between the two right frames
btn1 = ctk.CTkButton(buttonFrame, text="OCRmyPDF", command=change_to_start)
btn1.pack(side=TOP, pady=5)
btn2 = ctk.CTkButton(buttonFrame, text="Advanced Settings", command=change_to_advancedSettings)
btn2.pack(side=TOP, pady=5)
# TODO: Add title label

startPage.pack(fill='both', expand=TRUE, side=RIGHT)
win.mainloop()



