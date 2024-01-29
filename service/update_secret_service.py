from db.check_secret import check_secret
from model import SecretDao
from db.update_secret import update_secret_in_db
from .delete_secret_service import delete_secret

def update_secret(secret: SecretDao, env_variables):
    try:
        if(check_secret(secret)):
            update_secret_in_db(secret, env_variables)
        else:
            delete_secret(secret.hash, env_variables)
    except:
        raise Exception("Can't update the secret")
