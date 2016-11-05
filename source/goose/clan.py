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
        _range = _fixed
    else:
        _range = random.randrange(_min, _max)

    for count in range(_range):
        _CLAN.append(Goose('geese'+str(count), 0, 0, 'xy'))

    return _CLAN


class Clan:
    hashid = 'null'
    geese = []

    def __init__(self, _geesearray):
        self.geese = _geesearray
        self.hashid = hashlib.sha256(os.urandom(32)).hexdigest()

    def __str__(self):
        _string = 'CLAN:' + hashid

        for goose in self.geese:
            _string.append(goose + '\n')

        return _string

jimmyclan = Clan(generateClan(0, 0, 10))
print jimmyclan
