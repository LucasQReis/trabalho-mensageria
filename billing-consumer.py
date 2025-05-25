import pika
import json
import time

def callback(ch, method, properties, body):
    pedido = json.loads(body)
    print(f"[Billing] Processando pedido: {pedido}")
    time.sleep(30) 

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='billing_queue')

channel.queue_bind(
    exchange='direct_exchange',
    queue='billing_queue',
    routing_key='billing'
)

channel.basic_consume(
    queue='billing_queue',
    on_message_callback=callback,
    auto_ack=True
)

print('[Billing] Aguardando mensagens...')
channel.start_consuming()
