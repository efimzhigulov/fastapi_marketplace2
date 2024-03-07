import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

severities = ["new_order", "order_processing", "notification"]


for severity in severities:
    channel.queue_bind(
        exchange='direct_logs', queue=queue_name, routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    if method.routing_key == 'new_order':
        with open("new_order.txt", 'a') as file:
            create_text_1 = file.write(f"{method.routing_key}: Order with id {body} created\n")
            print(create_text_1)
    if method.routing_key == 'order_processing':
        with open("order_processing.txt", 'a') as file:
            create_text_2 = file.write(f"{method.routing_key}: The order's status: {body}\n")
            print(create_text_2)
    if method.routing_key == 'notification':
        with open("notification.txt", 'a') as file:
            create_text_3 = file.write(f"{method.routing_key}: new order registered at {body}\n")
            print(create_text_3)


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()