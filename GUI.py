from tkinter import *
from tkinter import font
import tkinter.messagebox
from tkinter.ttk import Style
import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Create an instance of tkinter frame or window
win = ctk.CTk()

# Set the size of the window
win.geometry("700x350")

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

#TODO: Figure out if styles are actually of use to me
# === Styles ===
headingStyle = Style()
headingStyle.configure(style='headingStyle', font=('Arial', 16, 'bold'))

# === Right frames ===
# Add content to right frames
label1 = ctk.CTkLabel(startPage, text="Basic usage here")
label1.pack(pady=20)
#TODO Add input file box
#TODO Add language drop down menu - should these be checkboxes?
#TODO Add output file box

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




