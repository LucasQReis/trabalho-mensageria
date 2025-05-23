import pika
import json

def callback(ch, method, properties, body):
    pedido = json.loads(body)
    print(f"Processing billing note: {pedido}")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='billing_queue')

channel.basic_consume(queue='billing_queue',
                      on_message_callback=callback,
                      auto_ack=True)

print('Waiting message...')
channel.start_consuming()
