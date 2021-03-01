import requests
import time
import smtplib


def sendmail():
    server = smtplib.SMTP("smtp.gmail.com", 587)  # creates a connection to use smpt protocol
    server.ehlo()  # initiate smpt conversation with server
    server.starttls()  # starts transport layer security

    server.login("carcatcherservice@gmail.com", "cecpxllseewstbeu")  # email and app password
    subject = "Price fell down"
    body = "You should buy this now: https://www.amazon.co.uk/Lacoste-2010871-Mens-Watch/dp/B01KNHQ4V8/ref=sr_1_5?keywords=mens+watch&qid=1568583110&sr=8-5"
    msg = f"Subject: {subject}\n\n{body}"  # formatting message
    server.sendmail(
        "carcatcherservice@gmail.com",  # sender
        "adamholland12398@gmail.com",  # receiver
        msg  # message
    )
    print(msg)
    server.quit()


sendmail()



