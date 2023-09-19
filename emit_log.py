import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="localhost",
        port=5672,
        credentials=pika.PlainCredentials(username="admin", password="guest"),
    )
)
channel = connection.channel()

channel.exchange_declare(exchange="logs", exchange_type="fanout")

message = ' '.join(sys.argv[1:]) or "info: empty!"
channel.basic_publish(exchange="", routing_key="teste", body=message)
print(f" [x] Sent {message}")
connection.close()
