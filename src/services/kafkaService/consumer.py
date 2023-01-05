from json import dumps  
from kafka import KafkaConsumer 
import logging

TOPIC_NAME = 'wireshark-data'
SERVER_URL = 'localhost:9092'

def initializeConsumer():
    consumer = KafkaConsumer(  
        TOPIC_NAME,  
        bootstrap_servers = [SERVER_URL],   
        value_deserializer = lambda x : loads(x.decode('utf-8'))  
    )  
    return consumer

def getFromTopic():
    consumer = initializeConsumer()
    print("Initialized Kafka Consumer")
    logging.debug("Initialized Kafka Consumer")
    for message in consumer:
        print(message.value)
