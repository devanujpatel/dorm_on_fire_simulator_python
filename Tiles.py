import math
import time

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


class Tile:
    def __init__(self, x, y, walkable, flammable, is_on_fire, has_human, color, id):
        self.x = x
        self.y = y
        self.walkable = walkable
        self.flammable = flammable
        self.is_on_fire = is_on_fire
        self.color = color
        self.population = 0
        self.id = id
        self.cost_imposed_on_weight = 0
        #self.all_tile_dicts = all_tiles_dict

    def increment_population(self):
        self.population += 1
        self.cost_imposed_on_weight += 100

    def decrement_population(self):
        self.population -= 1
        self.cost_imposed_on_weight -= 100

    def set_on_fire(self):
        self.flammable = True
        self.cost_imposed_on_weight += 500

    def is_walkable(self):
        return self.walkable

    def is_flammable(self):
        return self.flammable

    def is_on_fire(self):
        return self.is_on_fire

    def has_human(self):
        return self.has_human

    def get_location(self):
        return self.x, self.y

    def calculate_costs(self, exits):
        min_dist = 123456
        min_dist_exit = None
        print(exits)
        for each_exit in exits:
            if min_dist == 123456:
                min_dist_exit = each_exit
            elif calculate_distance(self.x, self.y, each_exit.x, each_exit.y) < min_dist_exit:
                min_dist_exit = calculate_distance(self.x, self.y, each_exit.x, each_exit.y)
                min_dist_exit = each_exit

        self.cost_imposed_on_weight = calculate_distance(self.x, self.y, min_dist_exit.x, min_dist_exit.y)
