from .get_conn import get_conn
from .queries import UPDATE_QUERY
from model import SecretDao

def update_secret_in_db(secret: SecretDao, env_variables): 
    conn = get_conn(env_variables)
    cur = conn.cursor()
    try:
        cur.execute(UPDATE_QUERY, (secret.remainingViews -1,secret.hash)) # paramList: new views, hash            
        conn.commit()
    except Exception: 
        raise Exception("Update query can't be executed")
    cur.close()
    