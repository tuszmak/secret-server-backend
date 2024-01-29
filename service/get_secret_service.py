from db.get_secret import get_secret_from_db
from encrypt import decrypt_secret
from utils import to_secret_dao, to_secret_dto
from service.update_secret_service import update_secret

def get_secret_by_hash(hash: str, envVariables):
    secret = get_secret_from_db(hash, envVariables)
    secret_dao = to_secret_dao(secret)
    update_secret(secret_dao, envVariables)
    decrypted_secret = decrypt_secret(secret_dao.secret_text)
    return to_secret_dto(secret_dao, decrypted_secret.get("secret"))
