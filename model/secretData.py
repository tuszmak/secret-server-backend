from datetime import datetime

class SecretData:
    def __init__(self,text:str,numberOfVisits:int, expDate:datetime):
        self.text = text
        self.numberOfVisits = numberOfVisits
        self.expDate = expDate
