from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.cluster import KMeans 




class KMeansModel:
    def __init__(self, X):
        self.X=X

    def build_model(self):
        model=make_pipeline(
            StandardScaler(),
            KMeans(n_clusters=5, random_state=42)
        )
        model.fit(self.X)
        return model


