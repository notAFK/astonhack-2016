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

    def getLenght(self):
        return len(self.geese)


def generateRandomClan(_count):
    _geesearray = []
    for count in range(_count+1):
        _geesearray.append(entity.generateRandomGoose())
    return _geesearray
