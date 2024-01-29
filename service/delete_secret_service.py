from db.delete_secret import delete_secret_from_db

def delete_secret(hash: str, envVariables):
    delete_secret_from_db(hash, envVariables)