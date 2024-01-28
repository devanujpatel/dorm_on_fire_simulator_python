from tkinter import *
import pickle
from Fire import Fire

f = open("temp_for_file_name.txt", "r")
name = f.read()
print(name)
f.close()
root = Tk()
root.title("")
width = root.winfo_screenwidth()  # width of screen
height = root.winfo_screenheight()  # height of screen
divisions = 100
width_of_tile = width / divisions
height_of_tile = height / divisions
fire_list = []

root.winfo_toplevel().geometry("%dx%d%+d%+d" % (width, height, 0, 0))

radio_selection = "human"

var = StringVar()
human_button = Radiobutton(root, text="Human", variable=var, value="human")
human_button.pack(side=TOP, padx=10)
fire_button = Radiobutton(root, text="Fire", variable=var, value="fire")
fire_button.pack(side=TOP, padx=10)


def submit():
    global fire_list, all_tiles_dict, all_tiles_list
    root.unbind("<Button-1>")
    human_button.destroy()
    fire_button.destroy()
    subButton.destroy()
    print(fire_list)
    spreader = Fire(fire_list, all_tiles_list, all_tiles_dict, my_canvas)
    spreader.spread_fire()


subButton = Button(root, text="Submit", command=submit)
subButton.pack()

my_canvas = Canvas(root, width=width, height=height)
my_canvas.pack()

with open(name, "rb") as file:
    data = pickle.load(file)
    all_tiles_list = data["list"]
    all_tiles_dict = data["dictionary"]

print("Canvas Dimensions:", my_canvas.winfo_width(), my_canvas.winfo_height())
print(width, height)

for tile in all_tiles_list:
    location = tile.get_location()
    my_canvas.create_rectangle(location[0] * width_of_tile, location[1] * height_of_tile,
                               location[0] * width_of_tile + width_of_tile,
                               location[1] * height_of_tile + height_of_tile, fill=tile.color, outline=tile.color)


def on_click(event):
    global radio_selection, fire_list, all_tiles_dict
    x, y = event.x, event.y
    x_coord = int(x / width_of_tile)
    y_coord = int(y / height_of_tile)
    radio_selection = var.get()
    if radio_selection == "human":
        all_tiles_dict[x_coord][y_coord].increment_population()
        my_canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black", outline="black")

    else:
        try:
            all_tiles_dict[x_coord][y_coord].set_on_fire(my_canvas, x, y)
            #my_canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="OrangeRed2", outline="OrangeRed2")
            fire_list.append(all_tiles_dict[x_coord][y_coord])
        except:
            pass

root.bind("<Button-1>", on_click)

root.mainloop()
