# Coded by MasterJonJon & the NTI Koding Team
import smtplib as s
import time
username = "Enter gmail username here"
password = "Enter gmail password here"
print"\n\r\n\rWelcome to Jon Paul's SPAMMING Client. By continuing, you realize that JP is NOT responsible for any damage done. Trust Respect Responsibilty. All day. E're day."
name = raw_input("Name: ")
obj = s.SMTP("smtp.gmail.com:587")
obj.starttls()
obj.login(username, password)
print "Logged In! \n\r"
email = raw_input("Destination Email Address aka Where the Bacon will be Sent: ")
#message = raw_input("Email Message: ")
print "> Connecting to the SPAM client"
time.sleep(1)
print "> Sending SPAM into the void."
while True:
    obj.sendmail("username", email, "YOU'VE RECIEVED STUFF!\n\r---From your friend " + name)
    print "ya!"
print "Sent!"
