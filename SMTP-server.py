import requests
import time
import smtplib
import pika
import json

server = smtplib.SMTP("smtp.gmail.com", 587)  # creates a connection to use smpt protocol
server.ehlo()  # initiate smpt conversation with server
server.starttls()  # starts transport layer security

server.login("carcatcherservice@gmail.com", "cecpxllseewstbeu")  # email and app password



def sendmail(server, arr):
    subject = "Price fell down"
    body = "You should buy this now: https://www.amazon.co.uk/Lacoste-2010871-Mens-Watch/dp/B01KNHQ4V8/ref=sr_1_5?keywords=mens+watch&qid=1568583110&sr=8-5"
    msg = f"Subject: {subject}\n\n{body}"  # formatting message
    server.sendmail(
        "carcatcherservice@gmail.com",  # sender
        "adamholland12398@gmail.com",  # receiver
        msg  # message
    )
    print(msg)


def main():
    server = smtplib.SMTP("smtp.gmail.com", 587)  # creates a connection to use smpt protocol
    server.ehlo()  # initiate smpt conversation with server
    server.starttls()  # starts transport layer security

    server.login("carcatcherservice@gmail.com", "cecpxllseewstbeu")  # email and app password


    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='smtpTESTING')

    def callback(ch, method, properties, body):
       # print(" [x] baka >~< Received", json.loads(body))
        array = eval(json.loads(body)["detections"])
        #print("\n\n\n", np.asarray(array[0]), np.asarray(array[0]).shape)
        sendmail(server, array)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue='baka', on_message_callback=callback)

    channel.basic_qos(prefetch_count=1)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

#server.quit()



