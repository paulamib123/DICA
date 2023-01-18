import os
import logging
from datetime import datetime
from pytz import timezone, utc

def customTime(*args):
        utc_dt = utc.localize(datetime.utcnow())
        my_tz = timezone("Asia/Calcutta")
        converted = utc_dt.astimezone(my_tz)
        return converted.timetuple()

logging.Formatter.converter = customTime

SRC_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
ROOT_DIR = os.path.realpath(os.path.join(SRC_DIR, '..'))
LOG_FILE_PATH = "/logs/api.log"

LOG_FILE_NAME = ROOT_DIR + LOG_FILE_PATH

def loggerConfig():
        logging.basicConfig(
                    #filename=LOG_FILE_NAME, 
                    #filemode='w',
                    level=logging.INFO, 
                    format="%(asctime)s:%(levelname)s: %(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S')
                    
        logging.debug("Logger Configured and Started")