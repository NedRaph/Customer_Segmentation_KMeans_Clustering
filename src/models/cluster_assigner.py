class ClusterAssigner:
    def __init__(self, customer_df, X, model):
        self.customer_df=customer_df.copy()
        self.model=model
        self.X=X

    def assign_clusters(self):
        self.customer_df["Cluster"] = self.model.predict(self.X)
        return self.customer_df