import math


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

    def increment_population(self):
        self.population += 1
        self.cost_imposed_on_weight += 50

    def decrement_population(self):
        self.population -= 1
        self.cost_imposed_on_weight -= 10

    def set_on_fire(self):
        self.is_on_fire = True
        self.cost_imposed_on_weight += 500

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
                min_dist = calculate_distance(self.x, self.y, each_exit.x, each_exit.y)
                min_dist_exit = each_exit

        self.cost_imposed_on_weight = calculate_distance(self.x, self.y, min_dist_exit.x, min_dist_exit.y)

    def put_human_on_tile(self, canvas, x, y):
        if not self.is_on_fire:
            canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black", outline="black")

    def remove_human_on_tile(self, canvas, x, y):
        canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black", outline="black")
