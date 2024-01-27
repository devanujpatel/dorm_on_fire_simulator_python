class Tile:
    def __init__(self,x,y, walkable,flammable,is_on_fire,color):
        self.x = x
        self.y = y
        self.walkable = walkable
        self.flammable = flammable
        self.is_on_fire = is_on_fire
        self.color = color

