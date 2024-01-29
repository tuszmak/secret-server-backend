"""Secret getting methods"""

from db.queries import GET_QUERY
from .get_conn import get_conn

def get_secret_from_db(hash : str, env_variables):
    """Execute select query"""
    conn = get_conn(env_variables)
    cur = conn.cursor()
    secret = []
    try:
        with conn.cursor() as cur:
            cur.execute(GET_QUERY, (hash,)) # The execute wants a tuple as parameter, that's the weird parameters.
            secret = cur.fetchall()            
    except Exception:
        raise Exception("Select query can't be executed")
    cur.close()
    
    if(len(secret) == 0):
        return None
    if(len(secret) > 1):
        raise Exception("There are multiple secrets with the same hash.")
    return secret[0]
              