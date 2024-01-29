from model import SecretDao, SecretDto
from dataclasses import asdict

def to_secret_dao(secret: tuple):
    return SecretDao(id=secret[0], 
                     hash=secret[1], 
                     secret_text=secret[2],
                     created_at=secret[3], 
                     expires_at=secret[4], 
                     remainingViews=secret[5])

def to_secret_dto(secret: SecretDao, decrypted_secret):
    return asdict(SecretDto(
                     hash=secret.hash, 
                     secret_text=decrypted_secret,
                     created_at=secret.created_at, 
                     expires_at=secret.expires_at, 
                     remainingViews=secret.remainingViews -1))
