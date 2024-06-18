import pika

credentials = pika.PlainCredentials('pubuser1','pubuser1')
print(credentials)
parameters  = pika.ConnectionParameters('rabbitmq.selfmade.ninja',5672,'/',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='My_first_Queue')

def callback(ch , method , properties , body):
    print('[X] Received %r'%body)

channel.basic_consume(queue='My_first_Queue',auto_ack=True, on_message_callback=callable)
