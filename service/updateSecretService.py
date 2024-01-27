from db.checkSecret import check_secret
from db.updateSecret import update_secret_in_db
from .deleteSecretService import delete_secret
from model import SecretDao

def update_secret(secret: SecretDao, envVariables):
    try:
        if(check_secret(secret)):
            update_secret_in_db(secret, envVariables)
        else:
            delete_secret(secret.hash, envVariables)
    except:
        raise
        raise Exception("Can't update the secret")

