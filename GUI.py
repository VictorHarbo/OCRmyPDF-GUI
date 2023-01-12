import subprocess
import time
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import tkinter.messagebox
from tkinter.ttk import Style
import customtkinter as ctk
import os
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
helpPage = ctk.CTkFrame(win)

# === Functions ===
# Define a function for switching the frames
def change_to_start():
   startPage.pack(fill='both', expand=TRUE, side=RIGHT)
   advancedSettings.pack_forget()
   helpPage.pack_forget()

def change_to_advancedSettings():
   advancedSettings.pack(fill='both', expand=TRUE, side=RIGHT)
   startPage.pack_forget()
   helpPage.pack_forget()

def change_to_helppage():
   helpPage.pack(fill='both', expand=TRUE, side=RIGHT)
   startPage.pack_forget()
   advancedSettings.pack_forget()

def select_file():
   filetypes = (
     ('PFD files', '*.pdf'),
     ('All files', '*.*')
   )

   filename1 = fd.askopenfilename(
      title='Open a file',
      initialdir='~/',
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
      language = "dan "
   elif languageBox.get() == "German":
      language = "deu "
   elif languageBox.get() == "French":
      language = "fre "
   else:
      language="eng "
   
   # Set second language param if not none
   if secondLanguageBox.get() == "Danish":
      secondLanguage = "+ dan "
   elif secondLanguageBox.get() == "German":
      secondLanguage = "+ deu "
   elif secondLanguageBox.get() == "English":
      secondLanguage = "+ eng "
   elif secondLanguageBox.get() == "French":
      secondLanguage = "+ fre "
   else:
      secondLanguage = ""

   # Check for forceToggle
   if forceToggle.get() == 1:
      forceOCR = "--force-ocr "
   else:
      forceOCR = ""
   
   printStatus()

   if __name__ == '__main__':  # To ensure correct behavior on Windows and macOS
      cmd = "ocrmypdf " +"-l "+ language + secondLanguage + "--output-type pdf " + forceOCR + inputVariable.get() + " " + outputVariable.get()
      subprocess.call(cmd, shell=True)
      if subprocess.CalledProcessError:
         runInfoLabel.configure(text="PDF file already has OCR. To rerun use 'Force OCR' setting.")

def printStatus():
   if inputVariable.get() == "" or outputVariable.get() == "":
      runInfoLabel.configure(text="Please set input and output files.")
   else:
      runInfoLabel.configure(text="Please wait while your file is scanned...")
   #except ocrmypdf.PriorOcrFoundError:
   #   runInfoLabel.config(text="Chosen text already has OCR. Use Force OCR to scan anyway.")

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

forceToggle = ctk.CTkCheckBox(master=runFrame, 
                              text="Force OCR")
forceToggle.pack(pady=5, side=TOP)

runInfoLabel = ctk.CTkLabel(runFrame, text = "Ready to OCR scan your file!")
runInfoLabel.pack(pady=5)


runButton = ctk.CTkButton(runFrame,
                           text='RUN',
                           command=run_program
                           )
runButton.pack(pady=5, side=BOTTOM)

# TODO: Add pop up message that says that the OCR process is finished
# TODO: Add more languages to the language picker

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

advancedSettingsTitle = ctk.CTkLabel(advancedSettingsTitleFrame, text="Advanced settings")
advancedSettingsTitle.pack(pady=20)
multipleLanguagesLabel = ctk.CTkLabel(advancedSettingsTitleFrame, text = "Multiple languages can be selected here:")
multipleLanguagesLabel.pack(pady=5)

secondLanguageLabel = ctk.CTkLabel(leftFrameAdvancedSettings, text="Second OCR Language")
secondLanguageLabel.pack(side=TOP, pady=5)

secondLanguageBox = ctk.CTkComboBox(master=rightFrameAdvancedSettings,
                              values=["none","English", "Danish", "German", "French"])
secondLanguageBox.pack(pady=5, side=TOP)


# === Left frame ===
leftTitel = ctk.CTkLabel(buttonFrame, text="OCRmyPDF")
leftTitel.pack(pady=5)

# Add buttons to left frame tat switch between the two right frames
btn1 = ctk.CTkButton(buttonFrame, text="OCRmyPDF", command=change_to_start)
btn1.pack(side=TOP, pady=5)
btn2 = ctk.CTkButton(buttonFrame, text="Advanced Settings", command=change_to_advancedSettings)
btn2.pack(side=TOP, pady=5)
btn3 = ctk.CTkButton(buttonFrame, text="Help", command=change_to_helppage)
btn3.pack(side=TOP, pady=5)

startPage.pack(fill='both', expand=TRUE, side=RIGHT)
win.mainloop()



