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

        counter = 1

        for record in data:
            producer.send(credentials["kafkaTopic"], value = record)
            logging.info(f'Sent record with id : {counter} to topic {credentials["kafkaTopic"]}')
            counter += 1

    except BufferError as error:
        logging.exception(error)
        print(f'Error producing message: {error}')
    except Exception as error:
        logging.exception(error)
        print(f'Error producing message: {error}')
