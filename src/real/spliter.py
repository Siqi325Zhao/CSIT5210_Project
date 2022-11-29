# this is the data source file, waiting for other data source extensions!

from kafka import KafkaProducer
from pathlib import Path
import os
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

# use delicious data as an example
def producer():
    path = os.getcwd()
    print(path)

    # this could be changed to the path of the file you want to split
    f = open(path + "/src/real/data/delicious.txt", "r")

    dataset = f.readlines()

    # print(len(dataset))
    data_head = dataset[0]
    data_head = data_head.split(" ")[1:]
    # print(data_head)
    data_head.insert(0, 100)
    data_head_string = ""
    for i in data_head:
        if (i == len(data_head) - 1):
            data_head_string += str(i) + '\n'
            break
        data_head_string += str(i) + " "
    # print(data_head_string)
    dataset = dataset[1:]
    # print(len(dataset))

    data_sent = []
    for i in range(len(dataset)):
        bb = dataset[i].encode('utf-8')
        print(bb)
        producer.send('raymond', bb)
        if (i % 100 == 0):
            time.sleep(5)
        if i == 600:
            break

    producer.flush()

# here could be another data source
# every piece of data is consisted of a labels and features
# set the Num_Features Num_Labels in setting file default.yaml first


def producer_extension():
    pass


if __name__ == '__main__':
    print("processing...")

    producer()
