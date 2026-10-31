import re

def normalize_phone_number(phone_number):
    cleaned = re.sub(r'[^\d+]', "", phone_number)
    digits = re.sub(r'[^\d]', "", phone_number)
    has_plus = phone_number.strip().startswith('+')
    if has_plus:
        return f"+{digits}"
    if digits.startswith('380'):
        return f"+{digits}"
    elif digits.startswith('0'):
        return f"+38{digits}"
    else:
        return f"+38{digits}"

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