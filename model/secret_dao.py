from datetime import datetime
from dataclasses import dataclass


@dataclass
class SecretDao:
    id: int
    hash: str
    secret_text: str
    created_at: datetime
    expires_at:datetime
    remainingViews:int