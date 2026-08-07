# Import libraries
import pandas as pd
from src.utils.logger import logger


class DataCleaner:
    def __init__(self, df):
        self.df=df.copy()
    
    def wrangle(self):
        """
        Cleans and transforms the raw Online Retail dataset into a 
        customer-level dataset suitable for K-Means clustering

        Parameters
        ----------
        df : pandas.DataFrame
            Raw transactional data

        Returns
        -------
        df : pandas.DataFrame
            Customer-level dataframe with engineered features

        """ 
        logger.info("Starting data cleaning and feature engineering")
        # Remove duplicates
        self.df.drop_duplicates(inplace=True)

        # Remove rows with missing values
        self.df.dropna(inplace=True)

        # Separate purchases and cancelletaions
        purchases=self.df[self.df["Quantity"]>0].copy()
        cancellations=self.df[self.df["Quantity"]<0].copy()

        # Create absolute quantity for matching
        purchases["AbsQuantity"] = purchases["Quantity"]
        cancellations["AbsQuantity"] = cancellations["Quantity"].abs()

        # Match purchases with cancellations
        matched = purchases.merge(
        cancellations,
        on=["CustomerID", "StockCode", "UnitPrice", "AbsQuantity"],
        suffixes=("_purchase", "_cancel")
        )

        # Get all invoice numbers involved in complete cancellations
        invoices_to_remove = (
            set(matched["InvoiceNo_purchase"])
            .union(set(matched["InvoiceNo_cancel"]))
        )

        # Remove matched purchase/cancellation pairs
        self.df = self.df[~self.df["InvoiceNo"].isin(invoices_to_remove)]

        # Remove any remaining negative quantities or invalid prices
        self.df = self.df[(self.df["Quantity"] > 0) & (self.df["UnitPrice"] > 0)]

        # Create TotalPrice feature
        self.df["TotalPrice"] = self.df["Quantity"] * self.df["UnitPrice"]

        # Reference date for Recency calculation
        reference_date = self.df["InvoiceDate"].max()

        # Aggregate transaction-level data to customer level
        customer_df = (
            self.df.groupby("CustomerID")
            .agg(
                TotalSpent=("TotalPrice", "sum"),
                Orders=("InvoiceNo", "nunique"),
                ItemsPurchased=("Quantity", "sum"),
                CountriesPurchased=("Country", "nunique"),
                LastPurchase=("InvoiceDate", "max")
            )
            .reset_index()
        )

        # Feature Engineering

        # Average spend per order
        customer_df["AvgOrderValue"] = (
            customer_df["TotalSpent"] / customer_df["Orders"]
        )

        # Days since last purchase
        customer_df["Recency"] = (
            reference_date - customer_df["LastPurchase"]
        ).dt.days

        # Drop helper column
        customer_df.drop(columns="LastPurchase", inplace=True)
        logger.info(f"Data cleaning completed. Customer df shape: {customer_df.shape}")

        return customer_df


