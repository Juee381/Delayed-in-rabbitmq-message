import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

message = "Hey (after delay)"

# Declared exchange
channel.exchange_declare("delay-x", exchange_type="x-delayed-message", arguments={"x-delayed-type": "direct"})

channel.basic_publish('delay-x', 'delayed_message', message,
                      properties=pika.BasicProperties(headers={"x-delay": 10000}))

print("message published...")

connection.close()
