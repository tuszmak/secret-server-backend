from datetime import datetime
from dataclasses import dataclass

@dataclass
class SecretDto:
    hash: str
    secret_text: str
    created_at: datetime
    expires_at:datetime
    remainingViews:int