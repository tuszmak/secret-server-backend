from db.deleteSecret import delete_secret_from_db

def delete_secret(hash: str, envVariables):
    try:
        delete_secret_from_db(hash, envVariables)
    except:
        raise