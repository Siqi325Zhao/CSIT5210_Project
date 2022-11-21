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
