from kafka import KafkaConsumer

# consumer = KafkaConsumer("topic")
consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
consumer = KafkaConsumer("raymond")

print("consumer")

for consumer_record in consumer:
    print(type(consumer_record))
    print(consumer_record)

# next(consumer)
print("success2")

# msgpack.loads

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

print("processing...")

for i in range(12):
    producer.send('raymond', b"lishangyu_%d" % i)

producer.flush()
print("success")
# sleep(5)
