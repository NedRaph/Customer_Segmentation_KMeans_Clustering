import pandas as pd
import openpyxl
from src.utils.logger import logger


class DataLoader:
    def __init__(self, path):
        self.path=path

    def load_data(self):
        logger.info(f"Loading raw data from: {self.path}")
        df=pd.read_excel(self.path)
        logger.info(f"Raw data successfully loaded. Shape: {df.shape}")
        return df
        


