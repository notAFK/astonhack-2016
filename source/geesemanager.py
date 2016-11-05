#!/usr/bin/python

import goose.entity
import goose.clan

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
    print 'Use random data? (y/n)'
    if str(raw_input('---> ')) == 'y':
        geesearray = goose.clan.generateRandomClan(size)
        print 'Finished generating clan.'
        return goose.clan.Clan(geesearray)
    else:
        geesearray = []
        for gooseCount in range(size):
            geesearray.append(harvestGoose())
        print 'Finished generating clan.'
        return goose.clan.Clan(geesearray)


def createGeese(count):
    print 'Use random data? (y/n)'
    geesearray = []
    if str(raw_input('---> ')) == 'y':
        for gooseCount in range(count):
            geesearray.append(goose.entity.generateRandomGoose())
        return geesearray
        print 'Finished generating ' + count + ' geese.'
    else:
        for gooseCount in range(count):
            geesearray.append(harvestGoose())
        return geesearray
        print 'Finished generating ' + count + ' geese.'


def createGoose():
    return goose.entity.Goose(str(raw_input('name ---> ')), int(raw_input('age (d) ---> ')), int(raw_input('span (d) ---> ')), int(raw_input('health ---> ')), int(raw_input('hunger ---> ')), goose.entity.Location(int(raw_input('X: ')), int(raw_input('Y: '))), int(raw_input('gender ---> ')))


def exit():
    print '*quack*'
    print 'The geese will find you!'
    sys.exit()


def clear():
    for i in range(100):
        print
    return


if __name__ == '__main__':
    print WELCOMEMSG
    while(True):
        exec(str(raw_input('>_ ')))


'''
if __name__ == '__main__':
    print WELCOMEMSG

    print 'Select one option:'
    print '1) Generate individual geese.'
    print '2) Generate geese clan.'
    print '3) Exit program.'
    INPUT = int(raw_input('---> '))
    if INPUT == 1:
        createGeese(int(raw_input('count ---> ')))
    elif INPUT == 2:
        createClan(int(raw_input('size ---> ')))
    elif INPUT == 3:
        print 'The geese will find you!'
        sys.exit()
    else:
        print '*quack*'
        sys.exit()
'''
