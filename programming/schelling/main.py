class SchellingCA:
    is_done = False
    amount_segregation = 0

    def __init__(self, width=8, height=8, races=['white','black']):
        self.width = width
        self.height = height
        self.races = races

        preferences = {'white' : (0,1), 'black' : (0,1)}

        self.state = []
        for i in range(self.width):
            li = []
            for j in range(self.height):
                li.append(Person(preferences=preferences))
            self.state.append(li)

    def move_someone(self):
        # find someone with who is unhappy.
        self.updatePeoplesStates()
        canMoveSomeone = True
        return canMoveSomeone

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
        return [self.state[x][y] for (x,y) in nbr_coords]

    def iterate(self):
        # move someone

        # now update everyone's happiness
        for i in range(self.width):
            for j in range(self.height):
                nbr_races = [nbr.race for nbr in self.get_neighbors(i,j)]
                nbr_dict = {r: nbr_races.count(r) for r in self.races}
                self.state[i][j].update_happiness(nbr_dict)

    #def run(self, max_iterations=10):
        #for k in range(max_iterations):
    # def get_amount_segregation(self):


    def print_happiness(self):
        string_list = []
        for row in self.state:
            string = ""
            for person in row:
                string = string + " " + str(person.is_happy)
            string_list.append(string)

        for string in string_list:
            print string


    def print_races(self):
        string_list = []
        for row in self.state:
            string = ""
            for person in row:
                string = string + " " + str(person.race)
            string_list.append(string)

        for string in string_list:
            print string

    def print_state(self):
        string_list = []
        for row in self.state:
            string = ""
            for person in row:
                string = string + " " + str(person)
            string_list.append(string)

        for string in string_list:
            print string

class Person:
    # prefernces of the form: {'white': (.2,.3)} indicates prefers more than 20% white neighbors, less than %30 white neighbors.

    def __init__(self, preferences, race='white', is_happy=False, races=['white','black']):
        self.race = race
        self.races = races
        self.is_happy = is_happy
        self.preferences = preferences

    def __str__(self):
        return "(Race: "+self.race + ", is_happy:" + str(self.is_happy) + ", preferences:" + str(self.preferences) + ")"
    def __repr__(self):
        return str(self)

    def set_happiness(self,is_happy):
        self.is_happy = is_happy

    def update_happiness(self,nbr_dict):
        num_nbrs = sum(nbr_dict.values())

        for race in self.races:
            pct_race = nbr_dict[race] / num_nbrs
            lower_bound, upper_bound = self.preferences[race]

            if lower_bound <= pct_race <= upper_bound:
                pass
            else:
                # failed a condition. we are so unhappy
                self.is_happy = False
                return False

        # passed all of the conditions, so we are happy.
        self.is_happy = True
        return True




s = SchellingCA(width=8,height=8)



