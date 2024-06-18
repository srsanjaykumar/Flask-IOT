import pika

credentials = pika.PlainCredentials('pubuser1','pubuser1')
print(credentials)
parameters  = pika.ConnectionParameters('rabbitmq.selfmade.ninja',5672,'/',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='My_first_Queue')

channel.basic_publish(exchange='',routing_key="My_first_Queue",body='Hello World....')
print("[-X-] Send Hello World !... ")


connection.close()