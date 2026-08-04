import pandas as pd
import openpyxl

class DataLoader:
    def __init__(self, path):
        self.path=path

    def load_data(self):
        return pd.read_excel(self.path)


