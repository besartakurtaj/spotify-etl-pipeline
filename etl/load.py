import pandas as pd
import json
from sqlalchemy import create_engine

def load_data(data: pd.DataFrame, table_name: str, config_path='config.json'):
    """Loads a DataFrame into a SQL Server table."""
    with open(config_path, 'r') as f:
        config = json.load(f)

    server = config['server']
    database = config['database']
  

    conn_str = f"mssql+pyodbc://@{server}/{database}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server"
    engine = create_engine(conn_str)

    data.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"Loaded {table_name}")
