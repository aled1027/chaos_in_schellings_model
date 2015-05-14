import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# .stack() also useful

def save_subplots():
    # note, may also need to change title.
    file_names = ['3.csv', '5.csv', '10.csv', '15.csv', '20.csv', '30.csv', '50.csv', '75.csv', '100.csv']
    params = [3,5,10,15,20,30,50,75,100]
    directory = 'data/stay_at_end_rw/rw_max_data_change_black'

    coords = [(0,i) for i in range(3)] + [(1,i) for i in range(3)] + [(2,i) for i in range(3)]

    fig, axes = plt.subplots(nrows=3, ncols=3, sharex=True, sharey=True)
    fig.tight_layout()

    first = True
    for max_walk_dist, file_name, coord in zip(params, file_names, coords):
        print(file_name, max_walk_dist)
        # import data and get the dataframes so we can work with them
        df = pd.read_csv(directory + '/' + file_name)
        sim_cols = ['sim_iter_%d' % i for i in range(50)]
        hap_cols = ['hap_iter_%d' % i for i in range(50)]

        sim_df = df[sim_cols]
        hap_df = df[hap_cols]

        # compute mean and standard deviation
        sim_means_df = pd.DataFrame(sim_df.mean(),columns=['sim_mean'])
        sim_std_df = pd.DataFrame(sim_df.std(),columns=['sim_std'])

        hap_means_df = pd.DataFrame(hap_df.mean(),columns=['hap_mean'])
        hap_std_df = pd.DataFrame(hap_df.std(),columns=['hap_std'])

        sim_means_df    = sim_means_df.set_index([range(50)])
        sim_std_df      = sim_std_df.set_index([range(50)])
        hap_means_df    = hap_means_df.set_index([range(50)])
        hap_std_df      = hap_std_df.set_index([range(50)])

        # combine the means and std dataframes
        all_df = sim_means_df.join(sim_std_df).join(hap_means_df).join(hap_std_df)
        all_df = all_df.set_index([range(50)])

        # plot 'em
        # matplot subplot
        # MAY NEED TO CHANGE TITEL WHEN RUNNING
        p = all_df.plot(title='Max Black Steps = %d' % max_walk_dist, ax=axes[coord[0], coord[1]])
        p.axis([0,50,0,1])
        p.legend().set_visible(False)

    plt.suptitle('Max White Steps = 10, Prefs = (Bl=0.3, Wh=0.5), Stay at end of RW', size=14)
    plt.subplots_adjust(top=0.85)
    plt.savefig(directory + '/images/graph.png')

save_subplots()
