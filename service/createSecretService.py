from model import SecretData
from db import createSecret
from datetime import datetime

def create_secret_dao(data : dict, env_variables):
    parsed_date = datetime.fromisoformat(str(data.get("expiryDate")))
    new_secret_data = SecretData(data.get("secret"),data.get("numberOfVisits"), parsed_date)
    if(check_secret_values(new_secret_data)):
        return createSecret(new_secret_data, env_variables)
    else: 
        raise Exception("Some data is not provided.")
    
def check_secret_values(data: SecretData):
    return data.text != "" and data.numberOfVisits != 0 and data.expDate!=None
