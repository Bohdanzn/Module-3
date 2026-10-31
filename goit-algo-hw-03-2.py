import random

def get_numbers_ticket(min_val, max_val, quantity):
    if not (1 <= min_val <= max_val <= 1000):
        return []
    if not (1 <= quantity <= (max_val - min_val + 1)):
        return []
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min_val, max_val))
    return sorted(list(numbers))

