from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.cluster import KMeans 
from src.utils.logger import logger



class KMeansModel:
    def __init__(self, X):
        self.X=X

    def build_model(self):
        logger.info(f"Starting KMeans model training. Training data shape {self.X.shape}")
        model=make_pipeline(
            StandardScaler(),
            KMeans(n_clusters=5, random_state=42)
        )
        model.fit(self.X)
        logger.info("KMeans model training completed")
        return model


