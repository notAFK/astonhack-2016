import os
import sys
import hashlib
import random
from entity import Goose


__MAXSIZE = 100
__MINSIZE = 10


def generateClan(_min=__MINSIZE, _max=__MAXSIZE, _fixed=0):
    _CLAN = []
    if _fixed != 0:
        _range = _fixed+1
    else:
        _range = random.randrange(_min, _max+1)

    for count in range(_range):
        _CLAN.append(Goose('goose'+str(count), 0, 0, 'xy'))

    return _CLAN


class Clan:
    hashid = 'null'
    geese = []

    def __init__(self, _geesearray):
        self.geese = _geesearray
        self.hashid = hashlib.sha256(os.urandom(32)).hexdigest()[0:8]

    def __str__(self):
        _string = 'CLAN:' + self.hashid

        for goose in self.geese:
            _string += (goose.__str__() + '\n')

        return _string
