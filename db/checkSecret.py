from datetime import datetime
from model import SecretDao
def check_secret(secret: SecretDao):
    if(secret != None):
        return check_time(secret.expires_at) and check_visit_number(secret.remainingViews)
    else:
        raise Exception("No data given")

def check_time(time: datetime):
    return time > datetime.now()
def check_visit_number(number):
    return number > 0