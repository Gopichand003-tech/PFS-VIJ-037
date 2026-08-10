# Email Automation System with OTP Authentication
import random
import math
import smtplib

digits = "0123456789"
OTP = ""

for i in range(6):
    OTP += digits[math.floor(random.random() * 10)]
otp = OTP + " Idigo Nee OTP"
msg = otp

s = smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("chennapalligopichand@gmail.com","zdxk crpn hgbr vrbu")
user = "chennapalligopichand@gmail.com"
mailid = input("MAil Enter chey ra evariki pampalo : ")
s.sendmail(user,mailid,msg)

while True:
     a=input("Otp Enter chey: ")
     if a == OTP:
         print("Hmm correct ey!")
         exit
     else:
          print("Tappu Otp ra babu")
