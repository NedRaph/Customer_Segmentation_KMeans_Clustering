from src.utils.logger import logger

class ClusterAssigner:
    def __init__(self, customer_df, X, model):
        self.customer_df=customer_df.copy()
        self.model=model
        self.X=X

    def assign_clusters(self):
        logger.info("Assigning clusters to customers")
        self.customer_df["Cluster"] = self.model.predict(self.X)
        logger.info(f"Cluster assignment completed. Customers clustered: {self.customer_df.shape[0]}")
        return self.customer_df