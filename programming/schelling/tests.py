from ca import SchellingCA, Person
import logging
import random

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
    pref1 = 0.5
    pref2 = 0.0
    ret[2][2] = (Person(nbr_like_pref=pref1, race='white', pk=0))
    ret[0][0] = (Person(nbr_like_pref=pref2, race='black', pk=1))
    ret[1][0] = (Person(nbr_like_pref=pref2, race='white', pk=2))
    ret[0][1] = (Person(nbr_like_pref=pref2, race='black', pk=3))
    return ret

def config(width=8,height=8, prefs=None):

    # approximately fills with 1/3 people
    v = 2
    ret = []
    pref = .5
    for i in range(width):
        li = []
        for j in range(height):
            r = random.randint(1,3)
            if r == 1:
                li.append(Person(nbr_like_pref=pref, race='white', pk=i+j))
            elif r == 2:
                li.append(Person(nbr_like_pref=pref, race='black', pk=i+j))
            else:
                li.append(None)
        ret.append(li)
    return ret

def test_random_walk():
    print('running test_random_walk')


    s = SchellingCA(width=8, height=8, state=c())
    print(s)
    s.print_happiness()
    print()
    #s.print_races()
    s.iterate()
    print()
    print(s)
    s.print_happiness()
    print()
    #s.print_races()

    # TODO CHECK GET_DELTAS


    print('ending test_random_walk')

def test1():
    print('running test1')
    #s = SchellingCA(width=8, height=8, state=config(prefs = None), mode='nearest')
    s = SchellingCA(width=8, height=8, state=c(), mode='nearest')
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



def simpletest():
    print('running simpletest')
    s = SchellingCA(width=8, height=8, state=c(), mode='nearest')
    print(s)
    s.print_happiness()
    print()
    s.print_races()
    print('finishing simpletest')




# if  __name__ == '__main__':
#     logging.basicConfig(filename='schelling.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#     logging.info('starting testing')
#
#     #simpletest()
#     #test_random_walk()
#     test1()
#     logging.info('finishing testing')


print('running test1')
#s = SchellingCA(width=8, height=8, state=config(prefs = None), mode='nearest')
s = SchellingCA(width=8, height=8, state=c(), mode='nearest')
s.print_happiness()
print()
s.print_races()
