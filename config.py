import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_exchange', exchange_type='direct')

filas = ['billing_queue', 'shipping_queue']
routing_keys = ['billing', 'shipping']

for fila, key in zip(filas, routing_keys):
    channel.queue_declare(queue=fila)
    channel.queue_bind(exchange='direct_exchange',
                       queue=fila,
                       routing_key=key)

connection.close()
