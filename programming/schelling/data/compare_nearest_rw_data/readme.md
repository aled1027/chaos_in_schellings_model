The code for producing the data:

def compare_nearest_rw():
    _dict = {}
    _dict['num_trials'] = 50
    _dict['num_iterations'] = 50
    _dict['width'] = 8
    _dict['height'] = 8
    _dict['black_pref'] = 0.3
    _dict['white_pref'] = 0.3
    _dict['black_max_walk'] = 10
    _dict['white_max_walk'] = 10
    _dict['dir'] = 'data/compare_nearest_rw_data'
    _dict['param_list'] = []
    _dict['stay_at_end_rw'] = False
    _dict['mode'] = ''
    _dict['num_probs'] = 4

    white_pref_list = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

    for white_pref in white_pref_list:
        with open(_dict['dir'] + '/rw_%f.csv' % white_pref, 'w') as ne_csvfile:
            with open(_dict['dir'] + '/nearest_%f.csv' % white_pref, 'w') as rw_csvfile:
                ne_csvwriter = csv.writer(ne_csvfile, delimiter=',')
                rw_csvwriter = csv.writer(rw_csvfile, delimiter=',')

                # make header for csv file
                l = ['trial_number']
                k = []
                for i in range(_dict['num_iterations']+1):
                     l.append('sim_iter_%d' % i)
                     k.append('hap_iter_%d' % i)
                ne_csvwriter.writerow(l + k)
                rw_csvwriter.writerow(l + k)

                # run the simulation
                for i in range(_dict['num_trials']):
                    logging.info('starting trial %d' % i)
                    a = c_random(_dict['width'], _dict['height'], _dict['black_pref'], white_pref,  _dict['black_max_walk'], _dict['white_max_walk'], _dict['num_probs'])
                    b = copy.deepcopy(a)

                    ne = SchellingCA(width=_dict['width'], height=_dict['height'], state=a, mode='nearest')
                    rw = SchellingCA(width=_dict['width'], height=_dict['height'], state=b, mode='rw', stay_at_end_rw=_dict['stay_at_end_rw'])
                    ne_avg_sim = [i, ne.avg_similarity]
                    ne_avg_hap = [ne.avg_happiness]

                    rw_avg_sim = [i, rw.avg_similarity]
                    rw_avg_hap = [rw.avg_happiness]


                    for j in range(_dict['num_iterations']):
                        ne.iterate()
                        rw.iterate()

                        ne_avg_sim.append(ne.avg_similarity)
                        ne_avg_hap.append(ne.avg_happiness)
                        rw_avg_sim.append(rw.avg_similarity)
                        rw_avg_hap.append(rw.avg_happiness)

                    ne_csvwriter.writerow(ne_avg_sim + ne_avg_hap)
                    rw_csvwriter.writerow(rw_avg_sim + rw_avg_hap)



