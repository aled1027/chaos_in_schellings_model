import random


class SchellingCA:
    is_done = False
    amount_segregation = 0
    empty_positions = set()
    unhappy_positions = set()
    happy_positions = set()

    def __init__(self, width=8, height=8, races=None, state=None):
        self.races = races if races else ['white','black']
        self.state = state if state else [[None]*self.width]*self.height
        self.width = width
        self.height = height
        self.update_states_and_sets()

    def __repr__(self):
        return "%d by %d; agents: %d; agents unhappy: %d; avg happiness: %d; avg similiarity: %d" \
                % (self.width, self.height, len(self.unhappy_positions) + len(self.happy_positions), \
                    len(self.unhappy_positions), self.avg_happiness, self.avg_similarity)

    def __len__(self):
        return self.width * self.height

    def __getitem__(self, index):
        # treat index as moving across rows first, and then columns
        # i.e index = width_index + self.height*height_index
        if index >= len(self):
            raise IndexError

        width_index = index % self.height
        height_index = (index - width_index) / self.height
        return self.state[width_index][height_index]

    def test(self):
        for i,j in enumerate(self):
            print i,j

    @property
    def avg_similarity(self):
        # calculates average similarity ratio
        similarity = []
        for index,cell in enumerate(self):
            i = index % self.height
            j = (index - i) / self.height
            if cell != None:
                nbr_races = [nbr.race for nbr in self.get_neighbors(i, j, cell.vision)]
                nbr_dict = {race: nbr_races.count(race) for race in self.races}
                cur_race = cell.race
                num_nbrs = sum(nbr_dict.values())

                if num_nbrs  == 0:
                    similarity.append(1)
                else:
                    ratio = float(nbr_dict[cur_race]) / float(num_nbrs )
                    similarity.append(ratio)
        average_similarity = float(sum(similarity))/float(len(similarity))
        return average_similarity

    @property
    def avg_happiness(self):
        num_person = 0
        happy_counter = 0
        for cell in self:
            if cell != None:
                num_person += 1
                if cell.is_happy == True:
                    happy_counter += 1
        return float(happy_counter) / float(num_person)

    def update_states_and_sets(self):
        """
        - updates the happiness of all persons on board
        - updates the three sets:
            - self.empty_positions
            - self.unhappy_positions
            - self.happy_positions
        """
        for index,cell in enumerate(self):
            i = index % self.height
            j = (index - i) / self.height
            if cell == None:
                self.empty_positions.add((i,j))
            else:
                nbr_races = [nbr.race for nbr in self.get_neighbors(i, j, cell.vision)]
                nbr_dict = {race: nbr_races.count(race) for race in self.races}
                cell.update_happiness(nbr_dict)

                if (cell.is_happy == True):
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
            old_x, old_y = self.unhappy_positions.pop()
            did_move_someone = False

            # 2. move them to a new position; such that they are happey
            print(self.empty_positions)
            while self.empty_positions:
                new_x,new_y = self.empty_positions.pop()
                nbr_races = [nbr.race for nbr in self.get_neighbors(new_x,new_y,self.state[old_x][old_y].vision)]
                nbr_dict = {r: nbr_races.count(r) for r in self.races}
                b = self.state[old_x][old_y].update_happiness(nbr_dict)

                # would they be happy at (new_x,new_y)?
                if (self.state[old_x][old_y].update_happiness(nbr_dict) == True):
                    print('moving from (%d,%d) to (%d,%d)' % (old_x,old_y,new_x,new_y))
                    self.state[old_x][old_y],self.state[new_x][new_y] =  self.state[new_x][new_y], self.state[old_x][old_y]
                    did_move_someone = True
                    break

        if did_move_someone is False:
            print('Did not move anyone')
        return did_move_someone

    def get_neighbors(self,i,j,vision=1):
        if i < 0:
             raise RuntimeError("Width %d Lower than number of cells. " %i)
        elif i >= self.width:
             raise RuntimeError("Width %d Lower than number of cells. " %i)
        elif j < 0:
             raise RuntimeError("Height %d Higher than number of cells. " %i)
        elif j >= self.height:
             raise RuntimeError("Height %d Higher than number of cells. " %i)

        v = vision
        deltas = [(a,b) for a in range(-1*v,v+1) for b in range(-1*v,v+1) if abs(a)+abs(b) <= v and (a,b) != (0,0)]
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
    # vision measured in manhattan distance.
    def __init__(self, preferences=None, race='white', is_happy=False, races=None, vision=1):
        self.races = races if races else ['white','black']
        self.preferences = preferences if preferences else {}
        self.race = race
        self.is_happy = is_happy
        self.preferences = preferences
        self.vision = vision

    def update_happiness(self,nbr_dict):
        num_neighbors = sum(nbr_dict.values())

        if num_neighbors == 0:
            return True

        for race in self.races:
            pct_race = float(nbr_dict[race]) / float(num_neighbors)
            lower_bound, upper_bound = self.preferences[race]
            if not (lower_bound <= pct_race <= upper_bound):
                # failed a condition. we are so unhappy
                self.is_happy = False
                return False

        self.is_happy = True
        return True


    def strall(self):
        return "(Race: "+self.race + ", is_happy:" + str(self.is_happy) + ", preferences:" + str(self.preferences) + ")"

    def strsmall(self):
        return self.race + " " + str(self.is_happy)

    def __str__(self):
        return self.strsmall()

    def __repr__(self):
        return str(self)

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

def config_random(width=8,height=8):
    # approximately fills with 1/3 people
    v = 5
    ret = []
    for i in range(width):
        li = []
        for j in range(height):
            r = random.randint(1,3)
            if r == 1:
                rs = sorted([random.random() for _ in range(2)])
                prefs = {'white' : (0,rs[1]), 'black' : (0,rs[0])}
                li.append(Person(preferences=prefs, race='white',vision=v))
            elif r == 2:
                rs = sorted([random.random() for _ in range(2)])
                prefs = {'black' : (0,rs[1]), 'white' : (0,rs[0])}
                li.append(Person(preferences=prefs, race='black',vision=v))
            else:
                li.append(None)
        ret.append(li)
    return ret

def config_random2(width=8,height=8):
    # approximately fills with 1/3 people
    ret = []
    for i in range(width):
        li = []
        for j in range(height):
            r = random.randint(1,3)
            if r == 1:
                rs = sorted([random.random() for _ in range(4)])
                prefs = {'white' : (rs[1],rs[3]), 'black' : (rs[0],rs[2])}
                li.append(Person(preferences=prefs, race='white'))
            elif r == 2:
                rs = sorted([random.random() for _ in range(4)])
                prefs = {'black' : (rs[1],rs[3]), 'white' : (rs[0],rs[2])}
                li.append(Person(preferences=prefs, race='black'))
            else:
                li.append(None)
        ret.append(li)
    return ret

def config_fav(width=8,height=8):
    # approximately fills with 1/3 people
    v = 2
    rs = [.2,.8,.2,.8]
    ret = []
    for i in range(width):
        li = []
        for j in range(height):
            r = random.randint(1,3)
            if r == 1:
                prefs = {'white' : (rs[0],rs[1]), 'black' : (rs[2],rs[3])}
                li.append(Person(preferences=prefs, race='white',vision=v))
            elif r == 2:
                prefs = {'white' : (rs[0],rs[1]), 'black' : (rs[2],rs[3])}
                li.append(Person(preferences=prefs, race='black',vision=v))
            else:
                li.append(None)
        ret.append(li)
    return ret

# s = SchellingCA(width=8,height=8, state=config1())
# t = SchellingCA(width=8,height=8, state=config_all_white_all_happy())
# u = SchellingCA(width=8,height=8, state=config_all_black_all_happy())
# v = SchellingCA(width=8,height=8, state=config_mixed())
# w = SchellingCA(width=8,height=8, state=config_random())
# y = SchellingCA(width=8,height=8, state=config_fav())


def loop():
    # approx 5-10 seconds

    width = 8
    height = 8
    state = [[None]*width]*height
    small = 30
    big = 60
    for v in [1,2,5,10]:
        for p1 in range(10,big,10):
            for p2 in range(p1,big,10):
                for p3 in range(small,big,10):
                    for p4 in range(p3,big,10):
                        for q1 in range(small,big,10):
                            for q2 in range(q1,big,10):
                                for q3 in range(small,big,10):
                                    for q4 in range(q3,100,10):
                                        for _ratio in range(0,10,1):
                                            print(v)
                                            white_prefs = {'white': (p1,p2), 'black': (p3,p4)}
                                            pers =  Person(preferences=white_prefs,race='white',vision=v)
                                            s = SchellingCA(width=8,height=8, state=config_fav())

def main():
    #s = SchellingCA(width=8,height=8, state=config_fav())


    for v1 in range(1,11):

        # number of loops: 10 *10^4 * 10^4 * 10
        print(v1)
        for v2 in range(1,11):
            for p1 in range(0,100,10):
                for p2 in range(p1,100,10):
                    for p3 in range(0,100,10):
                        for p4 in range(p3,100,10):
                            for q1 in range(0,100,10):
                                for q2 in range(q1,100,10):
                                    for q3 in range(0,100,10):
                                        for q4 in range(q3,100,10):
                                            for _ratio in range(0,10,1):
                                                ratio = float(_ratio)/float(10)
                                                print(v1)
                                                # also loop over ratio of agents
                                                white_prefs = {'white': (p1,p2), 'black': (p3,p4)}
                                                black_prefs = {'white': (q1,q2), 'black': (q3,q4)}
                                                positions = [(x,y) for x in range(width) for y in range(height)]
                                                num_agents = ratio*width*height
                                                while num_agents > 0:
                                                    r = random.randint(0,len(positions)-1)
                                                    p = positions[r]
                                                    if state[p[0]][p[1]] is None:
                                                        num_agents -= 1
                                                        r2 = random.randint(0,1)
                                                        if r2 == 0:
                                                            pers =  Person(preferences=white_prefs,race='white',vision=v1)
                                                            state[p[0]][p[1]] = pers
                                                        else:
                                                            pers =  Person(preferences=black_prefs,race='black',vision=v2)
                                                            state[p[0]][p[1]] = pers


s = SchellingCA(width=8,height=8, state=config_fav())
print(s)





















