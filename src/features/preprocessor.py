import numpy as np
from src.utils.logger import logger

class DataPreprocessor:
    def __init__(self, customer_df):
        self.customer_df=customer_df.copy()

   
    def preprocess(self):
        logger.info("Starting feature preprocessing")
        self.customer_df[["TotalSpent", "Orders", "ItemsPurchased", "AvgOrderValue"]] = np.log1p( self.customer_df[["TotalSpent", "Orders", "ItemsPurchased", "AvgOrderValue"]] )
        X=self.customer_df.drop(columns=['CountriesPurchased', 'CustomerID'])

        logger.info(f"Feature preprocessing completed. Input shape: {self.customer_df.shape}, Output shape: {X.shape}")
        return X