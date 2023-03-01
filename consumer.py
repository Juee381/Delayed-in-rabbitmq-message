import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


def callback(ch, method, property, body):
    print(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.queue_declare(queue='delay_q', durable=True)

# Bind the queue with exchange and route key
channel.queue_bind(queue="delay_q", exchange="delay-x", routing_key="delayed_message")

# Consuming From queue
channel.basic_consume(queue='delay_q', auto_ack=False, on_message_callback=callback)

print("Consumer Waiting")
channel.start_consuming()
connection.close()
