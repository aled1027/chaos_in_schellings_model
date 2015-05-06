import logging
import random

def tuple_add(a,b):
        return (a[0]+b[0], a[1]+b[1])

class SchellingCA:
    """
    TODO document what each parameter is
    """
    def __init__(self, width=8, height=8, races=None, state=None, moving_radius_function=None, mode='rw'):
        self.width = width
        self.height = height
        self.is_done = False
        self.amount_segregation = 0
        self.num_iterations = 0
        self.empty_positions = set()
        self.unhappy_positions = set()
        self.happy_positions = set()
        self.state = state if state else [[None]*self.width]*self.height
        self.races = races if races else ['white','black']
        self.mode = mode
        if moving_radius_function:
            self.moving_radius_function = moving_radius_function
        else:
            self.moving_radius_function = lambda x: 10000

        self.update_states_and_sets()


    def __repr__(self):
        return str(self)

    def __str__(self):
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

        width_index = int(index % self.height)
        height_index = int((index - width_index) / self.height)
        return self.state[width_index][height_index]

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
        logging.info('ca.py: update_states_and_sets')
        for index,cell in enumerate(self):
            i = index % self.height
            j = int((index - i) / self.height)
            if cell == None:
                self.empty_positions.add((i,j))
                self.unhappy_positions.discard((i,j))
                self.happy_positions.discard((i,j))
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
        Input: none
        Output: a boolean. True if someone was moved; False is nobody moved
        Change to state:
            1. Picks an unhappy person at random
            2. Tries to move the person via rw or unifrandom depending on the mode
                such that the person is happy at their new position.
        """

        old_x, old_y = 0,0
        did_move_someone = False

        if self.unhappy_positions:
            pos = self.unhappy_positions.pop()
            if self.mode== 'rw':
                did_move_someone = self.move_via_rw(pos)
            elif self.mode == 'unifrandom':
                did_move_someone = self.move_via_unifrandom(pos)
        else:
            logging.debug('Did not move anyone, no unhappy people')
            return False

        if did_move_someone is False:
            logging.debug('Did not move anyone. Could not find a happy place')

        return did_move_someone

    def get_deltas(self, x, y):
        ret = []
        if x > 0:
            ret.append((-1,0))
        if x < self.width - 1:
            ret.append((1,0))
        if y > 0:
            ret.append((0,-1))
        if y < self.height - 1:
            ret.append((0,1))
        return ret


    def move_via_rw(self, pos):
        new_x, new_y = old_x, old_y = pos
        cell = self.state[old_x][old_y]
        self.state[old_x][old_y] = None
        new_x, new_y = old_x, old_y
        distanced_walked = 0
        deltas = {0: (1,0), 1:(-1,0), 3:(0,1), 4:(0,-1)}
        while cell.distance_walked < cell.max_walking_distance:
            cell.distance_walked += 1
            delta = random.choice(self.get_deltas(new_x, new_y))
            new_pos = (new_x, new_y)
            new_x, new_y = tuple_add(new_pos, delta)
            print('checking %d, %d' % (new_x, new_y))
            print('dist walked: %d, max_dist %d' % (cell.distance_walked, cell.max_walking_distance))

            # PROBLEM: IT"S COUNTING ITSELF WHEN CALCULATING ITS NEIGHBORS

            nbr_races = [nbr.race for nbr in self.get_neighbors(new_x, new_y, cell.vision)]
            nbr_dict = {r: nbr_races.count(r) for r in self.races}
            print(nbr_dict)
            if self.state[new_x][new_y] is None and cell.update_happiness(nbr_dict):
                print('hereherhehre')
                self.state[new_x][new_y] = cell
                logging.debug('moved someone from (%d,%d) to (%d,%d)' %(old_x,old_y,new_x,new_y))
                return True

        else:
            self.state[old_x][old_y] = cell
            logging.debug('Did not move anyone. Tried to move: (%d,%d)' % (old_x,old_y,new_x,new_y))
            return False

    def move_via_unifrandom(self, old_x, old_y):
        cell = self.state[old_x][old_y]
        while self.empty_positions:
            new_x,new_y = self.empty_positions.pop()
            dist = abs(new_x - old_x) + abs(new_y-old_y)
            if dist > self.moving_radius_function(cell.vision):
                continue
            nbr_races = [nbr.race for nbr in self.get_neighbors(new_x,new_y,self.state[old_x][old_y].vision)]
            nbr_dict = {r: nbr_races.count(r) for r in self.races}
            b = cell.update_happiness(nbr_dict)
            if (cell.update_happiness(nbr_dict) == True):
                self.state[old_x][old_y],self.state[new_x][new_y] =  self.state[new_x][new_y], self.state[old_x][old_y]
                logging.debug('moved someone from (%d,%d) to (%d,%d)' %(old_x,old_y,new_x,new_y))
                did_move_someone = True
                break

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
        nbr_coords =  [(int(i+a), int(j+b)) for (a,b) in deltas if (0 <= i+a < self.width) and (0 <= j+b < self.height)]
        return [self.state[x][y] for (x,y) in nbr_coords if self.state[x][y] is not None]

    def iterate(self):
        """
        goes through one iteration of schelling's process.
        1. Look at a list of unhappy persons. Pick one randomly.
        2. Move that person
        3. Update everyone else's happiness.
        This aspect could be made more efficient by only updating people within the vision origin and destination of moved person.
        """
        did_move = self.move_someone()
        if (did_move == False):
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
    # pk is personal key = a personal identifying number
    # preferences of the form: {'white': (.2,.3)} indicates prefers more than 20% white neighbors, less than %30 white neighbors.
    # vision measured in manhattan distance.
    def __init__(self, preferences=None, race='white', is_happy=False, races=None, vision=1, pk=0, max_walking_distance=100):
        # TODO add max walking distance
        self.races = races if races else ['white','black']
        self.preferences = preferences if preferences else {}
        self.race = race
        self.is_happy = is_happy
        self.preferences = preferences
        self.vision = vision
        self.pk = pk
        self.max_walking_distance = max_walking_distance
        self.distance_walked = 0

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
        return str(self.pk) + ' ' + self.race + ' ' + str(self.is_happy)

    def __str__(self):
        return self.strsmall()

    def __repr__(self):
        return str(self)

