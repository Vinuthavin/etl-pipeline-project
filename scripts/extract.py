import pandas as pd

def extract():
    df = pd.read_csv('../data/employees.csv')
    return df

if __name__ == "__main__":
    print(extract())