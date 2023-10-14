import psycopg
from psycopg import sql
from project2_2019147547 import *
HOST = 'localhost'
DBNAME = 'mydbase'
USER = 'postgres'
PASSWORD = 'Redvelvet123!'
CONNECTION = f"host={HOST} dbname={DBNAME} user={USER} password={PASSWORD}"
path =  'C:/Users/USER/Desktop/DBe/create_table.sql'

execute_sql(CONNECTION, path)
path =  'C:/Users/USER/Desktop/DBe/insert_data.sql'

execute_sql(CONNECTION, path)

table_name = 'building'
entire_search(CONNECTION=CONNECTION, table_name=table_name)