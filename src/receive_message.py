import pika

# URL from CloudAMQP
url = 'amqps://vplszsqx:7FyY9c_yM93Amb-q3PavdJBZQtYmSzO9@cow.rmq2.cloudamqp.com/vplszsqx'

# Connection parameters from the URL
params = pika.URLParameters(url)

# Connection to the AMQP server
connection = pika.BlockingConnection(params)

# Open a communication channel
channel = connection.channel()

# Declare the queue we want to consume from
channel.queue_declare(queue='hello')

# Define what happens when a message is received
def callback(ch, method, properties, body):
    print("Message received:", body.decode())

# Set up consumer to listen for messages from 'hello' queue
channel.basic_consume(
    queue='hello',
    on_message_callback=callback,
    auto_ack=True  # Automatically acknowledge receipt of message
)

print('Waiting for messages. To exit press CTRL+C')

# Start the message-consuming loop
channel.start_consuming()
