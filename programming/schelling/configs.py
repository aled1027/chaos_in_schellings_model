import logging
from ca import Person, SchellingCA
import random

def config1(width=8,height=8):
    always_happy = {'white' : (0,1), 'black' : (0,1)}
    never_happy = {'white' : (1,1), 'black' : (1,1)}
    half_happy = {'white' : (.25,.75), 'black' : (.25,.75)}
    hates_blacks = {'white' : (0,1), 'black' : (0,0)}
    ret = []
    for i in range(width):
        li = []
        for j in range(height):
            li.append(Person(preferences=always_happy, race='white'))
        ret.append(li)
    ret[0][0] = (Person(preferences=always_happy, race='black'))
    ret[0][1] = (Person(preferences=hates_blacks, race='white'))
    ret[7][7] = None
    return ret

def config_mixed(width=8,height=8):
    always_happy = {'white' : (0,1), 'black' : (0,1)}
    never_happy = {'white' : (1,1), 'black' : (1,1)}
    half_happy = {'white' : (.25,.75), 'black' : (.25,.75)}
    hates_blacks = {'white' : (0,1), 'black' : (0,0)}
    ret = []
    for i in range(width):
        li = []
        for j in range(height):
            if i%3 == 0:
                li.append(Person(preferences=half_happy, race='white'))
            elif i%3 == 1:
                li.append(Person(preferences=half_happy, race='black'))
            elif i%3 == 2:
                li.append(None)
        ret.append(li)
    ret[0][0] = (Person(preferences=always_happy, race='black'))
    ret[0][1] = (Person(preferences=hates_blacks, race='white'))
    ret[7][7] = None
    return ret

def config_all_white_all_happy(width=8,height=8):
    always_happy = {'white' : (0,1), 'black' : (0,1)}
    ret = []
    for i in range(width):
        li = []
        for j in range(height):
            li.append(Person(preferences=always_happy, race='white'))
        ret.append(li)
    return ret

def config_all_black_all_happy(width=8,height=8):
    always_happy = {'white' : (0,1), 'black' : (0,1)}
    ret = []
    for i in range(width):
        li = []
        for j in range(height):
            li.append(Person(preferences=always_happy, race='black'))
        ret.append(li)
    return ret

def config_random(width=8,height=8):
    # approximately fills with 1/3 people
    v = 5
    ret = []
    for i in range(width):
        li = []
        for j in range(height):
            r = random.randint(1,3)
            if r == 1:
                rs = sorted([random.random() for _ in range(2)])
                prefs = {'white' : (0,rs[1]), 'black' : (0,rs[0])}
                li.append(Person(preferences=prefs, race='white',vision=v))
            elif r == 2:
                rs = sorted([random.random() for _ in range(2)])
                prefs = {'black' : (0,rs[1]), 'white' : (0,rs[0])}
                li.append(Person(preferences=prefs, race='black',vision=v))
            else:
                li.append(None)
        ret.append(li)
    return ret

def config_random2(width=8,height=8):
    # approximately fills with 1/3 people
    ret = []
    for i in range(width):
        li = []
        for j in range(height):
            r = random.randint(1,3)
            if r == 1:
                rs = sorted([random.random() for _ in range(4)])
                prefs = {'white' : (rs[1],rs[3]), 'black' : (rs[0],rs[2])}
                li.append(Person(preferences=prefs, race='white'))
            elif r == 2:
                rs = sorted([random.random() for _ in range(4)])
                prefs = {'black' : (rs[1],rs[3]), 'white' : (rs[0],rs[2])}
                li.append(Person(preferences=prefs, race='black'))
            else:
                li.append(None)
        ret.append(li)
    return ret

def config_fav(width=8,height=8):
    # approximately fills with 1/3 people
    v = 2
    rs = [.2,.8,.2,.8]
    # rs = [0,1,0,1]
    ret = []
    for i in range(width):
        li = []
        for j in range(height):
            r = random.randint(1,3)
            if r == 1:
                prefs = {'white' : (rs[0],rs[1]), 'black' : (rs[2],rs[3])}
                li.append(Person(preferences=prefs, race='white',vision=v))
            elif r == 2:
                prefs = {'white' : (rs[0],rs[1]), 'black' : (rs[2],rs[3])}
                li.append(Person(preferences=prefs, race='black',vision=v))
            else:
                li.append(None)
        ret.append(li)
    return ret


