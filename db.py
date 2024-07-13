import pyodbc as odbc
import os
from dotenv import load_dotenv

load_dotenv() 

DRIVER_NAME = os.environ.get('DRIVER_NAME', 'SQL SERVER')
DATABASE_SERVER_NAME = os.environ.get('DATABASE_SERVER_NAME')
DATABASE_NAME = os.environ.get('DATABASE_NAME')

def connect_db():
    connection_string = f"""
        DRIVER={{{DRIVER_NAME}}};
        SERVER={DATABASE_SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trust_Connection=yes;
    """

    connection = odbc.connect(connection_string)
    return connection