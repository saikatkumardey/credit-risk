import pymssql
import os
import pandas as pd
from sqlsoup import SQLSoup

# server details
SERVER = os.environ.get("SERVER", "localhost")
USERNAME = os.environ.get("DB_USERNAME", "sa")
PASSWORD = os.environ.get("DB_PASSWORD", "reallyStrongPwd123")
DATABASE = os.environ.get("DB_NAME", "DW_AccessBI")
PORT = os.environ.get("DB_PORT", 1433)

# load data from SQL Server
# db_connection = pymssql.connect(
#     server=SERVER, user=USERNAME, password=PASSWORD, database=DATABASE, port=PORT)

conn_str = "mssql+pymssql://{user}:{password}@{server}/{database}?charset=utf8".format(
    user=USERNAME, password=PASSWORD, server=SERVER, database=DATABASE)
sqlsoup_obj = SQLSoup(conn_str)
engine = sqlsoup_obj.engine

def get_data_from_sqlserver(sql_string, connection_obj=engine):
    df = pd.read_sql(sql_string, connection_obj)
    return df

def get_categorical_values(column,table_name=None):
    
    if table_name is None:
        table_name = "D_"+column.upper()
    table = sqlsoup_obj.entity(table_name)
    rows = table.all()
    values = set()
    for row in rows:
        row_dict = row.__dict__
        column_value = row_dict.get(column,None)
        if column_value != None:
            values.add(column_value)
    
    values = [val for val in values if val!=None and len(val.strip())>0]
    values = sorted(values)
    values_tup = [(val,val) for val in values]
    return values_tup
