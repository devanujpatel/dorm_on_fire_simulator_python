import heapq
import pickle
import threading
from vertices_and_edges import VerticesAndEdges
import time


class Person(threading.Thread):
    def __init__(self, x, y, all_tiles_list, all_tiles_dict, my_canvas, width_of_tile, height_of_tile): #fire_values
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
        # self.fire_values = fire_values

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
        #print(len(self.fire_values))
        print("these many are in person")
        time.sleep(0.1)
        #self.fire_list.append(Fire.get_fire_list())
        #data_set = VerticesAndEdges(self.all_tiles_list, self.all_tiles_dict)
        #lowest_cost_neighbour = None

        curr = self.all_tiles_dict[self.x_coord][self.y_coord]
        if curr.color == "maroon":
            self.my_canvas.create_rectangle(self.x_coord * self.width, self.y_coord * self.height,
                                            self.x_coord * self.width + self.width,
                                            self.y_coord * self.height + self.height, fill="maroon",
                                            outline="maroon")
            return

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

        minCost = 100000
        minCostNeigh = None

        for neighbour in n:
            time.sleep(0.1)
            if neighbour is None:
                continue

            if minCostNeigh is None:
                minCostNeigh = neighbour

            # if neighbour in self.fire_values:
            #     continue

            neighbour.calculate_costs(exits)
            cost = neighbour.cost_imposed_on_weight

            # neighbour.calculate_costs(self.fire_values)

            #print(f"before adding: {cost}")
            # cost += 100 * neighbour.cost_imposed_on_weight
            #print(f"after adding: {cost}")

            # if neighbour in self.fire_values:
            #     cost += self.fire_values[neighbour]

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
            print(f"Cost here: {cost}")
            if neighbour.color == "maroon":
                minCostNeigh = neighbour
                break
            elif cost < minCost:
                minCost = cost
                minCostNeigh = neighbour

        #print(minCostNeigh.x, minCostNeigh.y)

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