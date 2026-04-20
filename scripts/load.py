import logging
from transform import transform

# Configure logging
logging.basicConfig(
    filename='../data/etl.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

import logging
import sqlite3
from transform import transform

logging.basicConfig(
    filename='../data/etl.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load():
    try:
        logging.info("ETL process started")
        
        df = transform()
        
        # Connect to SQLite DB
        conn = sqlite3.connect('../data/employees.db')
        
        # Load data into table
        df.to_sql('employees', conn, if_exists='replace', index=False)
        
        conn.close()
        
        logging.info("Data loaded into database successfully")
        print("Data loaded into database successfully")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        print("Error occurred:", e)

if __name__ == "__main__":
    load()