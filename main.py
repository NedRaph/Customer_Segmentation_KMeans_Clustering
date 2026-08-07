from src.data.loader import DataLoader
from src.data.validator import DataValidator
from src.data.cleaner import DataCleaner
from src.features.preprocessor import DataPreprocessor
from src.models.k_means_model import KMeansModel
from src.models.model_manager import ModelManager
from src.models.cluster_assigner import ClusterAssigner
from src.config.config import RAW_DATA_PATH
from src.utils.logger import logger





def main():
    # Load data
    loader=DataLoader(RAW_DATA_PATH)
    df=loader.load_data()
    # Validate data
    validator=DataValidator(df)
    validator.validate_columns()
    # Clean data
    cleaner=DataCleaner(df)
    customer_df=cleaner.wrangle()
    # Preprocess data
    preprocessor=DataPreprocessor(customer_df)
    X=preprocessor.preprocess()
    # Modelling
    modeler=KMeansModel(X)
    model=modeler.build_model()
    # Model manager
    model_manager=ModelManager()
    model_manager.save_model(model=model)
    # Assign clusters
    assigner=ClusterAssigner(customer_df=customer_df, X=X, model=model)
    clustered_df=assigner.assign_clusters()
    
    logger.info(f"Pipeline completed successfully. Customers clustered: {clustered_df.shape[0]}")

if __name__ == "__main__":
    main()    