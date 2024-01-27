from db.get_secret import getSecretFromDb
from encrypt import decryptSecret
from utils import to_secret_dao
from .updateSecretService import update_secret
def get_secret_by_hash(hash: str, envVariables):
    try:
        secret = getSecretFromDb(hash, envVariables)
        secret_dao = to_secret_dao(secret)
        update_secret(secret_dao, envVariables)
        return decryptSecret(secret_dao.secret_text)
    except:
        raise
    