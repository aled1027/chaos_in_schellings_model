import logging
from ca import SchellingCA, Person
from configs import *

def main():
    s = SchellingCA(width=8,height=8, state=config_fav())
    print('i', 'avg_happiness', 'avg_similarity')
    for i in range(10):
        s.iterate()
        print(i, s.avg_happiness, s.avg_similarity)
    s.print_happiness()


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


