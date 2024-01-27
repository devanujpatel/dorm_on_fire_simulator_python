class GUI_Tile:
    def __init__(self, x, y, width, height, all_tiles):
        self.x = x
        self.y = y
        self.WIDTH = width / 100
        self.HEIGHT = height / 100
        all_tiles[x][y] = self
        self.human_presence = 0
