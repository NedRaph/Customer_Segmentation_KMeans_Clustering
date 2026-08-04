import pandas as pd

class DataValidator:
    def __init__(self, df):
        self.df=df

    def validate_columns(self):
        expected_columns= {'InvoiceNo', 'StockCode','Description', 'Quantity','InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'}
        actual_columns=set(self.df.columns)
        if actual_columns == expected_columns:
            return 'columns match as expected'
        else:
            raise Exception (f'Columns do not match as expected. Check that the columns are; {expected_columns}')

