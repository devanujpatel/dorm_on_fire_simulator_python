from tkinter import *
import pickle

f = open("temp_for_file_name.txt", "r")
name = f.read()
print(name)
f.close()
root = Tk()
root.title("")
width = root.winfo_screenwidth()  # width of screen
height = root.winfo_screenheight()  # height of screen
divisions = 100
width_of_tile = width // divisions
height_of_tile = height // divisions
root.winfo_toplevel().geometry("%dx%d%+d%+d" % (width, height, 0, 0))

radio_selection = "human"

var = StringVar()
human_button = Radiobutton(root, text="Human", variable=var, value="human")
human_button.pack(side=TOP, padx=10)
fire_button = Radiobutton(root, text="Fire", variable=var, value="fire")
fire_button.pack(side=TOP, padx=10)


def submit():
    root.unbind("<Button-1>")
    human_button.destroy()
    fire_button.destroy()
    subButton.destroy()


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
    my_canvas.create_rectangle(tile.x * width_of_tile, tile.y * height_of_tile,
                               tile.x * width_of_tile + width_of_tile,
                               tile.y * height_of_tile + height_of_tile, fill=tile.color, outline=tile.color)


def on_click(event):
    global radio_selection
    x, y = event.x, event.y
    x_coord = int(x / width_of_tile)
    y_coord = int(y / height_of_tile)

    radio_selection = var.get()

    print(all_tiles_dict)
    print("look here")
    print(x_coord, y_coord)

    if radio_selection == "human":
        all_tiles_dict[x_coord][y_coord].increment_population()
        all_tiles_dict[x_coord][y_coord].put_human_on_tile(my_canvas, x, y)
    else:
        try:
            all_tiles_dict[x_coord][y_coord].set_on_fire()
            my_canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="OrangeRed2", outline="OrangeRed2")
        except:
            pass


root.bind("<Button-1>", on_click)

root.mainloop()
