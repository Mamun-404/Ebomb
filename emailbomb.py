import smtplib
import time




mail=smtplib.SMTP('smtp.gmail.com',587)



email=str(input("Enter your gmail address: "))
password=input("Enter your gmail_password: ")
bmail=input("Enter Your Target Email : ")
message=input("Enter Message: ")
counter=int(input("How many message you want to send?: "))
s=input('Select the service provider (Gmail / Outlook): ').lower()



if s=="gmail":
	mail=smtplib.SMTP('smtp.gmail.com','587')
elif s_ == "outlook":
	mail = smtplib.SMTP('smtp.office365.com',587)

for x in range(0,counter):
	print("Number of Message Sent : ", x+1)
	
mail.ehlo()
mail.starttls()
mail.login(email,password)
mail.sendmail(email,bmail,message)