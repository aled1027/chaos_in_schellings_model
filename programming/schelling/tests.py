from ca import SchellingCA, Person
import logging
import random

def config(width=8,height=8, prefs=None):

    # approximately fills with 1/3 people
    v = 2
    prefs = prefs if prefs else [.3,.8,.3,.8]
    ret = []
    for i in range(width):
        li = []
        for j in range(height):
            r = random.randint(1,3)
            if r == 1:
                pref = {'white' : (prefs[0],prefs[1]), 'black' : (prefs[2],prefs[3])}
                li.append(Person(preferences=pref, race='white',vision=v, pk=i+j))
            elif r == 2:
                pref = {'white' : (prefs[0],prefs[1]), 'black' : (prefs[2],prefs[3])}
                li.append(Person(preferences=pref, race='black',vision=v, pk=i+j))
            else:
                li.append(None)
        ret.append(li)
    return ret

def test_random_walk():
    print('running test_random_walk')

    def c(width=8,height=8, prefs=None):
        # Board is empty except for
            # white person at [2][2]
            # 3 black people at [0][0], [0][1], [1][0]
        ret = []
        for i in range(width):
            li = []
            for j in range(height):
                                li.append(None)
            ret.append(li)
        pref1 = {'white' : (.0,1), 'black' : (.5,1)}
        pref2 = {'white' : (.0,1), 'black' : (.5,1)}
        ret[2][2] = (Person(preferences=pref1, race='white',vision=1, pk=0))
        ret[0][0] = (Person(preferences=pref2, race='black',vision=1, pk=1))
        ret[1][0] = (Person(preferences=pref2, race='black',vision=1, pk=2))
        ret[0][1] = (Person(preferences=pref2, race='black',vision=1, pk=3))
        return ret

    s = SchellingCA(width=8, height=8, state=c())
    print(s)
    s.print_happiness()
    print()
    s.print_races()
    s.iterate()
    print()
    print(s)
    s.print_happiness()
    print()
    s.print_races()

    # TODO CHECK GET_DELTAS


    print('ending test_random_walk')

def test1():
    print('running test1')
    s = SchellingCA(width=8, height=8, state=config(prefs = None))
    print(s)
    s.print_happiness()
    print()
    s.print_races()
    s.iterate()

    print()
    s.print_happiness()
    print()
    s.print_races()
    print(s)

    print('finishing test1')


if  __name__ == '__main__':
    logging.basicConfig(filename='schelling.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info('starting testing')
    test_random_walk()
    #test1()
    logging.info('finishing testing')



