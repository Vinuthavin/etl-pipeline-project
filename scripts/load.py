from transform import transform

def load():
    df = transform()
    df.to_csv('../data/processed_employees.csv', index=False)
    print("Data loaded successfully")

if __name__ == "__main__":
    load()