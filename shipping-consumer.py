import pika
import json

def callback(ch, method, properties, body):
    pedido = json.loads(body)
    print(f"Processing shipping: {pedido}")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='shipping_queue')

channel.basic_consume(queue='shipping_queue',
                      on_message_callback=callback,
                      auto_ack=True)

print('Waintig message...')
channel.start_consuming()
