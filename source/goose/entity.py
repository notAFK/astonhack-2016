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
        _x = random.uniform(-180.0, 180.0)
        _y = random.uniform(-90.0, 90.0)
        return Location(_x, _y)

    def __str__(self):
        return str(self.x) + ',' + str(self.y)


class Goose:
    __doc__ = ''' Class that stores the goose essentials. '''

    __GENDER = {0: 'female', 1: 'male', 2: 'apache attack helicopter'}

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

    def printAll(self):
        for key, value in self.__dict__.items():
            if key != 'gender':
                print key, ':', value
            else:
                print key, ':', Goose.__GENDER[value]


def generateRandomGoose():
    _name = 'goose'
    _lifespan = random.uniform(4000.0, 8000.0 + 1.0)
    _hunger = random.uniform(80.0, 100.0 + 1.0)
    _health = random.uniform(90.0, 100.0 + 1.0)
    _location = Location().random()
    _gender = random.randrange(0, 1 + 1)
    _age = random.randrange(0, 4 + 1)

    return Goose(_name, _age, _lifespan, _health, _hunger, _location, _gender)


def generateRandomClanGoose(location):
    _name = 'goose'
    _lifespan = random.uniform(4000.0, 8000.0 + 1.0)
    _hunger = random.uniform(80.0, 100.0 + 1.0)
    _health = random.uniform(90.0, 100.0 + 1.0)
    _location = location
    _gender = random.randrange(0, 1 + 1)
    _age = random.randrange(0, 4 + 1)

    return Goose(_name, _age, _lifespan, _health, _hunger, _location, _gender)
