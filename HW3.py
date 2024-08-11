import datetime
from datetime import datetime
import random
import re

#First task

def get_days_from_today(date):
    try:
        a = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.now()
        diff = (today - a) 
        print(diff.days)
        return diff.days
    except ValueError:
        print(f"Date should be in 'YYYY-MM-DD' format")
get_days_from_today("2024-07-31")

#Second task

def get_numbers_ticket(min, max, quantity):
    nlist = []
    if min > 0:
        if 0 < max < 1000:
            if ((max+1)-min)>=quantity:
                lst = list(range(min, max + 1))
                nlist = (random.sample(lst, quantity))
                nlist.sort()
                return nlist
            return nlist
        return nlist
    return nlist
get_numbers_ticket(1, 49, 6)

# Third task

def normalize_phone(phone_number = str):
    
    pattern = r"\d"
    matches = re.findall(pattern, phone_number )
    phone_number = "".join(matches)
    phone_number = phone_number[-10:-1]
    phone_number = "+38" + phone_number
    
    return phone_number
normalize_phone("067\\t123 4567")


