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

def run_program():
   # Set language param
   if languageBox.get() == "Danish":
      language = "dan"
   elif languageBox.get() == "German":
      language = "deu"
   else:
      language="eng"

   if __name__ == '__main__':  # To ensure correct behavior on Windows and macOS
      ocrmypdf.ocr(input_file=inputVariable.get(), 
                     output_file=outputVariable.get(),
                     language=language, 
                     output_type= "pdf",
                     force_ocr=TRUE)

# === Right frames ===
# Add content to right frames
# = Main frame =
rightTitleFrame = ctk.CTkFrame(startPage)
leftFrame = ctk.CTkFrame(startPage)
rightFrame = ctk.CTkFrame(startPage)
runFrame = ctk.CTkFrame(startPage)
rightTitleFrame.pack(side=TOP, fill="both")
runFrame.pack(side=BOTTOM, fill="both")
leftFrame.pack(side=LEFT, expand=TRUE, fill="both")
rightFrame.pack(side=RIGHT, expand=TRUE, fill="both")


label1 = ctk.CTkLabel(rightTitleFrame, text="Basic usage here")
label1.pack(pady=5)

inputButton = ctk.CTkButton(
   leftFrame,
   text='Input file',
   command=select_file
)

outputButton = ctk.CTkButton(
   leftFrame,
   text='Output file',
   command=save_file
)

inputButton.pack(side=TOP, pady=5)
outputButton.pack(side=TOP, pady=5)

inputEntry = ctk.CTkEntry(rightFrame, textvariable = inputVariable)
inputEntry.pack(pady=5, side=TOP)

outputEntry = ctk.CTkEntry(rightFrame, textvariable= outputVariable)
outputEntry.pack(pady=5, side=TOP)

languageLabel = ctk.CTkLabel(leftFrame, text="Language")
languageLabel.pack(pady=5, side=TOP)
languageBox = ctk.CTkComboBox(master=rightFrame,
                              values=["English", "Danish", "German", "French"])
languageBox.pack(pady=5, side=TOP)

runButton = ctk.CTkButton(runFrame,
                           text='RUN',
                           command=run_program
                           )
runButton.pack(pady=5, side=BOTTOM)

# TODO: Add progressbar for OCR progress
# Progress bar is showing, but is not following the OCR progress
pb = ctk.CTkProgressBar(
   runFrame,
   orient="horizontal",
   mode="determinate"
)
pb.set(0)
pb.pack(side=TOP)
# TODO: Add more languages to the language picker
# TODO: Add functionality for two languages - maybe advanced setting
# TODO: Add funtionality to redo OCR


# = Advanced settings =
#TODO: Advanced options - what should be included?
advancedSettingsTitleFrame = ctk.CTkFrame(advancedSettings)
leftFrameAdvancedSettings = ctk.CTkFrame(advancedSettings)
rightFrameAdvancedSettings = ctk.CTkFrame(advancedSettings)
runFrameAdvancedSetting = ctk.CTkFrame(advancedSettings)
advancedSettingsTitleFrame.pack(side=TOP, fill="both")
runFrameAdvancedSetting.pack(side=BOTTOM, fill="both")
leftFrameAdvancedSettings.pack(side=LEFT, expand=TRUE, fill="both")
rightFrameAdvancedSettings.pack(side=RIGHT, expand=TRUE, fill="both")

label2 = ctk.CTkLabel(advancedSettingsTitleFrame, text="Advanced settings here")
label2.pack(pady=20)

multiLanguageCheck = ctk.CTkCheckBox(leftFrameAdvancedSettings, text= "Multiple languages")
multiLanguageCheck.pack()


# === Left frame ===
leftTitel = ctk.CTkLabel(buttonFrame, text="OCRmyPDF")
leftTitel.pack(pady=5)

# Add buttons to left frame tat switch between the two right frames
btn1 = ctk.CTkButton(buttonFrame, text="OCRmyPDF", command=change_to_start)
btn1.pack(side=TOP, pady=5)
btn2 = ctk.CTkButton(buttonFrame, text="Advanced Settings", command=change_to_advancedSettings)
btn2.pack(side=TOP, pady=5)
# TODO: Add title label

startPage.pack(fill='both', expand=TRUE, side=RIGHT)
win.mainloop()



