import random


class SchellingCA:
    is_done = False
    amount_segregation = 0
    empty_positions = set()
    unhappy_positions = set()
    happy_positions = set()

    def __init__(self, width=8, height=8, races=['white','black'], state=None):
        self.width = width
        self.height = height
        self.races = races
        if state:
            self.state = state
        else:
            self.state = [[None]*self.width]*self.height
        self.update_states_and_sets()

    def get_avg_similarity(self):
        # calculates average similarity ratio
        similarity = []
        for i in range(self.width):
            for j in range(self.height):
                if self.state[i][j] != None:
                    nbr_races = [nbr.race for nbr in self.get_neighbors(i,j)]
                    nbr_dict = {r: nbr_races.count(r) for r in self.races}
                    cur_race = self.state[i][j].race
                    num_nbrs = sum(nbr_dict.values())

                    if num_nbrs  == 0:
                        similarilty.append(1)
                    else:
                        ratio = float( nbr_dict[cur_race] / num_nbrs )
                        similarity.append(ratio)
        average_similarity = sum(similarity)/len(similarity)
        return average_similarity

        """
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
        """

    def update_states_and_sets(self):
        """
        - updates the happiness of all persons on board
        - updates the three sets:
            - self.empty_positions
            - self.unhappy_positions
            - self.happy_positions
        """

        for i in range(self.width):
            for j in range(self.height):
                if self.state[i][j] == None:
                    self.empty_positions.add((i,j))
                else:
                    nbr_races = [nbr.race for nbr in self.get_neighbors(i,j)]
                    nbr_dict = {r: nbr_races.count(r) for r in self.races}
                    self.state[i][j].update_happiness(nbr_dict)

                    if (self.state[i][j].is_happy == True):
                        self.happy_positions.add((i,j))
                        self.unhappy_positions.discard((i,j))
                    else:
                        self.unhappy_positions.add((i,j))
                        self.happy_positions.discard((i,j))

    def move_someone(self):
        """
        move_someone(self)
        1. If we can, pick a random unhappy person.
        2. Move them to a new position such that they are happy
        3. Return True if we could find someone to move
        4. Return False if we could not find someone to move
        """
        if self.unhappy_positions:
            # 1. pick an unhappy person at random.
            old_x, old_y = mover_origin = self.unhappy_positions.pop()
            did_move_someone = False

            # 2. move them to a new position; such that they are happey
            print(self.empty_positions)
            while self.empty_positions:
                new_x,new_y = self.empty_positions.pop()
                nbr_races = [nbr.race for nbr in self.get_neighbors(new_x,new_y)]
                nbr_dict = {r: nbr_races.count(r) for r in self.races}
                b = self.state[old_x][old_y].update_happiness(nbr_dict)
                # would they be happy at (new_x,new_y)?
                if (self.state[old_x][old_y].update_happiness(nbr_dict) == True):
                    # then put 'em there
                    # is this swapping working?
                    print('moving from (%d,%d) to (%d,%d)' % (old_x,old_y,new_x,new_y))
                    self.state[old_x][old_y],self.state[new_x][new_y] =  self.state[new_x][new_y], self.state[old_x][old_y]
                    did_move_someone = True
                    break
        if did_move_someone is False:
            print('Did not move anyone')
        return did_move_someone

    def get_neighbors(self,i,j):
        if i < 0:
             raise RuntimeError("Width %d Lower than number of cells. " %i)
        elif i >= self.width:
             raise RuntimeError("Width %d Lower than number of cells. " %i)
        elif j < 0:
             raise RuntimeError("Height %d Higher than number of cells. " %i)
        elif j >= self.height:
             raise RuntimeError("Height %d Higher than number of cells. " %i)
        deltas = [(-1,0), (1,0), (0,-1), (0,1)]
        nbr_coords =  [(i+a, j+b) for (a,b) in deltas if (-1 < i+a < self.width) and (-1 < j+b < self.height)]
        return [self.state[x][y] for (x,y) in nbr_coords if self.state[x][y] is not None]

    def iterate(self):
        """
        goes through one iteration of schelling's process.
        1. Look at a list of unhappy persons. Pick one randomly.
        2. Move that person
        3. Update everyone else's happiness.
        This aspect could be made more efficient by only updating people within the vision origin and destination of moved person.
        """
        if (self.move_someone() == False):
            self.is_done = True
            return False
        self.update_states_and_sets()
        return True

    def print_happiness(self):
        string_list = []
        for row in self.state:
            string = ""
            for person in row:
                if person is None:
                    string = string + " " + "None"
                else:
                    string = string + " " + str(person.is_happy)
            string_list.append(string)

        for string in string_list:
            print(string)

    def print_races(self):
        string_list = []
        for row in self.state:
            string = ""
            for person in row:
                if person is None:
                    string = string + " " + "None "
                else:
                    string = string + " " + str(person.race)
            string_list.append(string)

        for string in string_list:
            print(string)

    def print_state(self):
        string_list = []
        for row in self.state:
            string = ""
            for person in row:
                if person is None:
                    string = string + " " + "None"
                else:
                    string = string + " " + person.strall
            string_list.append(string)

        for string in string_list:
            print(string)

class Person:
    # preferences of the form: {'white': (.2,.3)} indicates prefers more than 20% white neighbors, less than %30 white neighbors.
    def __init__(self, preferences={}, race='white', is_happy=False, races=['white','black']):
        self.race = race
        self.races = races
        self.is_happy = is_happy
        self.preferences = preferences


    def update_happiness(self,nbr_dict):
        num_nbrs = sum(nbr_dict.values())
        if num_nbrs == 0:
            return True
        for race in self.races:
            pct_race = nbr_dict[race] / num_nbrs
            lower_bound, upper_bound = self.preferences[race]

            if not (lower_bound <= pct_race <= upper_bound):
                # failed a condition. we are so unhappy
                self.is_happy = False
                return False

    def strall(self):
        return "(Race: "+self.race + ", is_happy:" + str(self.is_happy) + ", preferences:" + str(self.preferences) + ")"

    def strsmall(self):
        return self.race + " " + str(self.is_happy)

    def __str__(self):
        return self.strsmall()

    def __repr__(self):
        return str(self)

    def set_happiness(self,is_happy):
        self.is_happy = is_happy

def config1(width=8,height=8):
    always_happy = {'white' : (0,1), 'black' : (0,1)}
    never_happy = {'white' : (1,1), 'black' : (1,1)}
    half_happy = {'white' : (.25,.75), 'black' : (.25,.75)}
    hates_blacks = {'white' : (0,1), 'black' : (0,0)}
    ret = []
    for i in range(width):
        li = []
        for j in range(height):
            li.append(Person(preferences=always_happy, race='white'))
        ret.append(li)
    ret[0][0] = (Person(preferences=always_happy, race='black'))
    ret[0][1] = (Person(preferences=hates_blacks, race='white'))
    ret[7][7] = None
    return ret

def config_mixed(width=8,height=8):
    always_happy = {'white' : (0,1), 'black' : (0,1)}
    never_happy = {'white' : (1,1), 'black' : (1,1)}
    half_happy = {'white' : (.25,.75), 'black' : (.25,.75)}
    hates_blacks = {'white' : (0,1), 'black' : (0,0)}
    ret = []
    for i in range(width):
        li = []
        for j in range(height):
            if i%3 == 0:
                li.append(Person(preferences=half_happy, race='white'))
            elif i%3 == 1:
                li.append(Person(preferences=half_happy, race='black'))
            elif i%3 == 2:
                li.append(None)
        ret.append(li)
    ret[0][0] = (Person(preferences=always_happy, race='black'))
    ret[0][1] = (Person(preferences=hates_blacks, race='white'))
    ret[7][7] = None
    return ret


def config_all_white_all_happy(width=8,height=8):
    always_happy = {'white' : (0,1), 'black' : (0,1)}
    ret = []
    for i in range(width):
        li = []
        for j in range(height):
            li.append(Person(preferences=always_happy, race='white'))
        ret.append(li)
    return ret

def config_all_black_all_happy(width=8,height=8):
    always_happy = {'white' : (0,1), 'black' : (0,1)}
    ret = []
    for i in range(width):
        li = []
        for j in range(height):
            li.append(Person(preferences=always_happy, race='black'))
        ret.append(li)
    return ret

def config_random(num_people,width=8,height=8):
    ret = []
    for i in range(width):
        li = []
        for j in range(height):
            r = random.randint(1,3)
            if r == 1:
                rs = sorted([random.random() for _ in range(4)])
                prefs = {'white' : (r[2],r[4]), 'black' : (r[1],r[3])}
                li.append(Person(preferences=prefs, race='white'))
            elif r == 2:
                rs = sorted([random.random() for _ in range(4)])
                prefs = {'black' : (r[2],r[4]), 'white' : (r[1],r[3])}
                li.append(Person(preferences=prefs, race='black'))
            else:
                li.append(None)
        ret.append(li)
    return ret

s = SchellingCA(width=8,height=8, state=config1())
t = SchellingCA(width=8,height=8, state=config_all_white_all_happy())
u = SchellingCA(width=8,height=8, state=config_all_black_all_happy())
v = SchellingCA(width=8,height=8, state=config_mixed())
w = SchellingCA(width=8,height=8, state=config_random(int(64/3)))
