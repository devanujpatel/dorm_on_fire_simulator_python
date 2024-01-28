from vertices_and_edges import VerticesAndEdges


class Fire:
    def __init__(self, fire_list, all_tiles_list, all_tiles_dict, canvas, width, height):
        self.fire_list = fire_list
        self.all_tiles_list = all_tiles_list
        self.all_tiles_dict = all_tiles_dict
        self.dataset = VerticesAndEdges(self.all_tiles_list, self.all_tiles_dict)
        self.canvas = canvas
        self.width = width
        self.height = height

    def spread_fire(self):
        # print("fire spread called")
        # print(self.fire_list)
        fire_list2 = []
        for tile in self.fire_list:
            x = tile.x
            y = tile.y
            tile.set_on_fire(self.canvas, x * self.width, y * self.height, self.width, self.height, "red2")
            # print(x, y)
            # print(tile.flammable)
            # top left cell
            if x - 1 >= 0 and y - 1 >= 0 and self.all_tiles_dict[x - 1][y - 1] is not None and \
                    self.all_tiles_dict[x - 1][
                        y - 1].flammable == "Yes":
                # print("past1")
                self.all_tiles_dict[x - 1][y - 1].set_on_fire(self.canvas,
                                                              self.all_tiles_dict[x - 1][y - 1].x * self.width,
                                                              self.all_tiles_dict[x - 1][y - 1].y * self.height,
                                                              self.width, self.height, "deep sky blue")
                var = self.all_tiles_dict[x - 1][y - 1].x
                var2 = self.all_tiles_dict[x - 1][y - 1].y
                fire_list2.append(self.all_tiles_dict[x - 1][y - 1])

                # top up same column
            if y - 1 >= 0 and self.all_tiles_dict[x][y - 1] is not None and self.all_tiles_dict[x][
                y - 1].flammable == "Yes":
                # print("past2")
                self.all_tiles_dict[x][y - 1].set_on_fire(self.canvas, self.all_tiles_dict[x][y - 1].x * self.width,
                                                          self.all_tiles_dict[x][y - 1].y * self.height, self.width,
                                                          self.height, "gold")
                fire_list2.append(self.all_tiles_dict[x][y - 1])

                # top right
            if x + 1 <= 99 and y - 1 >= 0 and self.all_tiles_dict[x + 1][y - 1] is not None and \
                    self.all_tiles_dict[x + 1][
                        y - 1].flammable == "Yes":
                # print("past3")
                self.all_tiles_dict[x + 1][y - 1].set_on_fire(self.canvas,
                                                              self.all_tiles_dict[x + 1][y - 1].x * self.width,
                                                              self.all_tiles_dict[x + 1][y - 1].y * self.height,
                                                              self.width, self.height, "burlywood4")
                var = self.all_tiles_dict[x + 1][y - 1].x
                var2 = self.all_tiles_dict[x + 1][y - 1].y
                fire_list2.append(self.all_tiles_dict[x + 1][y - 1])
                # self.canvas.create_rectangle((x+1)*self.width, (y-1)*self.height, (x+1)*self.width + self.width, (y-1)*self.height + self.height, fill="Cyan2", outline="OrangeRed2")

                # same level left
            if x - 1 >= 0 and self.all_tiles_dict[x - 1][y] is not None and self.all_tiles_dict[x - 1][
                y].flammable == "Yes":
                # rint("past4")
                self.all_tiles_dict[x - 1][y].set_on_fire(self.canvas, self.all_tiles_dict[x - 1][y].x * self.width,
                                                          self.all_tiles_dict[x - 1][y].y * self.height, self.width,
                                                          self.height, "indian red")
                fire_list2.append(self.all_tiles_dict[x - 1][y])

            # same level right
            if x + 1 <= 99 and self.all_tiles_dict[x + 1][y] is not None and self.all_tiles_dict[x + 1][
                y].flammable == "Yes":
                # print("past5")
                self.all_tiles_dict[x + 1][y].set_on_fire(self.canvas, self.all_tiles_dict[x + 1][y].x * self.width,
                                                          self.all_tiles_dict[x + 1][y].y * self.height, self.width,
                                                          self.height, "orange")
                fire_list2.append(self.all_tiles_dict[x + 1][y])

            # bottom left
            if x - 1 >= 0 and y + 1 <= 99 and self.all_tiles_dict[x - 1][y + 1] is not None and \
                    self.all_tiles_dict[x - 1][
                        y + 1].flammable == "Yes":
                # print("past6")
                self.all_tiles_dict[x - 1][y + 1].set_on_fire(self.canvas,
                                                              self.all_tiles_dict[x - 1][y + 1].x * self.width,
                                                              self.all_tiles_dict[x - 1][y + 1].y * self.height,
                                                              self.width, self.height, "hot pink")
                fire_list2.append(self.all_tiles_dict[x - 1][y + 1])

            # same column bottom down
            if y + 1 <= 99 and self.all_tiles_dict[x][y + 1] is not None and self.all_tiles_dict[x][
                y + 1].flammable == "Yes":
                # print("past7")
                self.all_tiles_dict[x][y + 1].set_on_fire(self.canvas, self.all_tiles_dict[x][y + 1].x * self.width,
                                                          self.all_tiles_dict[x][y + 1].y * self.height, self.width,
                                                          self.height, "dark violet")
                fire_list2.append(self.all_tiles_dict[x][y + 1])

            # bottom right
            if x + 1 <= 99 and y + 1 <= 99 and self.all_tiles_dict[x + 1][y + 1] is not None and \
                    self.all_tiles_dict[x + 1][
                        y + 1].flammable == "Yes":
                # print("past8")
                self.all_tiles_dict[x + 1][y + 1].set_on_fire(self.canvas,
                                                              self.all_tiles_dict[x + 1][y + 1].x * self.width,
                                                              self.all_tiles_dict[x + 1][y + 1].y * self.height,
                                                              self.width, self.height, "khaki")
                fire_list2.append(self.all_tiles_dict[x + 1][y + 1])
        # for tile in self.fire_list:
        # print(tile.x, tile.y,)
        # for tile in fire_list2:
        # print(tile.x, tile.y, )
        self.fire_list.clear()
        # print(self.fire_list)
        self.fire_list.extend(fire_list2)
        # print(self.fire_list)
        if len(self.fire_list) != 0:
            self.spread_fire()
