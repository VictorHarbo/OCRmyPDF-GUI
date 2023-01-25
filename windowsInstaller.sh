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
