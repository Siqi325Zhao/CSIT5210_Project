from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

print("processing...")

for i in range(12):
    producer.send('raymond', b"lishangyu_%d" % i)

producer.flush()
print("success")
# sleep(5)