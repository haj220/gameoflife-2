class Terrain(list):

    WATER = 0

    def __init__(self, x, y, years):
        self.x = x
        self.y = y
        self.years = years

    def create(self):
        for i in range(self.y):
            self.append([Terrain.WATER] * self.x)

        import random
        for i in range(self.years):
            cell_x = random.randrange(self.x)
            cell_y = random.randrange(self.y)
            self[cell_y][cell_x] = 1

    def show(self):
        import pprint
        pprint.pprint(self)


class Life(list):

    NO_LIFE = None

    SUPPORTED_ON_TERRAIN = {
        None: None,
        0: 0,
        1: 1,
        }

    REP = {
        None: ' ',
        0: 'f',
        1: 'b',
        }

    def __init__(self, terrain):
        self.terrain = terrain

    def create(self):
        for i in range(self.terrain.y):
            self.append([Life.NO_LIFE] * self.terrain.x)

        self.populate()

    def populate(self):
        for y in range(self.terrain.y):
            for x in range(self.terrain.x):
                if self.life_is_posible(x, y):
                    self[y][x] = self.get_life_kind(x, y)

    def get_life_kind(self, x, y):
        return Life.SUPPORTED_ON_TERRAIN[self.terrain[x][y]]

    def life_is_posible(self, x, y):
        import random
        return random.randint(0, 1)

    def show(self):
        import copy
        _rep = copy.deepcopy(self)
        for y in range(self.terrain.y):
            for x in range(self.terrain.x):
                _rep[y][x] = Life.REP[self[y][x]]
        import pprint
        pprint.pprint(_rep)

    def update(self):
        pass


class World:

    def __init__(self, x, y, years):
        self.terrain = Terrain(x, y, years)
        self.life = Life(self.terrain)

    def create(self):
        self._create_terrain()
        self._create_life()

    def _create_terrain(self):
        self.terrain.create()

    def _create_life(self):
        self.life.create()

    def show(self):
        self.terrain.show()
        self.life.show()

    def update(self):
        self._alter_terrain()
        self._grow_life()

    def _alter_terrain(self):
        pass

    def _grow_life(self):
        self.life.update()


def WorldConfig():
    return {'x': 5,
            'y': 5,
            'years': 25,
            }


def show(item):
    item.show()


def update(item):
    item.update()


def delay():
    from time import sleep
    sleep(1)


def main():
    world_config = WorldConfig()
    world = World(**world_config)

    world.create()

    playing = True
    while playing:
        show(world)
        update(world)
        delay()


if __name__ == "__main__":
    main()
