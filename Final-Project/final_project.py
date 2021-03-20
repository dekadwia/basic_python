#Import Package
#Source : https://github.com/samlopezf/Python-Email/blob/master/send_email.py
import smtplib
from email.mime.base import MIMEBase
from email import encoders
from email.message import EmailMessage

#Set email account and password
sender_mail = input("type your e-mail : ")
password = input("type your password : ")

#Open File from txt files
#Source : https://www.youtube.com/watch?v=wUH36iH8HlA
file = open("list_receiver_email.txt", "r")
rec_mail = []
for line in file :
    rec_mail.append(line.strip())
file.close()

'''
import file with 3 column in 1 row from txt file :

file = open("Email.txt", "r")
rec_mail = []
ages =[]
subjects = []

for line in file :
    splitLine = line.split(",")
    names.append(spliLine[0])
    ages.append(int(splitLine[1]))
    subjects.append(splitLine[2].strip()) -> to remove line spacing at the end of row
file.close()

'''

#Set Message : Subject, body e-mail
#Source : https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Emails/mail-demo.py 
msg = EmailMessage()
msg['Subject'] = 'Final Project'
msg['From'] = sender_mail
msg['To'] = rec_mail
msg.set_content('This is a plain text email')
msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is Anfield!</h1>
    </body>
</html>
""", subtype='html')

#Attachment File
#Source : https://github.com/samlopezf/Python-Email/blob/master/send_email.py 
filename='this_is_anfield.jpg'
attachment  =open(filename,'rb')
part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)

#Connect to gmail server, login and sent e-mail
#Source : https://github.com/samlopezf/Python-Email/blob/master/send_email.py
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(sender_mail, password)
server.sendmail(sender_mail, rec_mail, msg.as_string())