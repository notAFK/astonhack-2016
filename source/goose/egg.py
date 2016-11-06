import random


class Egg:
    def __init__(self):
        self.days = random.randrange(24, 29)

    def __str__(self):
        return str(self.days)
