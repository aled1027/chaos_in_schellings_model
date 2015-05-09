from ca import SchellingCA, Person
import copy
import csv
import logging
import random

def c_random(width, height, low, high):
    ret = []
    for i in range(width):
        li = []
        for j in range(height):
            r = random.randint(1,3)
            if r == 1:
                li.append(Person(nbr_like_pref=low, race='black', pk=i+j))
            elif r == 2:
                li.append(Person(nbr_like_pref=high, race='white', pk=i+j))
            else:
                li.append(None)
        ret.append(li)
    return ret

if __name__=='__main__':
    logging.basicConfig(filename='schelling.log', level=logging.INFO, format='%(levelname)-8s %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info('starting')

    # INPUTS
    num_trials = 15
    num_iterations = 50
    width = 8
    height = 8
    low = .3
    high = [.3, .4, .5, .6, .7]

    for h in high:
        with open('data/nearest_data_%f_%f.csv' % (low,h), 'w') as nearest_csvfile:
            with open('data/rw_data_%f_%f.csv' % (low,h), 'w') as rw_csvfile:

                nearest_csvwriter = csv.writer(nearest_csvfile, delimiter=',')
                rw_csvwriter = csv.writer(rw_csvfile, delimiter=',')


                # make header for csv file
                l = ['trial_number']
                k = []
                for i in range(num_iterations+1):
                    l.append('sim_iter_%d' % i)
                    k.append('hap_iter_%d' % i)
                nearest_csvwriter.writerow(l + k)
                rw_csvwriter.writerow(l + k)

                # run the simulation
                for i in range(num_trials):
                    logging.info('starting trial %d' % i)
                    a = c_random(width, height, low, h)
                    b = copy.deepcopy(a)

                    s = SchellingCA(width=width, height=height, state=a, mode='nearest')
                    s_avg_hap = [s.avg_happiness]

                    t = SchellingCA(width=width, height=height, state=b, mode='rw')
                    s_avg_sim = [i, s.avg_similarity]
                    t_avg_sim = [i, t.avg_similarity]
                    t_avg_hap = [t.avg_happiness]

                    for j in range(num_iterations):
                        s.iterate()
                        s_avg_sim.append(s.avg_similarity)
                        s_avg_hap.append(s.avg_happiness)

                        t.iterate()
                        t_avg_sim.append(s.avg_similarity)
                        t_avg_hap.append(s.avg_happiness)

                    nearest_csvwriter.writerow(s_avg_sim + s_avg_hap)
                    rw_csvwriter.writerow(s_avg_sim + s_avg_hap)

    logging.info('finishing')

