import logging
import os   # we need os for creating a place for storing our logs
from datetime import datetime  # we want date & time of each log

LOGS_DIR="logs"

os.makedirs(LOGS_DIR, exist_ok=True)  #If the logs directory exists then dont create logs dir, but if it dosent exists then create

LOGS_FILE=os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log") #we store the LOGS DIRECTORY in a file and that file name is log_{"current date and time"}
# The strftime specifies the format, first year then month and then date
# File will look like in logs folder --> log_2025-02-21.log

logging.basicConfig(
    filename=LOGS_FILE,
    format='%(asctime)s - %(levelname)s - %(message)s', #asctime is at what time it was created with time, month, date and year,
    #Their are various levels for logging, 1)info, 2) warning, 3) error
    #time - INFO - message
    level=logging.INFO 
)

def get_logger(name):
    logger = logging.getLogger(name)  #It will create logger on the basis of the user passed name in the function
    logger.setLevel(logging.INFO)
    return logger







