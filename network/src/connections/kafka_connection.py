# src/networking/gateway/connections/kafka_connection.py

# Kafka Producer Example
from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost:9092'})
p.produce('error-logs', key='error', value='error message')
p.flush()

# Kafka Consumer Example
from confluent_kafka import Consumer, KafkaException

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['error-logs'])

try:
    while True:
        msg = c.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())
        else:
            # Correct message
            print(f"Received message: {msg.value().decode('utf-8')}")
except KeyboardInterrupt:
    pass
finally:
    c.close()
