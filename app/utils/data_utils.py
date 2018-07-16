import pandas as pd

def get_data_from_sqlserver(sql_string,connection_obj):
    df = pd.read_sql(sql_string,connection_obj)
    return df