from ca import SchellingCA, Person
import copy
import csv
import logging
import random

def c_random(width, height, low, high, _max_walking_distance1, _max_walking_distance2):
    ret = []
    for i in range(width):
        li = []
        for j in range(height):
            r = random.randint(1,4)
            if r == 1:
                li.append(Person(nbr_like_pref=low, race='black', pk=i+j, max_walking_distance = _max_walking_distance1))
            elif r == 2:
                li.append(Person(nbr_like_pref=high, race='white', pk=i+j, max_walking_distance = _max_walking_distance2))
            else:
                li.append(None)
        ret.append(li)
    return ret

def different_max_walk_experiment():
    # INPUTS
    num_trials = 50
    num_iterations = 50
    width = 8
    height = 8
    low = 0.5
    h = 0.5

    max_walk_list = [(5,10), (5,15), (5,20), (5,50), (10,10), (10,15), (10,20), (10,50)]


    for max_walk1, max_walk2 in max_walk_list:
        with open('rw_max_data/nearest_data_%d.csv' % max_walk, 'w') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerow(['max_walking_distance', max_walk])

            # make header for csv file
            l = ['trial_number']
            k = []
            for i in range(num_iterations+1):
                l.append(i)
                k.append(i)
            csvwriter.writerow(l + k)

            # run the simulation
            for i in range(num_trials):
                logging.info('starting trial %d' % i)
                a = c_random(width, height, low, h, max_walk1, max_walk2)
                s = SchellingCA(width=width, height=height, state=a, mode='nearest')
                s_avg_sim = [i, s.avg_similarity]
                s_avg_hap = [s.avg_happiness]

                for j in range(num_iterations):
                    s.iterate()
                    s_avg_sim.append(s.avg_similarity)
                    s_avg_hap.append(s.avg_happiness)

                csvwriter.writerow(s_avg_sim + s_avg_hap)


def max_walk_experiment():
    # INPUTS
    num_trials = 50
    num_iterations = 50
    width = 8
    height = 8
    low  = 0.3
    high = 0.5

    black_max_walk_list = [3,5,10,15,20,30,50,75,100]
    white_max_walk = 10

    for black_max_walk in black_max_walk_list:
        with open('data/rw_mixed_walk_diff_prefs_data/rw_%d.csv' % black_max_walk, 'w') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            # make header for csv file
            l = ['trial_number']
            k = []
            for i in range(num_iterations+1):
                l.append('sim_iter_%d' % i)
                k.append('hap_iter_%d' % i)
            csvwriter.writerow(l + k)

            # run the simulation
            for i in range(num_trials):
                logging.info('starting trial %d' % i)
                a = c_random(width, height, low, high, black_max_walk, white_max_walk)
                s = SchellingCA(width=width, height=height, state=a, mode='rw')
                s_avg_sim = [i, s.avg_similarity]
                s_avg_hap = [s.avg_happiness]

                for j in range(num_iterations):
                    s.iterate()
                    s_avg_sim.append(s.avg_similarity)
                    s_avg_hap.append(s.avg_happiness)

                csvwriter.writerow(s_avg_sim + s_avg_hap)

if __name__=='__main__':
    logging.basicConfig(filename='schelling.log', level=logging.INFO, format='%(levelname)-8s %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info('starting')
    max_walk_experiment()
    logging.info('finishing')

