import logging
from transform import transform

# Configure logging
logging.basicConfig(
    filename='../data/etl.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load():
    try:
        logging.info("ETL process started")
        
        df = transform()
        
        df.to_csv('../data/processed_employees.csv', index=False)
        
        logging.info("Data loaded successfully")
        print("Data loaded successfully")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        print("Error occurred:", e)

if __name__ == "__main__":
    load()