import pymssql
import os
import pandas as pd

# server details
SERVER = os.environ.get("SERVER", "localhost")
USERNAME = os.environ.get("DB_USERNAME", "sa")
PASSWORD = os.environ.get("DB_PASSWORD", "reallyStrongPwd123")
DATABASE = os.environ.get("DB_NAME", "DW_AccessBI")
PORT = os.environ.get("DB_PORT", 1433)

# load data from SQL Server
db_connection = pymssql.connect(server=SERVER,user=USERNAME,password=PASSWORD,database=DATABASE,port=1433)

def get_data_from_sqlserver(sql_string,connection_obj=db_connection):
    df = pd.read_sql(sql_string,connection_obj)
    return df
