class Tile:
    def __init__(self, x, y, walkable, flammable, is_on_fire, has_human):
        self.x = x
        self.y = y
        self.walkable = walkable
        self.flammable = flammable
        self.is_on_fire = is_on_fire
        self.has_human = has_human

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
