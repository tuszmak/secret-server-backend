from db.checkSecret import check_secret
from db.updateSecret import update_secret_in_db
from .deleteSecretService import delete_secret

def update_secret(secret, envVariables):
    try:
        if(check_secret(secret)):
            update_secret_in_db(secret, envVariables)
        else:
            delete_secret(secret, envVariables)
    except:
        raise Exception("Can't update the secret")

