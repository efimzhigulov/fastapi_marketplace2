import pika
import sys
def rabbit(sev,args):
    """Вызывается в функции add_order в main.py. При вызове отправляет
     сообщение в одну из трех очередей - new_order, order_processing,
     notification. Модуль recieve_logs_direct.py принимает данные из
     очередей и выполняет действия, такие как подтверждение заказа,
     обновление статуса и отправка уведомлений клиентам. Обработчик
     запускается командой:
     python consumer.py new_order order_processing notification > logs_from_rabbit.log"""
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

    severity = sev
    message = args
    channel.basic_publish(
        exchange='direct_logs', routing_key=severity, body=message)
    if sev == 'new_order':
        print(f" [x] Sent {severity}: Order with id {message} created")
    if sev == 'order_processing':
        print(f" [x] Sent {severity}: The order's status: {message}")
    if sev == 'notification':
        print(f" [x] Sent {severity} to the client, new order registered at {message}")

    connection.close()




