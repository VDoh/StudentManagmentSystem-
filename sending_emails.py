#!/usr/bin/env python3
import smtplib


class Mail:

    def __init__(self, emailUser, to , pasword, subject, text):
        self.EmailUser = emailUser
        self.Password = pasword
        self.Subject = subject
        self.Message = text

    def send_mail(self, emailUser, to, password, subject, text):
        
        TO = [to] #must be a list

        message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (emailUser, ", ".join(TO), subject, text)

        try:
            #server = smtplib.SMTP(SERVER) 
            server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
            server.ehlo()
            server.starttls()
            server.login(emailUser, password)
            server.sendmail(emailUser, TO, message)
            #server.quit()
            server.close()
            print ("successfully sent the mail")
        except:
            print ("failed to send mail")

print("Enter your email")
emailUser = input()

print("Enter your password")
password = input()

print("Enter your friend's Email")
to = input()

print("Enter Subject ")
subject = input()

print("Enter Your text mail")
text = input()

mail1 = Mail(emailUser, to ,password, subject, text )
mail1.send_mail(emailUser, to, password, subject, text)