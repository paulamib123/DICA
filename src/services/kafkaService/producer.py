from json import dumps
from kafka import KafkaProducer
import logging 
from time import sleep

from src.config.configs import credentials

def initializeProducer():
    producer = KafkaProducer(  
        bootstrap_servers = [credentials["kafkaServerURL"]],  
        value_serializer = lambda x : dumps(x).encode('utf-8')
    )  
    return producer

def sendToTopic(data):
    try:
        producer = initializeProducer()
        logging.debug("Initialized Kafka Producer")

        count = 0

        for record in data:
            producer.send(credentials["kafkaTopic"], value = record)
            count += 1
            logging.info(f'Sent record with {count} to topic {credentials["kafkaTopic"]}')

    except BufferError as error:
        logging.exception(error)
        print(f'Error producing message: {error}')
    except Exception as error:
        logging.exception(error)
        print(f'Error producing message: {error}')
