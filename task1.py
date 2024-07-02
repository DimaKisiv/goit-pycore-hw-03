from datetime import datetime

#function calculates difference between todays date and specified date, in days
def get_days_from_today(date):
    
    today = datetime.today()
    date_obj = parse_date_str(date)
    if (date_obj):
        return (date_obj - today).days

#parse and return date in format %Y-%m-%d and returns None if exception
def parse_date_str(date_str):
    date_format = "%Y-%m-%d"
    try:
        return datetime.strptime(date_str, date_format)
    except Exception as error:
        print(f"Date has wrong format. It must be {date_format}")
        print(f"InnerException: {error}")
        return None

print(f"2024-07-05 - today = {get_days_from_today("2024-07-05")} days")
print(f"2024-07-01 - today = {get_days_from_today("2024-07-01")} days")
print(f"2024-07-05asd - today = {get_days_from_today("2024-07-05asd")} days")
