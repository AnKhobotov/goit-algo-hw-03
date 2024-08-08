import datetime
from datetime import datetime
import random
import re

#First task

def getDaysFromToday(datum):
    try:
        datum = str(datum)
        a = datetime.strptime(datum, "%Y.%m.%d").date()
        today = datetime.now().date()
        diff = (today - a) 
        print(diff.days)
        return diff.days
    except ValueError:
        print(f"Datum should be in 'YYYY-MM-DD' format")
getDaysFromToday("2024.07.31")

#Second task

def get_numbers_ticket(min, max, quantity=int):
    num_set = set()
    nlist = list(num_set)
    if min > 0:
        if 0 < max < 1000:
            if min < quantity < max:        
                while int(len(num_set))<quantity:
                    a = random.randint(min, max)
                    num_set.add(a)
                nlist= list(num_set)
                nlist.sort()
            return nlist
        return nlist
    return nlist
    
get_numbers_ticket(1, 49, 6) 

# Third task
def normalize_phone(phone_number = str):
    raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "]

    phone_number = str
    sanitized_numbers = []
    for item in raw_numbers:
        pattern = r"\d"
        matches = re.findall(pattern, item )
        item = "".join(matches)
        item = item[-10:-1]
        item = "+38" + item
        sanitized_numbers.append(item)
        
    # for phone_number in raw_numbers:
    #     phone_number = phone_number
    #     phone_number.strip()
    #     pattern = r"[\-\(\)\.\s]"
    #     repl = ""
    #     phone_number = re.sub(pattern, repl, phone_number)
    #     phone_number = phone_number[-10:-1]
    #     phone_number = "+38" + phone_number
    #     san_num.append(phone_number)

    # for i[0:1] in phone_number:
    # if phone_number.find("38") is True:
    #     phone_number = "+".join(phone_number)
    #     print(phone_number)
    #     return phone_number
    # return phone_number
    print(sanitized_numbers)
normalize_phone("38050 111 22 11   ")

