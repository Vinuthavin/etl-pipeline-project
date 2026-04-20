import sqlite3
import pandas as pd

conn = sqlite3.connect('../data/employees.db')

query = "SELECT * FROM employees"

df = pd.read_sql(query, conn)

print(df)

conn.close()