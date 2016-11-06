import hashlib
import os
import sys
import random
import math


GLOBALIDCOUNT = 0


class Location:
    x = 666
    y = 666

    def __init__(self, _x=0, _y=0):
        self.x = _x
        self.y = _y

    def random(self):
        _x = random.uniform(-180.0, 180.0)
        _y = random.uniform(-90.0, 90.0)
        return Location(_x, _y)

    def __str__(self):
        return str(self.x) + ',' + str(self.y)


class Goose:
    __doc__ = ''' Class that stores the goose essentials. '''

    __GENDER = {0: 'female', 1: 'male', 2: 'apache attack helicopter'}
    __MAXLIFE = 8000

    def __init__(self, _name, _age, _lifespan,
                 _health, _hunger, _location, _gender, _range=12):

        global GLOBALIDCOUNT
        self.id = GLOBALIDCOUNT
        GLOBALIDCOUNT += 1

        self.hashid = hashlib.sha256(os.urandom(32)).hexdigest()[0:8]

        self.name = _name
        self.lifespan = _lifespan
        self.hunger = _hunger
        self.health = _health
        self.location = _location
        self.gender = _gender
        self.age = _age
        self.isAlive = True
        self.range = _range
        self.migrateCounter = 0
        self.saved = False
        self.matecooldown = 0

    def __str__(self):
        return self.hashid

    def decayLifespan(self):
        _decay = 1.0
        if self.health <= 70.0:
            _decay += 40.0/self.health
        self.lifespan -= _decay
        if self.lifespan <= 0:
            print self.__str__() + ' reached his lifespan.'
            self.die()

    def decayHunger(self):
        _decay = 3.0
        if self.hunger <= 30:
            _decay += 1.0
        self.hunger -= _decay
        if self.hunger <= 0:
            print self.__str__() + ' starved.'
            self.die()

    def decayHealth(self):
        _decay = 0.01
        if self.hunger <= 30:
            _decay += 1.0
            _decay += (30 - self.hunger)/10
            if self.health <= 0:
                print self.__str__() + ' had bad health.'
                self.die()

    def decayAge(self):
        self.age += 1
        self.matecooldown -= 1
        if self.age > Goose.__MAXLIFE:
            print self.__str__() + ' has reached the golden age.'
            self.die()

    def die(self):
        print self.__str__() + ' died.'
        self.isAlive = False

    def migrate(self, x, y):
        distance = math.sqrt((self.location.x - x)**2 + (self.location.y - y)**2)
        if self.migrateCounter == 0:
            self.migrateCounter = int(distance/self.range)
        if self.migrateCounter == 0:
            self.move(x, y)
        if self.migrateCounter > 0:
            self.migrateCounter -= 1
            if self.migrateCounter == 0:
                self.move(x, y)

    def move(self, x, y):
        distance = math.sqrt((self.location.x - x)**2 + (self.location.y - y)**2)
        if distance <= self.range:
            print self.__str__() + ' moved from ' + self.location + ' to ' + Location(x, y)
            self.location = Location(x, y)

    def printAll(self):
        for key, value in self.__dict__.items():
            if key != 'gender':
                print key, ':', value
            else:
                print key, ':', Goose.__GENDER[value]

    def feed(self):
        # check if there is food around.
        # if there is add food
        # else dont!
        pass

    def mate(self, geeseclan):
        if self.matecooldown <= 0:
            for goose in geeseclan:
                if goose.gender != self.gender:
                    if goose.age >= 720:
                        print self.__str__() + ' started reproduction with ' + goose.__str__()
                        geeseclan.addEggs(random.randrange(2, 10))
                        self.matecooldown = 180
                        return


def generateRandomGoose():
    _name = 'goose'
    _lifespan = random.uniform(4000.0, 8000.0 + 1.0)
    _hunger = random.uniform(80.0, 100.0 + 1.0)
    _health = random.uniform(90.0, 100.0 + 1.0)
    _location = Location().random()
    _gender = random.randrange(0, 1 + 1)
    _age = random.randrange(200, 1000 + 1)

    return Goose(_name, _age, _lifespan, _health, _hunger, _location, _gender)


def generateRandomClanGoose(location):
    _name = 'goose'
    _lifespan = random.uniform(4000.0, 8000.0 + 1.0)
    _hunger = random.uniform(80.0, 100.0 + 1.0)
    _health = random.uniform(90.0, 100.0 + 1.0)
    _location = location
    _gender = random.randrange(0, 1 + 1)
    _age = random.randrange(200, 1000 + 1)

    return Goose(_name, _age, _lifespan, _health, _hunger, _location, _gender)


def killGoose(goose):
    goose.isAlive = False

    return Goose(_name, _age, _lifespan, _health, _hunger, _location, _gender)
