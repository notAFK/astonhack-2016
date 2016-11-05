import hashlib
import os
import sys
import random


GLOBALIDCOUNT = 0


class Location:
    x = 666
    y = 666

    def __init__(self, _x=0, _y=0):
        self.x = _x
        self.y = _y

    def random(self):
        self.x = random.randrange(-180.0, 180.0)
        self.y = random.randrange(-90.0, 90.0)

    def __str__(self):
        return str(self.x) + ',' + str(self.y)


class Goose:
    __doc__ = ''' Class that stores the goose essentials. '''

    def __init__(self, _name, _age, _lifespan,
                 _health, _hunger, _location, _gender):

        global GLOBALIDCOUNT
        self.id = GLOBALIDCOUNT
        GLOBALIDCOUNT += 1

        self.hashid = hashlib.sha256(os.urandom(32)).hexdigest()[0:8]

        self.name = _name
        self.lifespan = _lifespan
        self.hunger = _hunger
        self.health = _health
        self.location = _location
        self.gender = _gender
        self.age = _age

    def __str__(self):
        return self.hashid

    def decayLifespan(self):
        _decay = 1.0
        if self.health <= 70.0:
            _decay += 40.0/self.health
        self.lifespan -= _decay

    def getAll(self):
        for key, value in self.__dict__.items():
            print key, ':', value


def generateRandomGoose():
    _name = 'goose'
    _lifespan = random.randrange(4000.0, 8000.0 + 1.0)
    _hunger = random.randrange(80.0, 100.0 + 1.0)
    _health = random.randrange(90.0, 100.0 + 1.0)
    _location = Location(0, 0)
    _gender = 'male' if random.randrange(0, 2) == 0 else 'female'
    _age = random.randrange(0, 4 + 1)

    return Goose(_name, _age, _lifespan, _health, _hunger, _location, _gender)
