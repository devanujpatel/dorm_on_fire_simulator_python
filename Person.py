import heapq
import pickle
import threading
from vertices_and_edges import VerticesAndEdges
import time


class Person(threading.Thread):
    def __init__(self, x, y, all_tiles_list, all_tiles_dict, my_canvas, width_of_tile, height_of_tile, fire_values):
        super().__init__()
        self.x_coord = x
        self.y_coord = y
        self.status = "Inside"
        self.alive = True
        self.all_tiles_list = all_tiles_list
        self.all_tiles_dict = all_tiles_dict
        self.my_canvas = my_canvas
        self.width = width_of_tile
        self.height = height_of_tile
        self.fire_values = fire_values

        f = open("temp_for_file_name.txt", "r")
        name = f.read()
        print(name)
        f.close()

        with open(name, "rb") as file:
            data = pickle.load(file)
            self.all_tiles_list = data["list"]
            self.all_tiles_dict = data["dictionary"]

    def run(self):
        self.makeNextMove()

    def makeNextMove(self):
        time.sleep(0.3)
        data_set = VerticesAndEdges(self.all_tiles_list, self.all_tiles_dict)
        lowest_cost_neighbour = None

        curr = self.all_tiles_dict[self.x_coord][self.y_coord]
        if curr.color == "maroon":
            self.my_canvas.create_rectangle(self.x_coord * self.width, self.y_coord * self.height,
                                            self.x_coord * self.width + self.width,
                                            self.y_coord * self.height + self.height, fill="maroon",
                                            outline="maroon")
            return


        lowest_cost = 10000
        left = False
        print(data_set.tile_to_neighbouring_tiles_costs)

        n = [self.all_tiles_dict[self.x_coord - 1][self.y_coord - 1],
             self.all_tiles_dict[self.x_coord][self.y_coord - 1],
             self.all_tiles_dict[self.x_coord + 1][self.y_coord - 1],
             self.all_tiles_dict[self.x_coord - 1][self.y_coord], self.all_tiles_dict[self.x_coord + 1][self.y_coord],
             self.all_tiles_dict[self.x_coord - 1][self.y_coord + 1],
             self.all_tiles_dict[self.x_coord][self.y_coord + 1]]

        exits = []
        for tile in self.all_tiles_list:
            if tile.color == "maroon":
                exits.append(tile)

        minCost = 10000
        minCostNeigh = None

        for neighbour in n:
            time.sleep(0.3)
            if neighbour is None:
                continue

            if minCostNeigh is None:
                minCostNeigh = neighbour

            neighbour.calculate_costs(exits)
            cost = neighbour.cost_imposed_on_weight
            if neighbour in self.fire_values:
                cost += self.fire_values[neighbour]


            if neighbour.is_on_fire:
                cost += 5000
                n = [self.all_tiles_dict[neighbour.x_coord - 1][neighbour.y_coord - 1],
                     self.all_tiles_dict[neighbour.x_coord][neighbour.y_coord - 1],
                     self.all_tiles_dict[neighbour.x_coord + 1][neighbour.y_coord - 1],
                     self.all_tiles_dict[neighbour.x_coord - 1][neighbour.y_coord],
                     self.all_tiles_dict[neighbour.x_coord + 1][neighbour.y_coord],
                     self.all_tiles_dict[neighbour.x_coord - 1][neighbour.y_coord + 1],
                     self.all_tiles_dict[neighbour.x_coord][neighbour.y_coord + 1]]
                for dn in n:
                    if dn.is_on_fire:
                        cost += 3000
                    else:
                        dn.cost_imposed_on_weight += 500

            if neighbour.color == "maroon":
                minCostNeigh = neighbour
                break
            elif cost < minCost:
                minCost = cost
                minCostNeigh = neighbour

        print(minCostNeigh.x, minCostNeigh.y)

        self.my_canvas.create_rectangle(self.x_coord * self.width, self.y_coord * self.height,
                                        self.x_coord * self.width + self.width,
                                        self.y_coord * self.height + self.height, fill="white",
                                        outline="white")
        self.x_coord = minCostNeigh.x
        self.y_coord = minCostNeigh.y
        self.my_canvas.create_rectangle(self.x_coord * self.width, self.y_coord * self.height,
                                        self.x_coord * self.width + self.width,
                                        self.y_coord * self.height + self.height, fill="black",
                                        outline="black")
        self.makeNextMove()




        """
        for neighbour in data_set.tile_to_neighbouring_tiles_costs[self.x_coord][self.y_coord]:
            if lowest_cost_neighbour is None:
                lowest_cost_neighbour = neighbour
            elif neighbour.color == "maroon":
                lowest_cost = \
                    data_set.tile_to_neighbouring_tiles_costs[self.all_tiles_dict[self.x_coord][self.y_coord]][
                        neighbour]
                lowest_cost_neighbour = self.all_tiles_dict[self.x_coord][self.y_coord]
                self.my_canvas.create_rectangle(self.x_coord * self.width, self.y_coord * self.height,
                                                self.x_coord * self.width + self.width,
                                                self.y_coord * self.height + self.height, fill="maroon",
                                                outline="maroon")
                left = True
                break
            elif data_set.tile_to_neighbouring_tiles_costs[curr][neighbour] < lowest_cost:
                lowest_cost = data_set.tile_to_neighbouring_tiles_costs[self.all_tiles_dict[self.x_coord][self.y_coord]][neighbour]
                lowest_cost_neighbour = self.all_tiles_dict[self.x_coord][self.y_coord]

        if not left:
            self.my_canvas.create_rectangle(self.x_coord * self.width, self.y_coord * self.height,
                                            self.x_coord * self.width + self.width,
                                            self.y_coord * self.height + self.height, fill="maroon",
                                            outline="white")
            self.x_coord = lowest_cost_neighbour.x_coord
            self.y_coord = lowest_cost_neighbour.y_coord
            self.my_canvas.create_rectangle(self.x_coord * self.width, self.y_coord * self.height,
                                            self.x_coord * self.width + self.width,
                                            self.y_coord * self.height + self.height, fill="maroon",
                                            outline="black")
            self.makeNextMove()
        """
"""
    def leave_building(self, exit_point):
        self.location = exit_point
        self.status = "Outside"
        self.evacuation_status = True
        print(f"{self.name} left the building through {exit_point}.")

"""