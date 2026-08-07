from pathlib import Path


BASE_DIR=Path(__file__).parent.parent.parent

RAW_DATA_PATH=BASE_DIR/"data"/"raw"/"Online Retail.xlsx"
MODEL_PATH=BASE_DIR/"artifacts"/"model.pkl"
