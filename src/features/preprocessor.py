import numpy as np

class DataPreprocessor:
    def __init__(self, customer_df):
        self.customer_df=customer_df.copy()

    def preprocess(self):
        self.customer_df[["TotalSpent", "Orders", "ItemsPurchased", "AvgOrderValue"]] = np.log1p( self.customer_df[["TotalSpent", "Orders", "ItemsPurchased", "AvgOrderValue"]] )
        X=self.customer_df.drop(columns=['CountriesPurchased', 'CustomerID'])
        return X