#!/usr/bin/env python
# encoding: utf-8
"""
python_3_email_with_attachment.py
Created by Robert Dempsey on 12/6/14.
Copyright (c) 2014 Robert Dempsey. Use at your own peril.

This script works with Python 3.x

NOTE: replace values in ALL CAPS with your own values
"""

import os
import getopt,sys
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '

def main(argv):
    sender = ''
    gmail_password = ''
    recipients = []
    # List of attachments
    attachments = []

    # Create the enclosing (outer) message
    outer = MIMEMultipart()
    outer['Subject'] = ''
    outer['To'] = COMMASPACE.join(recipients)
    outer['From'] = sender
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    
    
    try:
      opts, args = getopt.getopt(sys.argv[1:],"hf:p:t:s:a:",["help", "from=","password=","to=","subject=","attachment="])
      #opts, args = getopt.getopt(argv,"hf:",["help", "from="])
    except getopt.GetoptError:
      print ('program.py -f <your@gmail.com> -p <your_gmail_password> -t <to@gmail.com> -s <subject> -a <attachmentNameWithExtension>')
      #python email3.py -f copyblogdown@gmail.com -p jurassic -t anurajram@gmail.com -s test -a scan.txt
        #sys.exit(2)
        
    for opt, arg in opts:
        print (opt,"==>",arg)
    for opt, arg in opts:
          if opt == '-h':
         #print 'program.py -f <your@gmail.com> -p <your_gmail_password> -t <to@gmail.com> -s <subject> -a <attachmentNameWithExtension>'
             sys.exit()
          elif opt in ("-f", "--from"):
             sender = arg
          elif opt in ("-p", "--password"):
             gmail_password = arg
          elif opt in ("-t", "--to"):
             recipients.append(arg)# = arg
          elif opt in ("-s", "--subject"):
             outer['Subject']  = arg
          elif opt in ("-a", "--attachment"):
             attachments.append(arg)# = arg
    
    # Add the attachments to the message
    print (sender,gmail_password,recipients,outer['Subject'],attachments)
    for file in attachments:
        try:
            print (file)
            with open(file, 'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            outer.attach(msg)
        except:
            print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
            raise

    composed = outer.as_string()

    # Send the email
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(sender, gmail_password)
        server.sendmail(sender, recipients, composed)
        server.close()
        print("Email sent!")
    except:
        print("Unable to send the email. Error: ", sys.exc_info()[0])
        raise

if __name__ == '__main__':
    main(sys.argv)
