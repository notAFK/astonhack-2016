import hashlib
import os
import sys


class Goose:
    __doc__ = ''' Class that stores the goose essentials. '''

    __HUNGERTHRESHOLD = 30

    hashid = 'null'
    name = 'null'
    age = 'null'
    hunger = 'null'
    location = 'null'

    def __init__(self, _name, _age, _hunger, _location):
        self.hashid = hashlib.sha256(os.urandom(32)).hexdigest()
        self.name = _name
        self.age = _age
        self.hunger = _hunger
        self.location = _location

    def __str__(self):
        return self.name + ':' + self.hashid[0:6] + ':AGE(' + str(self.age) + ')' + ':HUNGER(' + str(self.hunger) + '):' + str(self.location)
