# other
:set foldnestmax=2

# todo schelling project
- add in none as a race
- if we are slow, only loop over the board once per iteration.
    - probably don't need to recalculate empty spaces every iteration. They change by 2 every iteration in veryt predictable way since one person moves. 
- add in needs a neighbor to be happy
- person who just wants their neighbors to be happy

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

# paper
The argument could be made that schelling's model doesn't model the migrations patterns of white and blacks in neighborhood because it neglects important pressures such as Imminent Domain, White Flight, changes in housing prices, parent's desire for good schools, closeness to work, and the list goes on. 

I claim that these criteria increase in the complexity of the model. We start with this model that captures some aspect of these relations, and we see that this model robustly exhibits chaos and segregation. 

Now, we add more contstaints to the model, and we check if this increases the chaos and segregation, or decreases it. 

I hypothesize that it will either increase the chaos and cause it to stay the same. 

The contrains that will be added will be less mathemetical - in the sense that they are less predicact, dependent on randomness and differences between individuals, so they should if anything produce strangeer behavior on the macro scale. 

That being said, there is the argument that in mass, large amounts of various influences can create a more orderly world. 

For example, say we have a neighborhood that has schelling's traditional rules exhibiting chaotic behavior. 

Then we consider the fact that these persons also work various jobs in various parts of the country, so they may not know the race of their neighbors. 

In order to add this into the model, we have the vision of a person be a random variable set at the time we intialize the model. 

Then perhaps the model will exhibit less chaotic behavior because most people won't have a large enough vision to notice the races surroudning them, and a few persons will move around a ton because they're vision is large enough to never satisfy their preferences. 


In this case we see that increasing the complexity of the model leads to more order.

This leads to large philospophical point that CA prove the enlighten: 
is the w
orld chaotic because the rules are random and chaotic? 
or is the world chaotic because of the rules synergize? 
or is the world chaotic because the rules are simple, but lead to complex, chaotic behavior, like class 3/4 of wolfram
or ...

If the world is chaotic, why is it chaotic?
















