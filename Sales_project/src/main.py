import os
import pandas as pd
from data_cleaner import DataCleaner
from database_manager import DatabaseManager
from data_logger import setup_logger
from analyzer import SalesAnalyzer

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

data_path = os.path.join(BASE_DIR, "Data", "sales_data.csv")
db_folder = os.path.join(BASE_DIR, "database")
db_path = os.path.join(db_folder, "sales.db")

log_folder = os.path.join(BASE_DIR, "logs")
log_path = os.path.join(log_folder, "app.log")

# Create folders if not exist
os.makedirs(db_folder, exist_ok=True)
os.makedirs(log_folder, exist_ok=True)

# Setup logger
logger = setup_logger(log_path)

try:
    logger.info("Application started")

    df = pd.read_csv(data_path)
    logger.info("CSV loaded successfully")

    cleaner = DataCleaner(df)
    cleaned_df = cleaner.clean_data()
    logger.info("Data cleaned successfully")

    db_manager = DatabaseManager(db_path)
    db_manager.create_table()
    db_manager.insert_data(cleaned_df)
    logger.info("Data inserted into database")

    rows = db_manager.fetch_all()
    logger.info("Data fetched from database")

    print("Process completed successfully!")


    # ANalyer start
    analyzer = SalesAnalyzer(db_path)
    
    print('\n TOTAL SALES:')
    print(analyzer.total_sales())

    print('\n SALES BY REGION:')
    print(analyzer.sales_by_region())

    print('\n BEST SELLING PRODUCT:')
    print(analyzer.best_selling_product())
    print('\n MONTHLY SALES:')
    print(analyzer.monthly_sales())

except FileNotFoundError:
    logger.error("CSV file not found.")
    print("CSV file not found.")
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    print(f"An error occurred: {e}")