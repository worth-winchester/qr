# qr

Author: Worth Winchester

Description: This project is meant to be a command and control setup that makes use of QR code image files instead of socket communication.
These QR code image files are hosted on one computer and downloaded and decoded on a second computer.
The QR codes contained in the image files will have the encoded commands meant to be run on the second computer.
The program qrApp.py is a Python Flask web application that generates and displays an image of a QR code.
The program qrReader.py will download the QR code image file and decode the terminal command from the image file.
Then, it will execute the command in a terminal and then repeat in a loop.
The user of qrApp.py can update the QR code image by supplying a query string to the web application.
The format for the query string is: cmd=desired terminal command
The following is an example of passing the query string: 127.0.0.1/cmd=xdg-open https://github.com/worth-winchester 
