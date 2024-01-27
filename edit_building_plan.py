import threading
import time
from tkinter import *
import pickle
from tkinter import simpledialog, messagebox

# from GUI_Tile import GUI_Tile
from Rectangle import Rectangle
from Tiles import Tile

# from tkinter import messagebox, simpledialog

divisions = 100
all_tiles = {}
all_tiles_list = []
all_rectangles = []
big_rectangle_id = 0

container = Tk()

# setting width and height of tkinter window to fit screen
width = container.winfo_screenwidth()  # width of screen
height = container.winfo_screenheight()  # height of screen
container.winfo_toplevel().geometry("%dx%d%+d%+d" % (width, height, 0, 0))


def save_to_dat_file():
    global container
    container.unbind("<ButtonPress-1>")
    container.unbind("<B1-Motion>")
    container.unbind("<ButtonRelease-1>")

    my_canvas.destroy()
    new_map_frame = Frame(container, height=container.winfo_height() - 10, width=container.winfo_screenheight() - 10)
    new_map_frame.pack()
    name_label = Label(new_map_frame, text="Enter Name of Map: ")
    name_label.pack()
    e = Entry(new_map_frame, width=50, bg="white")
    e.focus_set()

    def enterName():
        global container
        name = e.get()
        print(name)
        new_map_frame.destroy()
        print("saving")
        with open(f"{name}.dat", 'wb') as file:
            pickle.dump(all_tiles_list, file)

    e.pack()
    submitButton = Button(new_map_frame, text="Submit", padx=5, pady=5, command=enterName)
    submitButton.pack()


# submit_button = Button(container, text="Submit plan", command=save_to_dat_file)
# submit_button.pack()
try:
    container.bind('<Control-s>', lambda event: save_to_dat_file())
    container.bind('<Command-s>', lambda event: save_to_dat_file())
except:
    pass

my_canvas = Canvas(container, width=width, height=height)
my_canvas.grid(row = 1, column = 0) #pack(pady=20))

rect_start_x = None
rect_start_y = None
rect_id = None

for i in range(divisions):
    all_tiles[i] = {}
    for j in range(divisions):
        all_tiles[i][j] = None

# for x in range(divisions):
#    for y in range(divisions):
#        GUI_Tile(x, y, width, height, all_tiles)

saveMessage = Label(container, text ="To Save: COMMAND + S (Mac) or CTRL + S", width = 50)
saveMessage.grid(row = 0, column = 0)

tempFlammable = False
tempWalkable = False
wait_for_response = False
tempColor = None


class thread(threading.Thread):
    def __init__(self, thread_name, thread_ID, big_left_top_x, big_left_top_y, big_right_bottom_x, big_right_bottom_y,
                 width_of_tile, height_of_tile):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID
        self.big_left_top_x = big_left_top_x
        self.big_left_top_y = big_left_top_y
        self.big_right_bottom_x = big_right_bottom_x
        self.big_right_bottom_y = big_right_bottom_y
        self.width_of_tile = width_of_tile
        self.height_of_tile = height_of_tile

        # helper function to execute the threads

    def run(self):
        global big_rectangle_id
        print("running")
        while True:
            print(tempColor)
            if tempColor is None:
                time.sleep(1)
                print(tempColor)
            else:
                print("breaking")
                break


def draw_grid_on_canvas(canvas, width, height, divisions):
    cell_width = width / divisions
    cell_height = height / divisions

    for i in range(1, divisions):
        x = i * cell_width
        canvas.create_line(x, 0, x, height, fill="gray", dash=(2, 2))

    for i in range(1, divisions):
        y = i * cell_height
        canvas.create_line(0, y, width, y, fill="gray", dash=(2, 2))


def further_process(big_left_top_x, big_left_top_y, big_right_bottom_x, big_right_bottom_y, width_of_tile,
                    height_of_tile):
    global big_rectangle_id
    print("---")
    print(tempColor)
    print("---")

    my_canvas.create_rectangle(big_left_top_x, big_left_top_y, big_right_bottom_x,
                               big_right_bottom_y, fill=tempColor)

    # flammability, walkability, color = ask_the_three_questions()
    starting_x = round(big_left_top_x / width_of_tile, 0)
    starting_y = round(big_left_top_y / height_of_tile, 0)

    print("---")
    print(starting_x, starting_y)

    ending_x = round(big_right_bottom_x / width_of_tile, 0)
    ending_y = round(big_right_bottom_y / height_of_tile, 0)

    print(ending_x, ending_y)

    for x_coord in range(int(starting_x), int(ending_x) + 1):
        for y_coord in range(int(starting_y), int(ending_y) + 1):
            all_tiles[x_coord][y_coord] = Tile(x_coord, y_coord, tempWalkable, tempFlammable, False, False,
                                               tempColor,
                                               big_rectangle_id)
            all_tiles_list.append(Tile(x_coord, y_coord, tempWalkable, tempFlammable, False, False,
                                       tempColor,
                                       big_rectangle_id))
    big_rectangle_id += 1
    rect_start_x = None
    rect_start_y = None
    rect_id = None
    print("done")
    print(all_tiles_list)


def ask_the_three_questions(big_left_top_x, big_left_top_y, big_right_bottom_x, big_right_bottom_y, width_of_tile,
                            height_of_tile):
    # Create a new top-level window
    padConstant = 30
    window = Toplevel(padx=padConstant, pady=padConstant)
    window.title("")
    positionstr = "+" + '{:.0f}'.format((width / 2 - padConstant * 3)) + "+" + '{:.0f}'.format(
        (height / 2 - padConstant * 3))
    print(positionstr)
    window.geometry(positionstr)

    # Create a StringVar for each question
    flammable_var = StringVar(window)
    flammable_var.set("Yes")  # default value
    walkable_var = StringVar(window)
    walkable_var.set("Yes")  # default value
    color_var = StringVar(window)
    color_var.set("dim grey")  # default value

    # Create a label and dropdown menu for each question
    flammable_label = Label(window, text="Are the tiles flammable?")
    flammable_label.pack()
    flammable_options = ["Yes", "No"]
    flammable_dropdown = OptionMenu(window, flammable_var, *flammable_options)
    flammable_dropdown.pack()

    walkable_label = Label(window, text="Are the tiles walkable?")
    walkable_label.pack()
    walkable_options = ["Yes", "No"]
    walkable_dropdown = OptionMenu(window, walkable_var, *walkable_options)
    walkable_dropdown.pack()

    color_label = Label(window, text="Select area color: ")
    color_label.pack()
    color_options = ["dim gray", "lime green", "maroon", "yellow", "coral", "pink"]
    color_dropdown = OptionMenu(window, color_var, *color_options)
    color_dropdown.pack()

    # Create a function to be called when the button is clicked
    def on_button_click():
        global tempFlammable, tempWalkable, tempColor
        print("Selected options:", flammable_var.get(), walkable_var.get(), color_var.get())
        tempFlammable = flammable_var.get()
        tempWalkable = walkable_var.get()
        tempColor = color_var.get()
        print("set global variables")
        print(tempColor)
        window.destroy()
        further_process(big_left_top_x, big_left_top_y, big_right_bottom_x, big_right_bottom_y, width_of_tile,
                        height_of_tile)

    # Create an "OK" button
    button = Button(window, text="OK", command=on_button_click)
    button.pack()

    window.mainloop()


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
    global rect_start_x, rect_start_y, big_rectangle_id
    # Get the coordinates of the selected region
    rect_end_x = my_canvas.canvasx(event.x)
    rect_end_y = my_canvas.canvasy(event.y)

    # Perform actions based on the selected region
    selected_region_start = (rect_start_x, rect_start_y)
    selected_region_end = (rect_end_x, rect_end_y)

    # print("Selected Region Start:", selected_region_start)
    # print("Selected Region End:", selected_region_end)

    left_top_x = selected_region_start[0]
    left_top_y = selected_region_start[1]

    right_bottom_x = selected_region_end[0]
    right_bottom_y = selected_region_end[1]

    right_top_x, right_top_y, left_bottom_x, left_bottom_y = calculate_rt_and_lb_coordinates(left_top_x, left_top_y,
                                                                                             right_bottom_x,
                                                                                             right_bottom_y)

    # print(left_top_x, left_top_y)
    # print(right_top_x, right_top_y)
    # print(left_bottom_x, left_bottom_y)
    # print(right_bottom_x, right_bottom_y)

    x = left_top_x
    y = left_top_y
    width_of_tile = width / divisions
    height_of_tile = height / divisions

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

    new_rectangle = Rectangle(big_left_top_x, big_left_top_y, big_right_top_x, big_right_top_y, big_left_bottom_x,
                              big_left_bottom_y, big_right_bottom_x, big_right_bottom_y)

    flag = True

    if len(all_rectangles) == 0:
        pass
        # all_rectangles.append(new_rectangle)
        # my_canvas.create_rectangle(big_left_top_x, big_left_top_y, big_right_bottom_x,
        #                            big_right_bottom_y, fill="blue")
        # ask_if_flammable()
    else:
        for rectangle in all_rectangles:
            if rectangles_overlap(rectangle.get_coords(), new_rectangle.get_coords()):
                pass
                # let the user know about the overlap
                print("invalid")
                flag = False
                break
            else:
                print("valid")
    if flag:
        all_rectangles.append(new_rectangle)
        # my_canvas.create_rectangle(big_left_top_x, big_left_top_y, big_right_bottom_x,
        #                           big_right_bottom_y, fill="blue")
        # thread1 = thread(f"name{big_rectangle_id}", big_rectangle_id, big_left_top_x, big_left_top_y,
        # big_right_bottom_x, big_right_bottom_y,
        # width_of_tile, height_of_tile)
        # thread1.start()
        ask_the_three_questions(big_left_top_x, big_left_top_y, big_right_bottom_x, big_right_bottom_y, width_of_tile,
                                height_of_tile)
        # big_left_top_x, big_left_top_y, big_right_bottom_x, big_right_bottom_y, width_of_tile, height_of_tile):

        # tempFlammable = None
        # tempWalkable = None
        # def dialog(var):
        #    root2 = Tk()
        #    box = Frame(root2)
        #    question = Label(box, text = "Is the material " +  var + "?")
        #    def yes():
        #        temp = True
        #    def no():
        #        temp = False

        #    yButton = Button(box, text = "Yes", command = yes)
        #    nButton = Button(box, text = "False", command = no)

        # userInput = (simpledialog.askstring(title='Is material flammable', prompt = "Yes or No?"))


def rectangles_overlap(rect1, rect2):
    # Rectangles are represented as (x1, y1, x2, y2), where (x1, y1) is the top-left corner,
    # and (x2, y2) is the bottom-right corner.
    print(rect1)
    print(rect2)
    x1_rect1, y1_rect1, x2_rect1, y2_rect1 = rect1
    x1_rect2, y1_rect2, x2_rect2, y2_rect2 = rect2

    # Check for non-overlapping conditions
    if x2_rect1 - 1 < x1_rect2 or x2_rect2 < x1_rect1 + 1 or y2_rect1 - 1 < y1_rect2 or y2_rect2 < y1_rect1 + 1:
        return False
    else:
        return True


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
draw_grid_on_canvas(my_canvas, width, height, divisions)
container.mainloop()
