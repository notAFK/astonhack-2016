#!/usr/bin/python

import goose.entity
import sys
import os

WELCOMEMSG = '''
 ____ ____ ____ ____ ____
||G |||E |||E |||S |||E ||
||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|

   _____ _____ __  __ _    _ _            _______ ____  _____
  / ____|_   _|  \/  | |  | | |        /\|__   __/ __ \|  __ \\
 | (___   | | | \  / | |  | | |       /  \  | | | |  | | |__) |
  \___ \  | | | |\/| | |  | | |      / /\ \ | | | |  | |  _  /
  ____) |_| |_| |  | | |__| | |____ / ____ \| | | |__| | | \ \\
 |_____/|_____|_|  |_|\____/|______/_/    \_\_|  \____/|_|  \_\\
'''


def createClan(size):
    pass


def createGoose():
    pass


def harvestClan(size):
    pass


def harvestGoose():
    return goose.entity.Goose(str(raw_input('name ---> ')), int(raw_input('age (d) ---> ')), int(raw_input('span (d) ---> ')), int(raw_input('health ---> ')), int(raw_input('hunger ---> ')), goose.entity.Location(int(raw_input('X: ')), int(raw_input('Y: '))), int(raw_input('gender ---> ')))


if __name__ == '__main__':

    print 'Select one option:'
    print '1) Generate individual geese.'
    print '2) Generate geese clan.'
    print '3) Exit program.'
    INPUT = int(raw_input('---> '))
    if INPUT == 1:
        pass
    elif INPUT == 2:
        pass
    elif INPUT == 3:
        pass
    else:
        pass
