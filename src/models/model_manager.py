import joblib
from src.config.config import MODEL_PATH
from src.utils.logger import logger


class ModelManager:
    def __init__(self, path=MODEL_PATH):
        self.path=path

    def save_model(self, model):
        joblib.dump(model, self.path)
        logger.info(f'Model successfully saved at location: {self.path}')

    def load_model(self):
        model=joblib.load(self.path)
        return model
