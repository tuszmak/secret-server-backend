from model import SecretDao

def to_secret_dao(secret: tuple):
    return SecretDao(id=secret[0], hash=secret[1], secret_text=secret[2],created_at=secret[3], expires_at=secret[4], remainingViews=secret[5])
