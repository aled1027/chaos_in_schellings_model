from ca import SchellingCA, Person
import copy
import csv
import logging
import random

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
    logging.info('starting')

    with open('nearest_neighbor_data.csv', 'w') as nearest_csvfile:
        with open('rw_data.csv', 'w') as rw_csvfile:

            nearest_csvwriter = csv.writer(nearest_csvfile, delimiter=',')
            #rw_csvwriter = csv.writer(rw_csvfile, delimiter=',')

            #rw_csvwriter.writerow([1,2,3])

            # INPUTS
            num_trials = 10
            num_iterations = 50
            width = 8
            height = 8

            # make header for csv file
            l = ['trial_number']
            k = []
            for i in range(num_iterations+1):
                l.append('sim_iter_%d' % i)
                k.append('hap_iter_%d' % i)
            nearest_csvwriter.writerow(l + k)

            # run the simulation
            for i in range(num_trials):
                a = c_random(width, height)
                b = copy.deepcopy(a)

                s = SchellingCA(width=width, height=height, state=a, mode='nearest')
                t = SchellingCA(width=width, height=height, state=b, mode='rw')

                s_avg_sim = [i, s.avg_similarity]
                s_avg_hap = [s.avg_happiness]

                for j in range(num_iterations):
                    s.iterate()
                    s_avg_sim.append(s.avg_similarity)
                    s_avg_hap.append(s.avg_happiness)

                nearest_csvwriter.writerow(s_avg_sim + s_avg_hap)

    logging.info('finishing')

