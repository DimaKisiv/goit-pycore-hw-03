
from datetime import datetime
from datetime import timedelta

date_format = "%Y.%m.%d"
#returns day to congratulate user depending of his birthday
def get_upcoming_birthdays(users):
    users_to_congratulate = []
    today_date = datetime.today().date()
    for user in users:
        user_birthday_date = get_this_year_birthday(user, today_date)
        if (user_birthday_date is not None 
        and is_birthday_within_next_seven_days(user_birthday_date, today_date)):
            users_to_congratulate.append(get_congratulation_user(user["name"], user_birthday_date))
    return users_to_congratulate

#to compare with todays date we need a date wtih this year
def get_this_year_birthday(user, today_date):
    try:
        user_birthday_date = datetime.strptime(user["birthday"], date_format).date()
        return datetime(today_date.year, user_birthday_date.month, user_birthday_date.day).date()
    except: 
        return None

def is_birthday_within_next_seven_days(user_birthday_date, today_date):
    days_diff = (user_birthday_date - today_date).days
    return days_diff >= 0 and days_diff < 7

def get_congratulation_user(user_name, user_birthday_date):
    congratulation_date = datetime.strftime(user_birthday_date, date_format)
    day_number = user_birthday_date.weekday() + 1
    if (day_number) > 5:
        offset = 8-day_number
        user_birthday_date = user_birthday_date + timedelta(days=offset)
        congratulation_date = datetime.strftime(user_birthday_date, date_format)
    return {"name": user_name, "congratulation_date": congratulation_date}

users = [
    {"name": "yesterday", "birthday": "1985.07.01"},
    {"name": "today", "birthday": "1985.07.02"},
    {"name": "John Doe", "birthday": "1985.07.03"},
    {"name": "Jane Smith", "birthday": "1990.07.05"},
    {"name": "Weekend Saturday", "birthday": "2024.07.06"},
    {"name": "Weekend Sunday", "birthday": "2024.07.07"},
    {"name": "Broken User", "birthday": "2024.07.06_bad_format"}
]

print(get_upcoming_birthdays(users))