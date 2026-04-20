import pandas as pd
import logging

def extract():
    try:
        df = pd.read_csv('../data/employees.csv')
        logging.info("Data extracted successfully")
        return df
    except Exception as e:
        logging.error(f"Error in extract: {e}")
        raise