"""Secret deletion methods"""

from .get_conn import get_conn
from .queries import DELETE_QUERY
def delete_secret_from_db(hash, envVariables):
    """Execute delete query"""
    conn = get_conn(envVariables)
    cur = conn.cursor()
    try:
        with conn.cursor() as cur:
            cur.execute(DELETE_QUERY, (hash,)) # The execute wants a tuple as parameter, that's the weird parameters.              
            conn.commit()
    except Exception: 
        raise Exception("Delete query can't be executed")
    cur.close()
