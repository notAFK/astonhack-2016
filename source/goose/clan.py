import os
import sys
import hashlib
import random

import entity
from entity import Location
from entity import Goose


class Clan:
    hashid = 'null'
    geese = []

    def __init__(self, _geesearray):
        self.geese = _geesearray
        self.hashid = hashlib.sha256(os.urandom(32)).hexdigest()[0:8]

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


def generateRandomClan(_count, x, y):
    _geesearray = []
    _location = Location(x, y)
    for count in range(_count):
        _geesearray.append(entity.generateRandomClanGoose(_location))
    return _geesearray
