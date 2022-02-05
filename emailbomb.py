print( )

print( )
print( )


import smtplib
import time

print("×××××××Created By Mamun××××××××××")
print( )
print("#################################")
print( )
print("  github: ariyanahmedmamun    ")

print( )
print("Facebook: https://www.facebook.com/Cyber.Expert.Mamun")
print("------------------------------------------------")



print( )

print( )
print( )

mail=smtplib.SMTP('smtp.gmail.com',587)


email=str(input("Enter your gmail address: "))
print("Your Email is :"+email)
print( )
print( )

password=input("Enter your gmail_password: ")
print("Your Password is :"+password)
print( )
print( )


bmail=input("Enter Your Target Email : ")
print("Your Target Mail is :"+bmail)
print( )
print( )


message=input("Enter Message: ")
print( )
print( )


counter=(input("Enter Your Ammount :"))
print("Your Ammount is :"+counter)
print( )
print( )
s=input('Select the service provider (Gmail / Outlook): ').lower()
print("Method :"+s)
print( )
print( )

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
