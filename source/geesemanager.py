#!/usr/bin/python

import goose.entity as entity
import goose.clan as clan

from db.database import Database

import sys
import os
import json
import random
import cPickle as pickle


dbs = 'null'

WELCOMEMSG = '''


 _______ _______ _______ _______ _______ _______ _______
|\     /|\     /|\     /|\     /|\     /|\     /|\     /|
| +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |
| |   | | |   | | |   | | |   | | |   | | |   | | |   | |
| |F  | | |R  | | |A  | | |G  | | |I  | | |L  | | |E  | |
| +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |
|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|


 _______ _______ _______ _______ _______
|\     /|\     /|\     /|\     /|\     /|
| +---+ | +---+ | +---+ | +---+ | +---+ |
| |   | | |   | | |   | | |   | | |   | |
| |G  | | |E  | | |E  | | |S  | | |E  | |
| +---+ | +---+ | +---+ | +---+ | +---+ |
|/_____\|/_____\|/_____\|/_____\|/_____\|


 _______ _______ _______ _______ _______ _______ _______ _______ _______
|\     /|\     /|\     /|\     /|\     /|\     /|\     /|\     /|\     /|
| +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |
| |   | | |   | | |   | | |   | | |   | | |   | | |   | | |   | | |   | |
| |S  | | |I  | | |M  | | |U  | | |L  | | |A  | | |T  | | |O  | | |R  | |
| +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |
|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|

'''


def printArray(geesearray):
    for goose in geesearray:
        print goose


def getGooseFromHash(geesearray, hashid):
    for goose in geesearray:
        if str(goose.hashid) == str(hashid):
            return goose


def createDistributedClan(size, x, y, dist):
    return clan.Clan(clan.generateRandomDistributedClan(size, x, y, dist))


def createClan(size, x, y):
    print 'Use random data? (y/n)'
    if str(raw_input('---> ')) == 'y':
        geesearray = clan.generateRandomClan(size, x, y)
        print 'Finished generating clan.'
        return clan.Clan(geesearray)
    else:
        geesearray = []
        for gooseCount in range(size):
            geesearray.append(createClanGoose(x, y))
        print 'Finished generating clan.'
        return clan.Clan(geesearray)


def createGeese(count):
    print 'Use random data? (y/n)'
    geesearray = []
    if str(raw_input('---> ')) == 'y':
        for gooseCount in range(count):
            geesearray.append(entity.generateRandomGoose())
        return geesearray
        print 'Finished generating ' + count + ' geese.'
    else:
        for gooseCount in range(count):
            geesearray.append(createGoose())
        return geesearray
        print 'Finished generating ' + count + ' geese.'


def createGoose():
    print 'Use random data? (y/n)'
    if str(raw_input('---> ')) == 'y':
        return entity.generateRandomGoose()
    else:
        return entity.Goose(str(raw_input('name ---> ')), int(raw_input('age (d) ---> ')), float(raw_input('span (d) ---> ')), float(raw_input('health ---> ')), float(raw_input('hunger ---> ')), entity.Location(float(raw_input('X: ')), float(raw_input('Y: '))), int(raw_input('gender ---> ')), float(raw_input('range ---> ')))


def createClanGoose(x, y):
    return entity.Goose(str(raw_input('name ---> ')), int(raw_input('age (d) ---> ')), float(raw_input('span (d) ---> ')), float(raw_input('health ---> ')), float(raw_input('hunger ---> ')), entity.Location(x, y), int(raw_input('gender ---> ')), float(raw_input('range ---> ')))


def exit():
    print '*quack*'
    print 'The geese will find you!'
    sys.exit(1)


def clear():
    for i in range(100):
        print
    return


def export(obj, file):
    if mode == 0:
        pickle.dump(obj, open(file, 'wb'))
    elif mode == 1:
        print 'We have no support for JSON, woops!'
    else:
        print 'Wrong mode. Try 0 (pkl) or 1 (json).'


def start(geeseclan):
    daystorun = int(raw_input('simulation time (d) ---> '))
    for d in range(daystorun):
        print '#### #### ' + str(d) + ' #### ####'
        update(geeseclan)


def distributeGeese(count):
    return clan.Clan(createGeese(count))


def update(geeseclan):
    global dbs
    dbs.Save(geeseclan.geese)
    for goose in geeseclan.geese:
        if goose.isAlive:
            goose.decayAge()
            goose.decayLifespan()
            goose.decayHunger()
            goose.decayHealth()
            goose.feed()

            if random.randrange(0, 1000) < 5:
                goose.mate(geeseclan)

        if random.randrange(0, 200) < 5:
            goose.health -= 5

        if random.randrange(0, 1000) < 3:
            goose.die()

    geeseclan.ageAllEggs()


if __name__ == '__main__':
    IP = str(raw_input('ip: '))
    PORT = str(raw_input('port: '))
    dbs = Database(str(IP) + ':' + str(PORT))
    dbs.Delete()
    dbs.Create()
    print WELCOMEMSG
    while(True):
        exec(str(raw_input('#: ')))
