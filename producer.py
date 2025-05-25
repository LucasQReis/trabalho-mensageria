import pika
import json
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_exchange', exchange_type='direct')

routing_keys = ['billing', 'shipping']

pedido_id = 1

try:
    while True:
        for routing_key in routing_keys:
            pedido = {
                "id": pedido_id,
                "cliente": f"Cliente {pedido_id}",
                "produto": "Notebook"
            }
            mensagem = json.dumps(pedido)
            channel.basic_publish(
                exchange='direct_exchange',
                routing_key=routing_key,
                body=mensagem
            )
            print(f"[Produtor] Enviada para {routing_key}: Pedido #{pedido_id}")

        pedido_id += 1
        time.sleep(10) 

except KeyboardInterrupt:
    print("\n[Produtor] Interrompido pelo usuário.")
    connection.close()
