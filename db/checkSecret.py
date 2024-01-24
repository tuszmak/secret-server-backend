from datetime import datetime
def check_secret(secret):
    return check_time(secret[4]) and check_visit_number(3)

def check_time(time):
    return time < datetime.now()
def check_visit_number(number):
    return number > 0