''' 
The class should:

receive the customer-level DataFrame in __init__,
store a copy of it,
have one public method—choose a clear name—that:
applies np.log1p() to:
TotalSpent
Orders
ItemsPurchased
AvgOrderValue
removes:
CustomerID
CountriesPurchased
returns the final five-column DataFrame.

Keep it as one method. We do not need to split this into tiny methods.
'''
import numpy as np

class DataPreprocessor:
    def __init__(self, customer_df):
        self.customer_df=customer_df.copy()

    def preprocess(self):
        self.customer_df[["TotalSpent", "Orders", "ItemsPurchased", "AvgOrderValue"]] = np.log1p( self.customer_df[["TotalSpent", "Orders", "ItemsPurchased", "AvgOrderValue"]] )
        X=self.customer_df.drop(columns=['CountriesPurchased', 'CustomerID'])
        return X