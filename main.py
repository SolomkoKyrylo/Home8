from collections import defaultdict
from datetime import date, timedelta


def get_birthdays_per_week(users):
    today = date.today()
    next_week = today + timedelta(days=7)
    # current_weekday = today.weekday()
    birthdays_per_week = defaultdict(list)
    for user in users:
        birthday: date = user["birthday"]
        name = user["name"]
        this_year_bd = birthday.replace(year=today.year)
        if this_year_bd < today:
            this_year_bd = this_year_bd.replace(year=this_year_bd.year + 1)
        if today <= this_year_bd <= next_week:
            birthday_weekday = this_year_bd.weekday()
            # if birthday_weekday < current_weekday:
            #     birthday_weekday += 7
            # day_of_week = list(birthdays_per_week.keys())[birthday_weekday - current_weekday]
            if birthday_weekday in [5, 6]:
                birthdays_per_week["Monday"].append(name)
            else:
                birthdays_per_week[this_year_bd.strftime("%A")].append(name)
    return birthdays_per_week

if __name__ == "__main__":
    users = [
        {"name": "Bill Gates", "birthday": date(1955, 10, 28)},
        {"name": "Jan", "birthday": date(1990, 10, 18)},
        {"name": "Kim", "birthday": date(1985, 10, 19)}
    ]
    result = get_birthdays_per_week(users)
    print(result)
