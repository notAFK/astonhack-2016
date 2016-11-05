import hashlib
import os
import sys


class Location:
    x = 666
    y = 666

    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y


class Goose:
    __doc__ = ''' Class that stores the goose essentials. '''

    __HUNGERTHRESHOLD = 30
    __AVERAGELIFESPAN = 8000
    __MAXHUNGER = 100

    hashid = 'null'
    name = 'null'
    age = 'null'
    hunger = 'null'
    location = 'null'
    health = 'null'

    def __init__(self, _name, _age, _health, _hunger, _location):
        self.hashid = hashlib.sha256(os.urandom(32)).hexdigest()[0:8]
        self.name = _name
        self.age = _age
        self.hunger = _hunger
        self.health = _health
        self.location = _location

    def __str__(self):
        _string = self.hashid
        _string += (':' + self.name + '\n')
        _string += ('AGE:' + str(self.age) + ' HUNGER:' + str(self.hunger) + ' HEALTH:' + str(self.health))
        _string += ('\n' + 'X:' + str(self.location.x) + ', Y:' + str(self.location.y))

        return _string
