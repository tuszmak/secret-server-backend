import psycopg2
import os
# This function only exists to reduce code duplication.

def getConn(envVariables : dict):
    conn = psycopg2.connect(
              host=envVariables.get('DB_HOST'),
              database=envVariables.get('DB_NAME'),
              user=envVariables.get('DB_USERNAME'),
              password=envVariables.get('DB_PASSWORD')
              )
    return conn