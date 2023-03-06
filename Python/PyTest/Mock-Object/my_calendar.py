from datetime import datetime

def is_weekday():
    today = datetime.today()
    print(today)
    # for date, time in today:
    #     print(f" Today date {date} and current time we are {time}")
   
    # Python's datetime library treats Monday as 0 and Sunday as 1
    return (0 <= today.weekday() < 5)


# Test if today is a weekday
assert is_weekday()