from datetime import datetime

def get_days_from_today(date):
    given_date = datetime.strptime(date, "%Y-%m-%d").date()
    current_date = datetime.today().date()
    delta = current_date - given_date
    return delta.days
