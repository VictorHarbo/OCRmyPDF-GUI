import subprocess
import customtkinter as ctk
from tkinter import *
from tkinter import filedialog as fd

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

# Create three frames to the right in the window
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

def preExecute():
      runInfoLabel.configure(text="Your file is now getting OCR scanned. Please wait...")

def execute():
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

   if __name__ == '__main__':  # To ensure correct behavior on Windows and macOS
      cmd = "ocrmypdf " +"-l "+ language + secondLanguage + "--output-type pdf " + forceOCR + inputVariable.get() + " " + outputVariable.get()
      p = subprocess.call(cmd, shell=True)
      
      # Error handling, copied from: https://ocrmypdf.readthedocs.io/en/v11.7.0/advanced.html#return-code-policy
      if p == 1:
         runInfoLabel.configure(text="Invalid arguments, exited with an error.")
      elif p == 2:
         runInfoLabel.configure(text="The input file does not seem to be a valid PDF")
      elif p == 3:
         runInfoLabel.configure(text="An external program required by OCRmyPDF is missing.")
      elif p == 4:
         runInfoLabel.configure(text="An output file was created, but it does not seem to be a valid PDF. The file will be available.")
      elif p == 5:
         runInfoLabel.configure(text="The user running OCRmyPDF does not have sufficient permissions to read the input file and write the output file.")
      elif p == 6:
         runInfoLabel.configure(text="The file already appears to contain text so it may not need OCR.\n Use Force OCR to scan anyways.")
      elif p == 7:
         runInfoLabel.configure(text="An error occurred in an external program (child process) and OCRmyPDF cannot continue.")
      elif p == 8:
         runInfoLabel.configure(text="The input PDF is encrypted. OCRmyPDF does not read encrypted PDFs.")
      elif p == 9:
         runInfoLabel.configure(text="A custom configuration file was forwarded to Tesseract using --tesseract-config,\nand Tesseract rejected this file.")
      elif p == 10:
         runInfoLabel.configure(text="A valid PDF was created, PDF/A conversion failed. \nThe file will be available.")
      elif p == 15:
         runInfoLabel.configure(text="An unknown error occurred.")
      elif p == 130:
         runInfoLabel.configure(text="The program was interrupted by pressing Ctrl+C.")
      else: 
         runInfoLabel.configure(text="Your file has been OCR scanned.")


def run_program():
   preExecute()
   execute()

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

runButton = ctk.CTkButton(runFrame,
                           text='RUN',
                           command=run_program
                           )
runButton.pack(pady=5, side=BOTTOM)

runInfoLabel = ctk.CTkLabel(runFrame, text = "Ready to OCR scan your file!")
runInfoLabel.pack(pady=5)

# TODO: Add more languages to the language picker
# TODO: Write bash (or python scripts for installation of prerequisits on mac and windows)

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

#TODO: What should be written in info?

# === Left frame ===
leftTitel = ctk.CTkLabel(buttonFrame, text="OCRmyPDF")
leftTitel.pack(pady=5)

# Add buttons to left frame tat switch between the two right frames
btn1 = ctk.CTkButton(buttonFrame, text="OCRmyPDF", command=change_to_start)
btn1.pack(side=TOP, pady=5)
btn2 = ctk.CTkButton(buttonFrame, text="Advanced Settings", command=change_to_advancedSettings)
btn2.pack(side=TOP, pady=5)
btn3 = ctk.CTkButton(buttonFrame, text="Info", command=change_to_helppage)
btn3.pack(side=TOP, pady=5)

startPage.pack(fill='both', expand=TRUE, side=RIGHT)
win.mainloop()