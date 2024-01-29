from datetime import datetime
from model import SecretData
from db import create_secret

def create_secret_dao(data : dict, env_variables):
    parsed_date = datetime.fromisoformat(str(data.get("expiryDate")))
    new_secret_data = SecretData(data.get("secret"),data.get("numberOfVisits"), parsed_date)
    if check_secret_values(new_secret_data):
        return create_secret(new_secret_data, env_variables)
    raise Exception("Some data is not provided.")
    
def check_secret_values(data: SecretData):
    return data.text != "" and data.numberOfVisits != 0 and data.expDate!=None
