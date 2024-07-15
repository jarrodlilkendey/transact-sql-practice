import pandas as pd
from db import connect_db, execute_query_fetchall, execute_query
from query import read_query_from_file

DATA_FILE_PATH = './data/Projected population, components of change and summary statistics, 2022 (base) to 2071.xlsx'
DATA_SHEET_NAME = 'Australia'

def load_data():
    df = pd.read_excel(DATA_FILE_PATH, sheet_name = DATA_SHEET_NAME)
    print(df)
    ingest_data()

def ingest_data():
    connection = connect_db()
    execute_query(connection, read_query_from_file('./sql/0-drop-population-table.sql'))
    execute_query(connection, read_query_from_file('./sql/1-create-population-table.sql'))
    population_data = [
        ('Australia', 'High', 2022),
        ('Australia', 'Medium', 2022),
        ('Australia', 'Low', 2022),
    ]
    population_data_string = str(population_data).strip('[]')
    execute_query(connection, read_query_from_file('./sql/2-insert-population-data.sql').format(population_data_string))
    # how to make use of the relationsal aspect. maybe have region info tables, use as a foreign key

if __name__ == "__main__":
    load_data()