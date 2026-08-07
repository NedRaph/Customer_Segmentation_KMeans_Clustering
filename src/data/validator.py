import pandas as pd
from src.utils.logger import logger

class DataValidator:
    def __init__(self, df):
        self.df=df

    def validate_columns(self):
        expected_columns= {'InvoiceNo', 'StockCode','Description', 'Quantity','InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'}
        actual_columns=set(self.df.columns)

        logger.info("Validating raw data columns")
        if actual_columns == expected_columns:
            logger.info("Raw data validation successful")
        else:
            raise Exception (f'Columns do not match as expected. Check that the columns are; {expected_columns}')

