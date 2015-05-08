class Person(object)::
    # pk is personal key = a personal identifying number
    # vision measured in manhattan distance.
    # self.nbr_like_pref is a number between 0 and 1
        # let x = nbr_like_pref
        # the person wants for at least x percent of their neighbors to be like them.

    # Schelling's model does not have dissimilar pref.
    # self.nbr_dissimilar_pref is a number between 0 and 1
        # let y = nbr_dissimilar_pref
        # the person wants for at least y percent of their neighbors to be different from them.

    def __init__(self, nbr_like_pref=0.0, race='white', is_happy=False, vision=1, pk=0, max_walking_distance=100):
        # TODO add max walking distance
        self.nbr_like_pref = nbr_like_pref
        self.race = race
        self.is_happy = is_happy
        self.vision = vision
        self.pk = pk
        self.max_walking_distance = max_walking_distance
        self.distance_walked = 0

    def update_happiness(self, nbr_dict):
        num_neighbors = sum(nbr_dict.values())
        if num_neighbors == 0:
            return True

        ratio =  float (nbr_dict[self.race] / num_neighbors)
        # TODO CHECK THIS
        print('this ratio should be a float: %d' % ratio)

        if ratio < self.nbr_like_pref:
            self.is_happy = False
        else:
            self.is_happy = True
        return self.is_happy

    def strall(self):
        return "(Race: "+self.race + ", is_happy:" + str(self.is_happy) + ", nbr_like_pref:" + str(self.nbr_like_pref) + ")"

    def strsmall(self):
        return str(self.pk) + ' ' + self.race + ' ' + str(self.is_happy)

    def __str__(self):
        return self.strsmall()

    def __repr__(self):
        return str(self)





