## 📂 Project Structure

```
etl-pipeline-project/
│
├── data/
│   ├── employees.csv
│   ├── processed_employees.csv
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│
├── sql/
│   ├── create_tables.sql
│
└── README.md
```
## 🗄️ Database Integration
Data is loaded into SQLite database (`employees.db`) and queried using SQL.