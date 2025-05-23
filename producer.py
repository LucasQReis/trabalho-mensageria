import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_exchange', exchange_type='direct')

pedido = {"id": 1, "cliente": "Lucas", "produto": "Notebook"}
mensagem = json.dumps(pedido)

routing_keys = ['billing', 'shipping']
for key in routing_keys:
    channel.basic_publish(exchange='direct_exchange',
                          routing_key=key,
                          body=mensagem)
    print(f" Message sent to '{key}'")

connection.close()
