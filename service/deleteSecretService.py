from db.deleteSecret import delete_secret_from_db

def delete_secret(secret, envVariables):
    try:
        delete_secret_from_db(secret, envVariables)
    except:
        raise