import os
import pandas as pd
import numpy as np
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml, load_data
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE

logger = get_logger(__name__)

class DataProcessor:
    def __init__(self, train_path, test_path, processed_dir, config_path):
        self.train_path = train_path
        self.test_path = test_path
        self.processed_dir = processed_dir

        self.config = read_yaml(config_path)

        if not os.path.exists(self.processed_dir):
            os.makedirs(self.processed_dir)

    def preprocess_data(self, df):
        try:
            logger.info("Starting our dataprocessing step")

            logger.info("Dropping the columns")

            # Drop unrequired columns
            df.drop(columns= ['Unnamed: 0', 'Booking_ID'], inplace=True)

            # Drop duplicates
            df.drop_duplicates(inplace=True)

            # Defining cat_cols and num_cols
            cat_cols = self.config["data_processing"]["categorical_columns"]
            num_cols = self.config["data_processing"]["numerical_columns"]
            
            # Applying label encoding
            logger.info("Applying Label encoding")
       
            label_encoder = LabelEncoder()
            mappings={}

            for col in cat_cols:
              df[col] = label_encoder.fit_transform(df[col])
              mappings[col] = {label:code for label, code in zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_))}
            
            # Applying label mappings
            logger.info("Label mappings are :")

            for col, mapping in mappings.items():
                logger.info(f"{col} : {mapping}")
            
            # Checking multicollinearity but our data dosent have any multicollinearity as we found out in JupyterNotebook so we skip this part

            # Skewness handling
            logger.info("Doing skewness handling")

            skewness_threshold = self.config["data_processing"]["skewness_threshold"]

            # Applying lambda 
            skewness = df[num_cols].apply(lambda x:x.skew())
            # Applying log transformation
            for column in skewness[skewness>skewness_threshold].index:
                df[column] = np.log1p(df[column])

            # Return dataframe
            return df
       
        except Exception as e:
            logger.error(f"Error during preprocess step: {e}")
            raise CustomException("Error while preprocess data", e)
    
    def balance_data(self, df):
        try:
            logger.info("Handling Inmbalanced data")

            # Dropping booking_status column
            X = df.drop(columns = 'booking_status')
            y = df["booking_status"]
            
            # Using SMOTE
            smote = SMOTE(random_state=42)

            X_resampled, y_resampled = smote.fit_resample(X, y)

            balanced_df = pd.DataFrame(X_resampled, columns= X.columns)
            balanced_df["booking_status"] = y_resampled

            logger.info("Data balanced sucesfully")
            
            return balanced_df

        except Exception as e:
            logger.error(f"Error during balancing data step: {e}")
            raise CustomException("Error while balancing data", e)
        
    # Feature selection
    def select_features(self, df):
        try:
           logger.info("Starting our feature selection step")

           # Dropping booking_status column
           X = df.drop(columns = 'booking_status')
           y = df["booking_status"]

           model = RandomForestClassifier(random_state=42)
           model.fit(X, y)

           feature_importance = model.feature_importances_

           feature_importance_df = pd.DataFrame({
             'feature': X.columns,
             'importance': feature_importance
           })

           top_features_importance_df  = feature_importance_df.sort_values(by = "importance", ascending= False)

           num_features_to_select = self.config["data_processing"]["no_of_features"]

           # Top 10 features, we dont need all in order to predict target feature
           top_10_features = top_features_importance_df["feature"].head(num_features_to_select).values

           logger.info(f"Features selected : {top_10_features}")
           top_10_df = df[top_10_features.tolist() + ["booking_status"]]

           logger.info("Feature selection completed sucessfully")
           
           return top_10_df

        except Exception as e:
            logger.error(f"Error during feature selection step: {e}")
            raise CustomException("Error while feature selection", e)
        


    #We want this data in csv format, we right now have the data in dataframe format
    def save_data(self, df, file_path):
        try:
            logger.info("Saving our data in processed folder")

            df.to_csv(file_path, index=False)

            logger.info(f"Data saved sucesfully to {file_path}")

        except Exception as e:
            logger.error(f"Error during saving data step: {e}")
            raise CustomException("Error while saving data", e)
        
    def process(self):
        try:
            logger.info("Loading the data from RAW directory")

            train_df = load_data(self.train_path)
            test_df = load_data(self.test_path)

            train_df = self.preprocess_data(train_df)
            test_df = self.preprocess_data(test_df)

            train_df = self.balance_data(train_df)
            test_df = self.balance_data(test_df)

            train_df = self.select_features(train_df)
            # Don't be in a hurry and dont apply apply test_df = self.select_features(test_df) because top 10 features can be different for both train_df and test_df
            test_df = test_df[train_df.columns]

            self.save_data(train_df, PROCESSED_TRAIN_DATA_PATH)
            self.save_data(test_df, PROCESSED_TEST_DATA_PATH)

            logger.info("Data processing completed sucessfuly")

        except Exception as e:
            logger.error(f"Error during preprocessing pipeline:  {e}")
            raise CustomException("Error while preprocessing pipeline", e)


if __name__== "__main__":

    ### 2. Data processing
    processor = DataProcessor(TRAIN_FILE_PATH, TEST_FILE_PATH, PROCESSED_DIR, CONFIG_PATH)
    processor.process()

   # Use the -m flag from the project root:  D:\mlops>python -m src.data_preprocessing
# This tells Python to treat src as a package