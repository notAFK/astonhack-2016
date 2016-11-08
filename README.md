ASTON HACK 2016
===
###### Geese themed hackathon!

[![npm license](https://img.shields.io/npm/l/awesome-badges.svg)](https://github.com/thee-engineer/astonhack-2016)
![AstonHack2016 Status](https://img.shields.io/badge/astonhack2016-winner-orange.svg)
![Docker IMG](https://img.shields.io/badge/docker-image-blue.svg)

###### Travis CI Status
[![Build Status](https://travis-ci.com/thee-engineer/astonhack-2016.svg?token=ySNrvJx6Lqs7r3y3HqKN&branch=master)](https://travis-ci.com/thee-engineer/astonhack-2016)

![Goose](https://astonhack.co.uk/images/ah-goose.png )

# Description
Fragile/Swarming Geese Simulator, is a Python program that "simulates" the
behaviour of geese (a common theme around Birmingham). The main idea was to
create the activity history of groups and individual geese and then plot their
actions on a map (using **Google Maps API**). The history is stored using the **crate.io**
database.

### How to run the program.
```python
source/geesemanager.py
```
This will start a custom "shell" that allows you to call some of the main
functions of the program. You can also use RAW Python if you wish.

Inside the "shell" you can run:
```python
jimmy = createGoose()
```
This will start a "wizzard" to help you define
Jimmy, you can either use random data or custom
data.
```python
jimmy = createGoose()
Use random data? (y/n)
---> y
>_
```
Now we have a random goose in 'jimmy'.
```python
print jimmy
89e129f6
>_
```
Printing 'jimmy' like that will return the hashid.


If we were to choose custom data for 'jimmy', the
setup would look like this:
```python
>_ jimmy = createGoose()
Use random data? (y/n)
---> n
name ---> Jimmy
age (d) ---> 600
span (d) ---> 600
health ---> 200
hunger ---> 300
X: 90
Y: 80
gender ---> 2
range ---> 55
>_
```

### Creating a clan.

```python
>_ someclan = createClan(50,0,2)
# 50 is the number of geese.
# 0 is the X coordinate.
# 2 is the Y coordinate.
```

### Simulating a clan.

```python
>_ start(someclan)
# After this you are prompted to give a date.
# Then hell breaks loose!!!
# Some geese die, some are born, overall they win!
```

### More
For more information on what the program can do, look at the functions defined inside *source/geesemanager.py*

---
# crate.io
The program tries to connect to a crate.io database, so make sure you have one running
```shell
crate/crate # Linux/Mac
```
and when asked provide the ip and port:
```python
# Should work on most machines!
ip: localhost
port: 4200
```
After this, Python connects to the database and stores data about the geese! AMAZING!
