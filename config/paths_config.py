import os

############### Data Ingestion ###############

# After the extraction we will store the data in artifacts/raw/

RAW_DIR = "artifacts/raw"

# now we set the file in which the data will be coming
RAW_FILE_PATH = os.path.join(RAW_DIR, "raw.csv")

TRAIN_FILE_PATH = os.path.join(RAW_DIR, "train.csv")
TEST_FILE_PATH = os.path.join(RAW_DIR, "test.csv")

CONFIG_PATH = "config/config.yaml"



######################### DATA PROCESSING #########################

PROCESSED_DIR = "artifacts/processed"
PROCESSED_TRAIN_DATA_PATH = os.path.join(PROCESSED_DIR, "processed_train.csv")
PROCESSED_TEST_DATA_PATH = os.path.join(PROCESSED_DIR, "processed_test.csv")

######################### DATA PROCESSING #########################

MODEL_OUTPUT_PATH = "artifacts/models/lgbm_model.pki"