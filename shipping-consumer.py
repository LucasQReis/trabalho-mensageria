import pika
import json
import time

def callback(ch, method, properties, body):
    pedido = json.loads(body)
    print(f"[Shipping] Processando pedido: {pedido}")
    time.sleep(30)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='shipping_queue')

channel.queue_bind(
    exchange='direct_exchange',
    queue='shipping_queue',
    routing_key='shipping'
)

channel.basic_consume(
    queue='shipping_queue',
    on_message_callback=callback,
    auto_ack=True
)

print('[Shipping] Aguardando mensagens...')
channel.start_consuming()
