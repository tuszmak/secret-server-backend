from datetime import datetime
from dataclasses import dataclass

@dataclass
class SecretData:
    text:str
    numberOfVisits:int
    expDate:datetime