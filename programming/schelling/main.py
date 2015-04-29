import logging
import csv
from ca import SchellingCA, Person
from configs import *

def config_fav(width=8,height=8, prefs=None):
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

def theloop():
    with open('data.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        num_iterations = 40
        num_trials_per_pref = 40
        preferences = [[a,.8,.3,.8] for a in [.1,.2,.3,.4,.5,.6,.7,.8]]

        print('preferences narrow')
        print('i', 'avg_happiness', 'avg_similarity')
        unique_identifier = 0
        for p in preferences:
            for _ in range(num_trials_per_pref):
                s = SchellingCA(width=8, height=8, state=config_fav(prefs = p))
                for i in range(num_iterations):
                    s.iterate()
                    unique_identifier += 1
                    for index,cell in enumerate(s):
                        if cell is not None:
                            csvwriter.writerow([unique_identifier,i,cell.pk, cell.race])

                    # write to row: [pref[0], pref[1], pref[2], pref[3]]
                    # for each person:
                    # write to row: [unique_identifier, i, person id, race, preferences, happy at end?, initial position, position after n trials, distance traveled, num times moved]


                    # print(s.avg_happiness, s.avg_similarity)


def main():
    theloop()



if  __name__ == '__main__':
    logging.basicConfig(filename='schelling.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info('starting')
    main()
    logging.info('finishing')


# t = SchellingCA(width=8,height=8, state=config_all_white_all_happy())
# u = SchellingCA(width=8,height=8, state=config_all_black_all_happy())
# v = SchellingCA(width=8,height=8, state=config_mixed())
# w = SchellingCA(width=8,height=8, state=config_random())
# y = SchellingCA(width=8,height=8, state=config_fav())


"""
def loop():
    # approx 5-10 seconds

    width = 8
    height = 8
    state = [[None]*width]*height
    small = 30
    big = 60
    for v in [1,2,5,10]:
        for p1 in range(10,big,10):
            for p2 in range(p1,big,10):
                for p3 in range(small,big,10):
                    for p4 in range(p3,big,10):
                        for q1 in range(small,big,10):
                            for q2 in range(q1,big,10):
                                for q3 in range(small,big,10):
                                    for q4 in range(q3,100,10):
                                        for _ratio in range(0,10,1):
                                            print(v)
                                            white_prefs = {'white': (p1,p2), 'black': (p3,p4)}
                                            pers =  Person(preferences=white_prefs,race='white',vision=v)
                                            s = SchellingCA(width=8,height=8, state=config_fav())

def main():
    #s = SchellingCA(width=8,height=8, state=config_fav())


    for v1 in range(1,11):

        # number of loops: 10 *10^4 * 10^4 * 10
        print(v1)
        for v2 in range(1,11):
            for p1 in range(0,100,10):
                for p2 in range(p1,100,10):
                    for p3 in range(0,100,10):
                        for p4 in range(p3,100,10):
                            for q1 in range(0,100,10):
                                for q2 in range(q1,100,10):
                                    for q3 in range(0,100,10):
                                        for q4 in range(q3,100,10):
                                            for _ratio in range(0,10,1):
                                                ratio = float(_ratio)/float(10)
                                                print(v1)
                                                # also loop over ratio of agents
                                                white_prefs = {'white': (p1,p2), 'black': (p3,p4)}
                                                black_prefs = {'white': (q1,q2), 'black': (q3,q4)}
                                                positions = [(x,y) for x in range(width) for y in range(height)]
                                                num_agents = ratio*width*height
                                                while num_agents > 0:
                                                    r = random.randint(0,len(positions)-1)
                                                    p = positions[r]
                                                    if state[p[0]][p[1]] is None:
                                                        num_agents -= 1
                                                        r2 = random.randint(0,1)
                                                        if r2 == 0:
                                                            pers =  Person(preferences=white_prefs,race='white',vision=v1)
                                                            state[p[0]][p[1]] = pers
                                                        else:
                                                            pers =  Person(preferences=black_prefs,race='black',vision=v2)
                                                            state[p[0]][p[1]] = pers

"""


