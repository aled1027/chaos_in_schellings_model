from ca import SchellingCA, Person
import copy
import logging
import random


def c(width, height):
    # Board is empty except for
        # white person at [2][2]
        # 3 black people at [0][0], [0][1], [1][0]
    ret = []
    for i in range(width):
        li = []
        for j in range(height):
            li.append(None)
        ret.append(li)

    pref1 = 0.3
    pref2 = 0.5

    ret[0][0] = (Person(nbr_like_pref=pref1, race='black', pk=0))
    ret[1][1] = (Person(nbr_like_pref=pref1, race='black', pk=1))
    ret[2][0] = (Person(nbr_like_pref=pref1, race='black', pk=2))
    ret[3][1] = (Person(nbr_like_pref=pref1, race='black', pk=3))

    ret[0][1] = (Person(nbr_like_pref=pref2, race='white', pk=4))
    ret[1][0] = (Person(nbr_like_pref=pref2, race='white', pk=5))
    ret[2][1] = (Person(nbr_like_pref=pref2, race='white', pk=6))
    ret[3][0] = (Person(nbr_like_pref=pref2, race='white', pk=7))
    return ret

def c_random(width, height):
    pref1 = 0.3
    pref2 = 0.5

    ret = []
    for i in range(width):
        li = []
        for j in range(height):
            r = random.randint(1,3)
            if r == 1:
                li.append(Person(nbr_like_pref=pref1, race='black', pk=i+j))
            elif r == 2:
                li.append(Person(nbr_like_pref=pref2, race='white', pk=i+j))
            else:
                li.append(None)
        ret.append(li)
    return ret



if __name__=='__main__':
    logging.basicConfig(filename='schelling.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info('starting orig')
    a = c_random(4,4)
    b = copy.deepcopy(a)

    s = SchellingCA(width=4, height=4, state=a, mode='nearest')
    t = SchellingCA(width=4, height=4, state=b, mode='rw')

    print(s)
    for i in range(5):
        s.iterate()
        print(s)
        #print(s.print_races())
        #print('')
    logging.info('finishing orig')

    #print('---------------------------')
    #print(t)
    #for i in range(15):
    #    t.iterate()
    #    print(t)





