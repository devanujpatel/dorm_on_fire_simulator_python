from tkinter import *
import pickle
import preexistingMaps

name = preexistingMaps.
root = Tk()
root.title("")
width = root.winfo_screenwidth()  # width of screen
height = root.winfo_screenheight()  # height of screen
divisions = 100
width_of_tile = width / divisions
height_of_tile = height / divisions
root.winfo_toplevel().geometry("%dx%d%+d%+d" % (width, height, 0, 0))

my_canvas = Canvas(root, width = width, height = height)
my_canvas.pack()

with open(name, 'rb') as p:
    p1 = pickle.load(p)

print("Canvas Dimensions:", my_canvas.winfo_width(), my_canvas.winfo_height())
print(width, height)

for tile in p1:
    location = tile.get_location()
    my_canvas.create_rectangle(location[0] * width_of_tile, location[1] * height_of_tile, location[0] * width_of_tile + width_of_tile,
                               location[1] * height_of_tile + height_of_tile, fill=tile.color, outline = tile.color)


root.mainloop()



