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


def getSelection():
    print 'Select one of the options:'
    print '0) Generate one goose.'
    print '1) Generate two goose.'
    print '2) Generate multiple geese.'
    print '3) Exit.'

    INPUT = int(raw_input('---> '))
    if INPUT == 0:
        makeGoose()
    elif INPUT == 1:
        makeGoose()
        makeGoose()
    elif INPUT == 2:
        makeClan()
    elif INPUT == 3:
        sys.exit()
    else:
        print 'WUT?'
        getSelection()

if __name__ == '__main__':
    print WELCOMEMSG

    getSelection()
