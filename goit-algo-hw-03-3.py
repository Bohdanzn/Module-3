import re
def normalize_phone_number(phone_number):
    phone = re.sub(r'[^\d]', "", phone_number)
    if phone.startswith('380'):
        return f'+{phone}'
    elif phone.startswith('0'):
        return f'+38{phone}'
    else:
        return f'+380{phone}'
raw_numbers = [
     "067\t123 4567" ,
     "(095) 234-5678\n" ,
     "+380 44 123 4567" ,
     "380501234567" ,
     "+38(050) 14533" ,
     "(050)8889900" ,
     "38050-111-22-22" ,
     "38050 111 22 11" ,
]
sanitized_numbers = [normalize_phone_number(num) for num in raw_numbers]
print("Нормалізовані телефонні номери для SMS-розсилки:", sanitized_numbers)