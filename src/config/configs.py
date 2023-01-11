import os
import sys
from dotenv import load_dotenv
import logging

load_dotenv()

credentials = {
    "kafkaServerURL" : 
        os.getenv("KAFKA_SERVER_URL"),
    "kafkaTopic" : 
        os.getenv("KAFKA_TOPIC"),
    "flaskServerHost" : 
        os.getenv("FLASK_SERVER_HOST"),
    "flaskServerPort" : 
        os.getenv("FLASK_SERVER_PORT")
}


def validateCredentials(credentials):

    flag = False

    for key, value in credentials.items():
        if value is None:
            flag = True
            logging.error('enviornment variable {} is not defined'.format(key))
    
    if flag:
        sys.exit("Exited")

validateCredentials(credentials)
