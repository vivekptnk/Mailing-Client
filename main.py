import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
 
server = smtplib.SMTP('smtp.gmail.com', 25) # Set up SMTP server 

# Start Server
server.ehlo()
server.starttls()

with open('password.txt', 'r') as f: # import password from your password.txt
    password = f.read()

with open('email.txt', 'r') as f: # import email from your password.txt
    email = f.read()

server.login(email, password) # login using email, password

msg = MIMEMultipart()
msg['From'] = 'Vivek Pattanaik' # Add your name here
msg['To'] = 'testingmailforvivek@spaml.de' # Just a spam email reciever for testing, you can replace with the person you want to send.
msg['Subject'] = 'Test' # Subject for your email

# open your email message
with open('mailmessage.txt', 'r') as f : 
    message = f.read()

msg.attach(MIMEText(message, 'plain')) # Attach the message to the email using MIMEText 

# set up attahment you want to add to the email
filename = 'mailimage.jpeg'
attachment = open(filename, 'rb')

# Attach payload using MIMEBase
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

# Encode and add header 
encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename = {filename}')
msg.attach(p)

text = msg.as_string()

server.sendmail(email, 'testingmailforvivek@spaml.de', text)