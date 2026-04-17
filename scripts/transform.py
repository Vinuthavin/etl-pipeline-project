from extract import extract

def transform():
    df = extract()
    
    # Example transformation
    df['salary'] = df['salary'] * 1.1
    
    return df

if __name__ == "__main__":
    print(transform().head())