import random

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


class SchellingCA:
    is_done = False
    amount_segregation = 0
    empty_positions = set()
    unhappy_positions = set()
    happy_positions = set()

    def __init__(self, width=8, height=8, races=['white','black']):
        self.width = width
        self.height = height
        self.races = races

        self.state = config1()

        self.update_states_and_sets()

    def update_states_and_sets(self):
        print('updating')
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
        # checks if set is empty


        if self.unhappy_positions:
            # 1. pick an unhappy person at random.
            old_x, old_y = mover_origin = self.unhappy_positions.pop()

            # 2. move them to a new position; such that they are happey
            print(self.empty_positions)
            while self.empty_positions:
                new_x,new_y = self.empty_positions.pop()
                print(new_x, new_y)
                nbr_races = [nbr.race for nbr in self.get_neighbors(new_x,new_y)]
                nbr_dict = {r: nbr_races.count(r) for r in self.races}
                print(nbr_dict)
                b = self.state[old_x][old_y].update_happiness(nbr_dict)
                print("b is",b)
                # would they be happy at (new_x,new_y)?
                if (self.state[old_x][old_y].update_happiness(nbr_dict) == True):
                    # then put 'em there
                    # is this swapping working?
                    print('swapping')
                    self.state[old_x][old_y],self.state[new_x][new_y] =  self.state[new_x][new_y], self.state[old_x][old_y]
                    break
        else:
            return False
        return True



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

        # move someone
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
    # prefernces of the form: {'white': (.2,.3)} indicates prefers more than 20% white neighbors, less than %30 white neighbors.

    def __init__(self, preferences={}, race='white', is_happy=False, races=['white','black']):
        self.race = race
        self.races = races
        self.is_happy = is_happy
        self.preferences = preferences

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

        # passed all of the conditions, so we are happy.
        self.is_happy = True
        return True




s = SchellingCA(width=8,height=8)



