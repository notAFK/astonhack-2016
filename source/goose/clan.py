import os
import sys
import hashlib
import random

from entity import Location
from entity import Goose


__MAXSIZE = 100
__MINSIZE = 10


def generateClan(_fixed=0, _min=__MINSIZE, _max=__MAXSIZE):
    _CLAN = []
    if _fixed != 0:
        _range = _fixed
    else:
        _range = random.randrange(_min, _max+1)

    for count in range(_range):
        _CLAN.append(Goose('goose'+str(count), 8000, 100, 0, Location(4, 5), 'male'))

    return _CLAN


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
