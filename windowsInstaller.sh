# Install chocolatey package manager
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install packages through chocolatey
# First install python
echo "Installing python: "
choco install python3

# Then install tesseract
echo "Installing tesseract: "
choco install --pre tesseract

# Followed by installation of ghostscript
echo "Installing ghostscript: "
choco install ghostscript

# Then we install pngquant
echo "Installing pngquant"
choco install pngquant

# Restart shell
exec $SHELL

# Installing ocrmypdf
echo "Installing OCRmyPDF"
pip install ocrmypdf

echo "OCRmyPDF has now been installed on your computer"
echo "Installing languages for OCRmyPDF"

# Downloading languages:
# Danish language
curl -LJO https://raw.githubusercontent.com/tesseract-ocr/tessdata/main/dan.traineddata
# German language
curl -LJO https://raw.githubusercontent.com/tesseract-ocr/tessdata/main/deu.traineddata
# French language
curl -LJO https://raw.githubusercontent.com/tesseract-ocr/tessdata/main/fra.traineddata
# Move langfiles to tessdata folder: 
mv dan.traineddata C:\\Program Files\\Tesseract-OCR\\tessdata\\dan.traineddata
mv deu.traineddata C:\\Program Files\\Tesseract-OCR\\tessdata\\deu.traineddata
mv fra.traineddata C:\\Program Files\\Tesseract-OCR\\tessdata\\fra.traineddata
