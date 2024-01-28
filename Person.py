import heapq
import pickle
from vertices_and_edges import VerticesAndEdges


class Person:
    def __init__(self, x, y, all_tiles_list, all_tiles_dict, my_canvas, width_of_tile, height_of_tile):
        self.x_coord = x
        self.y_coord = y
        self.status = "Inside"
        self.alive = True
        self.all_tiles_list = all_tiles_list
        self.all_tiles_dict = all_tiles_dict
        self.my_canvas = my_canvas
        self.width = width_of_tile
        self.height = height_of_tile

        f = open("temp_for_file_name.txt", "r")
        name = f.read()
        print(name)
        f.close()

        with open(name, "rb") as file:
            data = pickle.load(file)
            self.all_tiles_list = data["list"]
            self.all_tiles_dict = data["dictionary"]

    def makeNextMove(self):

        data_set = VerticesAndEdges(self.all_tiles_list, self.all_tiles_dict)

        lowest_cost_neighbour = None

        curr = self.all_tiles_dict[self.x_coord][self.y_coord]

        lowest_cost = 10000
        left = False
        print(data_set.tile_to_neighbouring_tiles_costs)



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
    def leave_building(self, exit_point):
        self.location = exit_point
        self.status = "Outside"
        self.evacuation_status = True
        print(f"{self.name} left the building through {exit_point}.")

"""