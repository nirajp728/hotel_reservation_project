from src.data_ingestion import DataIngestion
from src.data_preprocessing import DataProcessor
from src.model_training import ModelTraining
from utils.common_functions import read_yaml
from config.paths_config import *

# python env cmd :  set GOOGLE_APPLICATION_CREDENTIALS=D:\mlops\scientific-air-428214-f7-0b2c8d8a5b52.json
# python env cmd : $env:PYTHONPATH="D:\mlops"

if __name__== "__main__":
    ### 1. Data ingestion
    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()

    ### 2. Data processing
    processor = DataProcessor(TRAIN_FILE_PATH, TEST_FILE_PATH, PROCESSED_DIR, CONFIG_PATH)
    processor.process()

    ### 3. Model Training
    trainer = ModelTraining(PROCESSED_TRAIN_DATA_PATH, PROCESSED_TEST_DATA_PATH, MODEL_OUTPUT_PATH)
    trainer.run()
