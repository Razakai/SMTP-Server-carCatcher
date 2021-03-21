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
    '''msg = f"Subject: {subject}\n\nThe following licence plates were spotted:\n{licencePlates}\nat this location: {location}\n\nRegards,\nCar Catcher Team"  # formatting message
    for email in ["adamholland12398@gmail.com"]:
        server.sendmail(
            "carcatcherservice@gmail.com",  # sender
            email,  # receiver
            msg  # message
        )
    print(msg)'''



'''async def processMessage(subject, licencePlates, location):
    emails = await getEmails()

    server = smtplib.SMTP("smtp.gmail.com", 587)  # creates a connection to use smpt protocol
    server.ehlo()  # initiate smpt conversation with server
    server.starttls()  # starts transport layer security

    server.login("carcatcherservice@gmail.com", "cecpxllseewstbeu")  # email and app password

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='smtpTESTING')

    def callback(ch, method, properties, body):
       # print(" [x] baka >~< Received", json.loads(body))
        message = json.loads(body)
        subject = message["subject"]
        licencePlates = message["licencePlates"]
        location = message["location"]

        sendmail(server, subject, licencePlates, location)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue='smtpTESTING', on_message_callback=callback)

    channel.basic_qos(prefetch_count=1)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()'''




