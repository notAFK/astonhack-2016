#!/usr/bin/python

import goose
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

INPUT = 'null'


def makeGoose():
    pass


def makeClan():
    pass


def harvestGooseData():
    name = str(raw_input('name ---> '))
    age = int(raw_input('age (days) ---> '))
    lifespan = int(raw_input('lifespan (days) ---> '))
    health = int(raw_input('health ---> '))
    hunger = int(raw_input('hunger ---> '))
    print '0) Female'
    print '1) Male'
    print '2) Apache attack helicopter'
    gender = int(raw_input('gender --->'))
    location = raw_input('location (x,y) ---> ').split(',')
    return [name, age, lifespan, health, hunger, gender, location]


def getSelection():
    print 'Select one of the options:'
    print '1) Generate one goose.'
    print '2) Generate multiple geese.'
    print '3) Exit.'
    INPUT = int(raw_input('---> '))
    if INPUT == 1:
        print 'Select one of the options:'
        print '1) Generate a random goose.'
        print '2) Generate a goose with custom data.'
        INPUT = int(raw_input('---> '))
        if INPUT == 1:
            pass  # MAKE ONE RANDOM GOOSE AND STORE IT ...
        elif INPUT == 2:
            print harvestGooseData()
    elif INPUT == 2:
        print 'How many?'
        INPUT = int(raw_input('---> '))
        if not type(INPUT) is int:
            print '*quack*'
            sys.exit()
        else:
            print 'Do you want random geese? (yes/no)'
            INPUT = str(raw_input('---> '))
            if INPUT == 'yes':
                pass  # DO YES STUFF
            elif INPUT == 'no':
                pass  # DO NO STUFF
            else:
                print '*quack*'
                sys.exit()
    elif INPUT == 3:
        print 'The geese will find you!'
        sys.exit()
    else:
        print '*quack*'
        getSelection()


if __name__ == '__main__':
    print WELCOMEMSG

    getSelection()
