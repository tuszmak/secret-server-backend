import traceback
from datetime import datetime
from model import SecretData
from .getConn import getConn
from encrypt import generateLink, encryptSecret
from db.queries import insert_query

def createSecret(data: SecretData, envVariables):
        conn = getConn(envVariables)
        # Open a cursor to perform database operations
        cur = conn.cursor()
        link = generateLink()
        try:
                with conn.cursor() as cur:
                        cur.execute(insert_query, (link, encryptSecret(data.text), datetime.now(), data.expDate, data.numberOfVisits))
                        conn.commit() 
        except Exception:
                raise
        return link
        