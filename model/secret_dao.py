from datetime import datetime

class SecretDao:
    def __init__(self,id:int ,hash:str, secret_text: str, created_at: datetime,expires_at:datetime, remainingViews:int):
        self.id = id
        self.hash = hash
        self.secret_text = secret_text
        self.created_at = created_at
        self.expires_at = expires_at
        self.remainingViews = remainingViews

