import datetime

def countdown(target_date):
    
    now = datetime.datetime.now()
    
    
    delta = target_date - now
    
    days = delta.days
    seconds = delta.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    
    print(f"Time remaining until {target_date}: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

target_date = datetime.datetime(2024, 12, 31, 23, 59, 59)
countdown(target_date)
