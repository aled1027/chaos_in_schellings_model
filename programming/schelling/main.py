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
    #with open('data.csv', 'w', newline='') as csvfile:
    with open('data.csv', 'w') as csvfile:
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
    print('starting')
    theloop()
    print('ending')



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



