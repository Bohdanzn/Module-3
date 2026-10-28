from random import randint
get_numbers_tickets = set()

while len(get_numbers_tickets) < 6:
    get_numbers_tickets.add(randint(1, 49))
    

print(sorted(get_numbers_tickets))
