import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# .stack() also useful

max_walk_dist_list = [3]
for max_walk_dist in max_walk_dist_list:
    # import data and get the dataframes so we can work with them
    df = pd.read_csv('../data/rw_max_data/rw_%d.csv' % max_walk_dist)
    sim_cols = ['sim_iter_%d' % i for i in range(50)]
    hap_cols = ['hap_iter_%d' % i for i in range(50)]
    sim_df = df[sim_cols]
    hap_df = df[hap_cols]

    # compute mean and standard deviation
    sim_means_df = pd.DataFrame(sim_df.mean(),columns=['mean'])
    sim_std_df = pd.DataFrame(sim_df.std(),columns=['std'])
    # combine the means and std dataframes
    both_means_df = sim_means_df.join(sim_std_df)
    both_means_df = both_means_df.set_index([range(50)])

    # plot it
    p = both_means_df.plot(title='Similarity for Max Walking Distance of %d (50 trials)' % max_walk_dist)
    plt.axis([0,50,0,1])
    p.set_xlabel('iteration')
    p.set_ylabel('ratio')
    plt.savefig('../data/rw_max_data/images/sim_rw_%d.png' % max_walk_dist)


