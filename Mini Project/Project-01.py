import random


def roll():
    min_value = 100000
    max_value = 999999
    roll = random.randint(min_value, max_value)

    return roll


value = roll()

print(value)