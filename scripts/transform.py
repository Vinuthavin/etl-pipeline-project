from extract import extract
import logging

def transform():
    try:
        df = extract()
        
        logging.info("Starting transformation")

        # Add bonus column
        df['bonus'] = df['salary'] * 0.2

        # Filter IT department
        df = df[df['department'] == 'IT']

        logging.info("Transformation completed")
        return df

    except Exception as e:
        logging.error(f"Error in transform: {e}")
        raise