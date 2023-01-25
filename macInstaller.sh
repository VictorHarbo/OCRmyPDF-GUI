# Check if homebrew is installed then either install or update homebrew
if [[ $(command -v brew) == "" ]]; then
    echo "Installing Hombrew"
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
else
    echo "Updating Homebrew"
    brew update
fi

# Installation of OCRmyPDF command line tool
brew install ocrmypdf

# Now we need to install languageas
brew install tesseract-lang  

echo "OCRmyPDF has now been installed on your computer"