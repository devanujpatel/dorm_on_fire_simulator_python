class VerticesAndEdges:
    def __init__(self, all_tiles_list, all_tiles_dict):
        self.all_tiles_list = all_tiles_list
        self.all_tiles_dict = all_tiles_dict
        self.tile_to_neighbouring_tiles = {}
        self.tile_to_neighbouring_tiles_costs = {}

    def work(self):
        for tile in self.all_tiles_list:

            self.tile_to_neighbouring_tiles[tile] = []
            self.tile_to_neighbouring_tiles_costs[tile] = {}
            x = tile.x
            y = tile.y

            # top left cell
            if x - 1 >= 0 and y - 1 >= 0 and self.all_tiles_dict[x - 1][y - 1] is not None and self.all_tiles_dict[x - 1][y - 1].walkable == True:
                self.tile_to_neighbouring_tiles[tile].append(self.all_tiles_dict[x - 1][y - 1])
                self.tile_to_neighbouring_tiles_costs[tile][self.all_tiles_dict[x - 1][y - 1]] = 1

                # top up same column
            if y - 1 >= 0 and self.all_tiles_dict[x][y - 1] is not None and self.all_tiles_dict[x][y - 1].walkable == True:
                self.tile_to_neighbouring_tiles[tile].append(self.all_tiles_dict[x][y - 1])
                self.tile_to_neighbouring_tiles_costs[tile][self.all_tiles_dict[x][y - 1]] = 1

                # top right
            if x + 1 <= 99 and y - 1 >= 0 and self.all_tiles_dict[x - 1][y - 1] is not None and self.all_tiles_dict[x - 1][y - 1].walkable == True:
                self.tile_to_neighbouring_tiles[tile].append(self.all_tiles_dict[x + 1][y - 1])
                self.tile_to_neighbouring_tiles_costs[tile][self.all_tiles_dict[x + 1][y - 1]] = 1

                # same level left
            if x - 1 >= 0 and self.all_tiles_dict[x - 1][y] is not None and self.all_tiles_dict[x - 1][y].walkable == True:
                self.tile_to_neighbouring_tiles[tile].append(self.all_tiles_dict[x - 1][y])
                self.tile_to_neighbouring_tiles_costs[tile][self.all_tiles_dict[x - 1][y]] = 1

                # same level right
            if x + 1 <= 99 and self.all_tiles_dict[x + 1][y] is not None and self.all_tiles_dict[x + 1][y].walkable == True:
                self.tile_to_neighbouring_tiles[tile].append(self.all_tiles_dict[x + 1][y])
                self.tile_to_neighbouring_tiles_costs[tile][self.all_tiles_dict[x + 1][y]] = 1

                # bottom left
            if x - 1 >= 0 and y + 1 <= 99 and self.all_tiles_dict[x - 1][y + 1] is not None and self.all_tiles_dict[x - 1][y + 1].walkable == True:
                self.tile_to_neighbouring_tiles[tile].append(self.all_tiles_dict[x - 1][y + 1])
                self.tile_to_neighbouring_tiles_costs[tile][self.all_tiles_dict[x - 1][y + 1]] = 1

            # same column bottom down
            if y + 1 <= 99 and self.all_tiles_dict[x][y + 1] is not None and self.all_tiles_dict[x][y + 1].walkable == True:
                self.tile_to_neighbouring_tiles[tile].append(self.all_tiles_dict[x][y + 1])
                self.tile_to_neighbouring_tiles_costs[tile][self.all_tiles_dict[x][y + 1]] = 1

            # bottom right
            if x + 1 <= 99 and y + 1 <= 99 and self.all_tiles_dict[x + 1][y + 1] is not None and self.all_tiles_dict[x + 1][y + 1].walkable == True:
                self.tile_to_neighbouring_tiles[tile].append(self.all_tiles_dict[x + 1][y + 1])
                self.tile_to_neighbouring_tiles_costs[tile][self.all_tiles_dict[x + 1][y + 1]] = 1

