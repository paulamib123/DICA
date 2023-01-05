from json import dumps  
from kafka import KafkaProducer
import logging 
from time import sleep

TOPIC_NAME = 'wireshark-data'
SERVER_URL = 'localhost:9092'

def initializeProducer():
    producer = KafkaProducer(  
        bootstrap_servers = [SERVER_URL],  
        value_serializer = lambda x : dumps(x).encode('utf-8')  
    )  
    return producer

def sendToTopic(data):
    producer = initializeProducer()
    #print("Initialized Kafka Producer")
    logging.debug("Initialized Kafka Producer")
    producer.send(TOPIC_NAME, value = data)
    #print("Sent data to topic {}".format(TOPIC_NAME))
    logging.info("Sent data to topic {}".format(TOPIC_NAME))
    sleep(5)
