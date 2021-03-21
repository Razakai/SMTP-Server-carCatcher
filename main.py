import json
import rabbitpy
from database.connection import connectDB, disconnectDB
from SMTP_server import sendmail, startServer, stopServer
import asyncio


async def connection():
    with rabbitpy.Connection('amqp://guest:guest@localhost:5672/%2f') as conn:
        with conn.channel() as channel:
            rabbitpy.create_queue(queue_name='smtpTESTING')
            queue = rabbitpy.Queue(channel, 'smtpTESTING')

            # Exit on CTRL-C
            try:
                # Consume the message
                for message in queue:
                    message = json.loads(body)
                    subject = message["subject"]
                    licencePlates = message["licencePlates"]
                    location = message["location"]
                    
                    await sendmail(subject, licencePlates, location)

                    message.ack()

            except KeyboardInterrupt:
                print('Exited consumer')

async def main():
    startServer()
    await connectDB()
    await connection()


if __name__ == "__main__":
    asyncio.run(main())
