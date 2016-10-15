# GMAIL-SMTP-SSL-WITH-ATTACHMENT
Gmail sender with SSL and attachment

Aim is to make a standalone gmail sender executable for Windows OS. It support SSL with port 456. I started with gmail port 587. But is thrown error continously, then changed to 456. 
Script supports only gmail sender account; none other tried.
Executable takes runtime parameters like sender's email and password, Receiver's email, subject of email and one attachment. All the attributes are not optional. To execute it we need a batch file with these arguments. 
Sample of Bat file is below:
-------------------------------------------------
email30.exe -f from_sender@gmail.com -p anuraj -t to_receiver@gmail.com -s subject_test -a attach_scan.txt
-------------------------------------------------
Source code is provided.
It is compiled in pyinstaller using command: pyinstaller --onefile email3.py

