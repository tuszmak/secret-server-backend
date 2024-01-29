"""Secret validation checks"""

from datetime import datetime
from model import SecretDao
def check_secret(secret: SecretDao):
    """Check if secret is valid."""
    if(secret is not None):
        return check_time(secret.expires_at) and check_visit_number(secret.remainingViews)
    raise Exception("No data given")

def check_time(time: datetime):
    """Check if the expiry time is valid"""
    return time > datetime.now()
def check_visit_number(number):
    """Check if you can still visit the secret"""
    return number > 0