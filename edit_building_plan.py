from tkinter import *
from GUI_Tile import GUI_Tile

all_tiles = {}

container = Tk()

# setting width and height of tkinter window to fit screen
width = container.winfo_screenwidth()  # width of screen
height = container.winfo_screenheight()  # height of screen
container.winfo_toplevel().geometry("%dx%d%+d%+d" % (width, height, 0, 0))

my_canvas = Canvas(container, width=width, height=height)
my_canvas.pack(pady=20)

rect_start_x = None
rect_start_y = None
rect_id = None

for i in range(100):
    all_tiles[i] = {}
    for j in range(100):
        all_tiles[i][j] = None

for x in range(100):
    for y in range(100):
        GUI_Tile(x, y, width, height, all_tiles)


def on_press(event):
    global rect_start_x, rect_start_y, rect_id
    rect_start_x = my_canvas.canvasx(event.x)
    rect_start_y = my_canvas.canvasy(event.y)

    # Remove previous rectangles
    my_canvas.delete("rect")

    # Create a new rectangle
    rect_id = my_canvas.create_rectangle(
        rect_start_x,
        rect_start_y,
        rect_start_x,
        rect_start_y,
        outline="black",
        tags="rect",
    )


def on_drag(event):
    cur_x = my_canvas.canvasx(event.x)
    cur_y = my_canvas.canvasy(event.y)

    # Update the rectangle size as the mouse is dragged
    my_canvas.coords(rect_id, rect_start_x, rect_start_y, cur_x, cur_y)


def on_release(event):
    global rect_start_x, rect_start_y
    # Get the coordinates of the selected region
    rect_end_x = my_canvas.canvasx(event.x)
    rect_end_y = my_canvas.canvasy(event.y)

    # Perform actions based on the selected region
    selected_region_start = (rect_start_x, rect_start_y)
    selected_region_end = (rect_end_x, rect_end_y)

    print("Selected Region Start:", selected_region_start)
    print("Selected Region End:", selected_region_end)

    left_top_x = selected_region_start[0]
    left_top_y = selected_region_start[1]

    right_bottom_x = selected_region_end[0]
    right_bottom_y = selected_region_end[1]

    right_top_x, right_top_y, left_bottom_x, left_bottom_y = calculate_rt_and_lb_coordinates(left_top_x, left_top_y,
                                                                                             right_bottom_x,
                                                                                             right_bottom_y)

    print(left_top_x, left_top_y)
    print(right_top_x, right_top_y)
    print(left_bottom_x, left_bottom_y)
    print(right_bottom_x, right_bottom_y)

    x = left_top_x
    y = left_top_y
    width_of_tile = width / 100
    height_of_tile = height / 100

    big_left_top_x = (x // width_of_tile) * width_of_tile
    big_left_top_y = (y // height_of_tile) * height_of_tile

    x = right_bottom_x
    y = right_bottom_y

    big_right_bottom_x = ((x // width_of_tile) + 1) * width_of_tile
    big_right_bottom_y = ((y // height_of_tile) + 1) * height_of_tile

    big_right_top_x, big_right_top_y, big_left_bottom_x, big_left_bottom_y = calculate_rt_and_lb_coordinates(
        big_left_top_x, big_left_top_y,
        big_right_bottom_x,
        big_right_bottom_y)

    print(big_left_top_x, big_left_top_y)
    print(big_right_top_x, big_right_top_y)
    print(big_left_bottom_x, big_left_bottom_y)
    print(big_right_bottom_x, big_right_bottom_y)

    my_canvas.create_rectangle(big_left_top_x, big_left_top_y, big_right_bottom_x,
                               big_right_bottom_y, fill="blue")


def calculate_rt_and_lb_coordinates(x1, y1, x2, y2):
    x3, y3 = x2, y1  # Right-top coordinate
    x4, y4 = x1, y2  # Left-bottom coordinate
    return x3, y3, x4, y4


# container.bind("<Button-1>", on_release())

"""
tiles = {}

for x in range(200):
    tiles[x] = {}
    for y in range(200):
        tiles[x][y] = Label(container, text="D")
        tiles[x][y].grid(row=x, column=y)
"""

container.bind("<ButtonPress-1>", on_press)
container.bind("<B1-Motion>", on_drag)
container.bind("<ButtonRelease-1>", on_release)
container.mainloop()

"""
import tkinter as tk


class CoordinateSystemGUI:
    def __init__(self, master, width, height, grid_size):
        self.master = master
        self.master.title("Coordinate System GUI")

        self.width = width
        self.height = height
        self.grid_size = grid_size

        self.master.geometry(f"{self.width}x{self.height}")

        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.draw_coordinate_system()
        self.draw_grid()

        self.start_x = None
        self.start_y = None
        self.rect = None

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def draw_coordinate_system(self):
        pass
    # Draw X-axis
    # self.canvas.create_line(0, self.height // 2, self.width, self.height // 2, width=2)

    # Draw Y-axis
    # self.canvas.create_line(self.width // 2, 0, self.width // 2, self.height, width=2)

    def draw_grid(self):
        for i in range(0, self.width, self.grid_size):
            self.canvas.create_line(i, 0, i, self.height, dash=(2, 2), fill="gray")

        for j in range(0, self.height, self.grid_size):
            self.canvas.create_line(0, j, self.width, j, dash=(2, 2), fill="gray")

    def on_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)

        if self.rect:
            self.canvas.delete(self.rect)

        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="blue")

    def on_drag(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)

        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_release(self, event):
        pass  # You can add logic here when the user releases the mouse button


def main():
    root = tk.Tk()
    grid_size = 20
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    app = CoordinateSystemGUI(root, screen_width, screen_height, grid_size)

    root.mainloop()


if __name__ == "__main__":
    main()

import tkinter as tk


class CoordinateSystemGUI:
    def __init__(self, master, width, height):
        self.master = master
        self.master.title("Coordinate System GUI")

        self.width = width
        self.height = height

        self.master.geometry(f"{self.width}x{self.height}")

        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.draw_coordinate_system()

        self.start_x = None
        self.start_y = None
        self.rect = None

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def draw_coordinate_system(self):
        # Draw X-axis
        self.canvas.create_line(50, self.height // 2, self.width - 50, self.height // 2, width=2)

        # Draw Y-axis
        self.canvas.create_line(self.width // 2, 50, self.width // 2, self.height - 50, width=2)

    def on_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)

        if self.rect:
            self.canvas.delete(self.rect)

        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="blue")

    def on_drag(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)

        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_release(self, event):
        pass  # You can add logic here when the user releases the mouse button


def main():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    app = CoordinateSystemGUI(root, screen_width, screen_height)

    root.mainloop()


if __name__ == "__main__":
    main()
"""

"""
import tkinter as tk


class CoordinateSystemGUI:
    def __init__(self, master, width, height, grid_size):
        self.master = master
        self.master.title("Coordinate System GUI")

        self.width = width
        self.height = height
        self.grid_size = grid_size

        self.master.geometry(f"{self.width}x{self.height}")

        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.draw_coordinate_system()
        self.draw_grid()

        self.start_x = None
        self.start_y = None
        self.rect = None

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def draw_coordinate_system(self):
        # Draw X-axis
        self.canvas.create_line(0, self.height // 2, self.width, self.height // 2, width=2)

        # Draw Y-axis
        self.canvas.create_line(self.width // 2, 0, self.width // 2, self.height, width=2)

    def draw_grid(self):
        for i in range(0, self.width, self.grid_size):
            self.canvas.create_line(i, 0, i, self.height, dash=(2, 2), fill="gray")

        for j in range(0, self.height, self.grid_size):
            self.canvas.create_line(0, j, self.width, j, dash=(2, 2), fill="gray")

    def on_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)

        if self.rect:
            self.canvas.delete(self.rect)

        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="blue")

    def on_drag(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)

        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_release(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)

        selected_pixels = self.get_selected_pixels(self.start_x, self.start_y, cur_x, cur_y)
        tile_coordinates = self.get_all_tile_coordinates(selected_pixels)

        print("Selected Pixels:", selected_pixels)
        print("All Tile Coordinates:", tile_coordinates)

    def get_selected_pixels(self, x1, y1, x2, y2):
        # Convert canvas coordinates to pixel coordinates
        x1_pixel, y1_pixel = self.canvas.canvasx(x1), self.canvas.canvasy(y1)
        x2_pixel, y2_pixel = self.canvas.canvasx(x2), self.canvas.canvasy(y2)

        # Ensure x1_pixel < x2_pixel and y1_pixel < y2_pixel
        x1_pixel, x2_pixel = min(x1_pixel, x2_pixel), max(x1_pixel, x2_pixel)
        y1_pixel, y2_pixel = min(y1_pixel, y2_pixel), max(y1_pixel, y2_pixel)

        return (x1_pixel, y1_pixel, x2_pixel, y2_pixel)

    def get_tile_coordinates(self, x, y):
        center_x = x
        center_y = y

        tile_x = int((center_x - self.width // 2) / self.grid_size)
        tile_y = int((self.height // 2 - center_y) / self.grid_size)

        return tile_x, tile_y

    def get_all_tile_coordinates(self, pixels):
        x1, y1, x2, y2 = pixels

        start_tile_x, start_tile_y = self.get_tile_coordinates(x1, y1)
        end_tile_x, end_tile_y = self.get_tile_coordinates(x2, y2)

        all_tile_coordinates = []

        for tile_x in range(start_tile_x, end_tile_x + 1):
            for tile_y in range(start_tile_y, end_tile_y + 1):
                all_tile_coordinates.append((tile_x, tile_y))

        return all_tile_coordinates


def main():
    root = tk.Tk()
    grid_size = 20
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    app = CoordinateSystemGUI(root, screen_width, screen_height, grid_size)

    root.mainloop()


if __name__ == "__main__":
    main()
"""
