from .getConn import getConn
from .queries import updateQuery
from model import SecretDao

def update_secret_in_db(secret: SecretDao, envVariables): 
    conn = getConn(envVariables)
    cur = conn.cursor()
    try:
              cur.execute(updateQuery, (secret.remainingViews -1,secret.hash)) # paramList: new views, hash              
              conn.commit()
    except Exception: 
              raise Exception("Update query can't be executed")
    cur.close()
    