import hashlib
import os
import sys
import random


GLOBALIDCOUNT = 0


class Location:
    x = 666
    y = 666

    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def random(self):
        self.x = random.randrange(-180, 180)
        self.y = random.randrange(-90, 90)


class Goose:
    __doc__ = ''' Class that stores the goose essentials. '''

    def __init__(self, _name, _age, _lifespan, _health, _hunger, _location, _gender):
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
        _decay = 1
        if self.health <= 70:
            _decay += 40/self.health
        self.lifespan -= _decay
