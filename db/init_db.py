import os
import sys

from .getConn import getConn
import psycopg2
def init(envVariables):
        
        conn = getConn(envVariables)
        
        # Open a cursor to perform database operations
        cur = conn.cursor()
        
        # Execute a command: this creates a new table
        try:
         
    # Execute the CREATE TABLE statement
         cur.execute('CREATE TABLE IF NOT EXISTS secrets (id serial PRIMARY KEY,'
                'hash varchar (150) NOT NULL,'
                'secret_text varchar (150) NOT NULL,'
                'created_at timestamp NOT NULL,'
                'expires_at timestamp NOT NULL,'
                'remaining_views integer NOT NULL);')
    # Commit the changes
         conn.commit()
         print("Table created successfully.")
        except Exception as e:
                print(f"Error: {e}")
        cur.close()
        