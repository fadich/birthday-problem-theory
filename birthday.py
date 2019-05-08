import random

from typing import Tuple


class Model(object):

    def __init__(self, people_number: int):
        self.people: Tuple = tuple(Model.generate_birthdays(people_number))

    @staticmethod
    def generate_birthdays(people_number: int):
        return (random.randint(0, 364) for i in range(people_number))

    @property
    def has_coincidence(self):
        length = len(self.people)
        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                if self.people[i] == self.people[j]:
                    return True
        return False
