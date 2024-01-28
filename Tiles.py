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

    def set_on_fire(self, canvas, x, y, width, height, color, all_tiles_dict):
        #print(f"{x}, {y}, onfire")
        canvas.create_rectangle(x, y, x + width , y + height, fill=color, outline = "OrangeRed2")

        #canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="OrangeRed2", outline="OrangeRed2")
        self.is_on_fire = True
        self.cost_imposed_on_weight += 500
        self.worsen_neighbour_costs(all_tiles_dict, 3000)

    def worsen_neighbour_costs(self, all_tiles_dict, offset, fire_values):
        n = [
            all_tiles_dict[self.x-1][self.y-1],
            all_tiles_dict[self.x][self.y - 1],
            all_tiles_dict[self.x + 1][self.y - 1],
            all_tiles_dict[self.x - 1][self.y],
            all_tiles_dict[self.x + 1][self.y],
            all_tiles_dict[self.x - 1][self.y + 1],
            all_tiles_dict[self.x][self.y + 1],
            all_tiles_dict[self.x + 1][self.y + 1]
        ]
        for neighbour in n:
            if neighbour is None:
                continue
            neighbour.cost_imposed_on_weight += offset
            if neighbour in fire_values:
                fire_values[neighbour] += offset
            else:
                fire_values[neighbour] = offset


    def is_walkable(self):
        return self.walkable

    def is_flammable(self):
        return self.flammable

    def has_human(self):
        return self.has_human

    def get_location(self):
        return self.x, self.y

    def calculate_costs(self, exits):
        min_dist = 123456
        min_dist_exit = None
        #print(exits)
        for each_exit in exits:
            if min_dist == 123456:
                min_dist_exit = each_exit
            elif calculate_distance(self.x, self.y, each_exit.x, each_exit.y) < min_dist:
                min_dist = calculate_distance(self.x, self.y, each_exit.x, each_exit.y)
                min_dist_exit = each_exit

        self.cost_imposed_on_weight += calculate_distance(self.x, self.y, min_dist_exit.x, min_dist_exit.y)
        print(self.cost_imposed_on_weight)
