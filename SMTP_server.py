import smtplib
from data.queries import getEmails


class Server():
    def __init__(self):
        self.server = None
    
    def startServer(self):
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.ehlo()
        self.server.starttls()
        self.server.login("carcatcherservice@gmail.com", "cecpxllseewstbeu")

    def stopServer(self):
        self.server.quit()
    
    def sendMail(self, msg, emails):
        for email in getEmails():
            self.server.sendmail(
                "carcatcherservice@gmail.com",
                email["email"],
                msg
            )

server = Server()


def startServer():
    server.startServer()


def stopServer():
    server.stopServer()


async def sendmail(subject, licencePlates, location):
    msg = f"Subject: {subject}\n\nThe following licence plates were spotted:\n{licencePlates}\nat this location: {location}\n\nRegards,\nCar Catcher Team"  # formatting message
    server.sendMail(msg)




