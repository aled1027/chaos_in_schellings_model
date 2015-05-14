# NEW
- TODO: DECOMPOSE HAPPINESS OF WHITE PEOPLE AND BLACK PEOPLE

- line misses discrete changes. try to use scatter plot instead of line plot
    - getting artifacts of matplotlib's plotting engine?



### OLLLLD
- 1.32s for 10 trials with 50 iterations

- individual amount of steps
    - no counter
- compare random walk to random jump
- TODO: fix init functions
- look up how to make python classes that have a ton of input variables

- each individual gets a certain about of steps that they can take.
- we can think of that number of steps as money/capital/influence anything that might someone explore more opportunities, ease one's way in the world.

# TODO
- if we are slow, only loop over the board once per iteration.
    - probably don't need to recalculate empty spaces every iteration. They change by 2 every iteration in veryt predictable way since one person moves. 


- https://www.coursera.org/course/modelthinking
    - has a list of books/sources at bottom that might be useful
- https://www.binpress.com/tutorial/introduction-to-agentbased-models-an-implementation-of-schelling-model-in-python/144
    - moves person to empty spot without regard to whether they are happy there.


        similarity_threshold_ratio = {}
        for i in [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]:
            schelling = Schelling(50, 50, 0.3, i, 500, 2)
            schelling.populate()
            schelling.update()
            similarity_threshold_ratio[i] = schelling.calculate_similarity()
        
        fig, ax = plt.subplots()
        plt.plot(similarity_threshold_ratio.keys(), similarity_threshold_ratio.values(), 'ro')
        ax.set_title('Similarity Threshold vs. Mean Similarity Ratio', fontsize=15, fontweight='bold')
        ax.set_xlim([0, 1])
        ax.set_ylim([0, 1.1])
        ax.set_xlabel("Similarity Threshold")
        ax.set_ylabel("Mean Similarity Ratio")
        plt.savefig('schelling_segregation_measure.png')

                
            

-

# other
:set foldnestmax=2


# my model
- random walk
    - can walk explore 'through' other people. 
    - can't live in same place as other people
    - explores until happy or doesn't find a place
