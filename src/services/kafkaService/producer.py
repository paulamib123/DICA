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
    try:
        producer = initializeProducer()
        logging.debug("Initialized Kafka Producer")

        for record in data:
            producer.send(TOPIC_NAME, value = record)

        logging.info(f'Sent data to topic {TOPIC_NAME}')
        sleep(5)
    except BufferError as error:
        logging.exception(error)
        print(f'Error producing message: {error}')
    except KafkaError as error:
        logging.exception(error)
        print(f'Error producing message: {error}')
    except Exception as error:
        logging.exception(error)
        print(f'Error producing message: {error}')
