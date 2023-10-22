import random
from game_data import data


def get_random_item():
    random_item = random.choice(data)
    print(random_item)
    return random_item


first_item = {}
first_item = get_random_item()
print(f"test {first_item['name']}")
