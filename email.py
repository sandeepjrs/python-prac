import smtplib
import getpass

default_email = 'sandeepjrs@gmail.com'
Recievers_list=['sandeepjrs@gmail.com','kushwaha.br1@gmail.com']
print """" the default sender Email id : sandeepjrs@gmail.com
press 'y' to confirm or 'n' to enter the  new email ID and password"""

user_responce= raw_input()

if user_responce is 'y' or 'Y':
	print "enter the password of the ",default_email
	user_email_ID=default_email
	user_password=getpass.getpass('Password:')
else:
	print "Enter the email ID  : "
	user_email_ID=raw_input()
	user_password=getpass.getpass('Password:')
	
	
sender = user_email_ID


subject="Subject: SMTP e-mail test \n"
message = "i am in body"
full_mail=subject+message


smtpObj = smtplib.SMTP('smtp.gmail.com',587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(sender,user_password)

for i in Recievers_list:	
	smtpObj.sendmail(sender,i, full_mail)         
	print "Successfully sent email to ",i

