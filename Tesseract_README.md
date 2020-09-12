## Installing Tesseract

[Tesseract](https://github.com/tesseract-ocr)  is an optical character recognition engine for various operating systems. It is free software, released under the Apache License. Originally developed by Hewlett-Packard as proprietary software in the 1980s, it was released as open source in 2005 and development has been sponsored by Google since 2006.

In this app pytesseract - a python library for implementing Tesseract ocr on Snipped Images

A Tesseract Installer(tesseract-ocr-w64-setup-<version>.exe) will be copied to installation folder from where user can to install it manually or download desired version from this [link](https://digi.bib.uni-mannheim.de/tesseract/).

### To use Tesseract as standalone program
To use just the Tesseract through commandline user will have to setup some Environment variables for which instructions are:

1. Create new enviorment variable named **TESSDATA_PREFIX** and assign the path of tessdata directory inside Tesseract installation directory.

2. Add  the path of your installation directory to the **PATH** environment variable

**This app will work fine if tesseract is installed in the default location, other wise user will have to setup the Environment variables as mentioned above**
