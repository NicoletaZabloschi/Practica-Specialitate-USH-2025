import pika

# URL from CloudAMQP
url = 'amqps://vplszsqx:7FyY9c_yM93Amb-q3PavdJBZQtYmSzO9@cow.rmq2.cloudamqp.com/vplszsqx'

params = pika.URLParameters(url)

connection = pika.BlockingConnection(params)
channel = connection.channel()

# queue
channel.queue_declare(queue='hello')

# message
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello!')

print("Message sent!")

connection.close()
