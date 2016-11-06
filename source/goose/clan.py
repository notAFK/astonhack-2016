import os
import sys
import hashlib
import random

import entity
from entity import Location
from entity import Goose
from egg import Egg


class Clan:
    hashid = 'null'
    geese = []

    def __init__(self, _geesearray):
        self.geese = _geesearray
        self.hashid = hashlib.sha256(os.urandom(32)).hexdigest()[0:8]
        self.eggs = []

    def __str__(self):
        _string = 'CLAN:' + self.hashid + '\n'

        for goose in self.geese:
            _string += (goose.hashid + '\n')

        return _string

    def __len__(self):
        return len(self.geese)

    def __getitem__(self, index):
        return self.geese[index]

    def printAll(self):
        for goose in self.geese:
            goose.printAll()
            print

    def printAlive(self):
        for goose in self.geese:
            if goose.isAlive:
                goose.printAll()
                print

    def addEggs(self, count):
        for c in range(count):
            self.eggs.append(Egg())

    def addGoose(self, goose):
        self.geese.append(goose)

    def ageAllEggs(self):
        for egg in self.eggs:
            egg.days -= 1
            if egg.days == 0:
                self.addGoose(Goose('newborn', 0, random.uniform(4000.0, 8000.0), 100.0, 100.0, self.geese[0].location, random.randrange(0, 2)))
                print 'EGG HATCHED: ' + self.geese[len(self.geese)-1]


def generateRandomClan(_count, x, y):
    _geesearray = []
    _location = Location(x, y)
    for count in range(_count):
        _geesearray.append(entity.generateRandomClanGoose(_location))
    return _geesearray
