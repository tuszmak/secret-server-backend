from .getConn import getConn
from .queries import deleteQuery
def delete_secret_from_db(hash, envVariables):
    conn = getConn(envVariables)
    cur = conn.cursor()
    try:
              with conn.cursor() as cur:
                cur.execute(deleteQuery, (hash,)) # The execute wants a tuple as parameter, that's the weird parameters.              
                conn.commit()
    except Exception: 
              raise Exception("Delete query can't be executed")
    cur.close()