import os
import sys
from src.logger import logging
from src.exception import CustomException

from sklearn.model_selection import train_test_split
import pandas as pd

from dataclasses import dataclass

## Initialize the Data Ingestion Configuration
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts', 'train.csv')
    test_data_path: str=os.path.join('artifacts', 'test.csv')
    raw_data_path: str=os.path.join('artifacts', 'raw.csv')

## Create the data ingestion CLass
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Method Start")

        try:
            pass

        except Exception as e:
            logging.info('Exception Occured in DataIngestion Stage')
            raise CustomException(e, sys)