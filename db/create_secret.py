"""Secret creation methods"""

from datetime import datetime
from db.queries import INSERT_QUERY
from model import SecretData
from encrypt import generate_link, encrypt_secret
from .get_conn import get_conn

def create_secret(data: SecretData, env_variables):
    """Execute insert query"""
    conn = get_conn(env_variables)
    # Open a cursor to perform database operations
    cur = conn.cursor()
    link = generate_link()
    with conn.cursor() as cur:

        cur.execute(INSERT_QUERY, (link, encrypt_secret(data.text), datetime.now(), data.expDate, data.numberOfVisits))
        conn.commit()
    return link
        