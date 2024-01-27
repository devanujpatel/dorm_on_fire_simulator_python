class Rectangle:
    def __init__(self, left_top_x, left_top_y, right_top_x, right_top_y, left_bottom_x, left_bottom_y, right_bottom_x,
                 right_bottom_y):
        self.left_top_x = left_top_x
        self.left_top_y = left_top_y
        self.right_top_x = right_top_x
        self.right_top_y = right_top_y
        self.left_bottom_x = left_bottom_x
        self.left_bottom_y = left_bottom_y
        self.right_bottom_x = right_bottom_x
        self.right_bottom_y = right_bottom_y

    def get_coords(self):
        return (self.left_top_x, self.left_top_y, self.right_bottom_x, self.right_bottom_y)
