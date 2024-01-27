# should be in a seperate thread and keep on changing the weights everywhere
import threading
import time
import pickle

f = open("temp_for_file_name.txt", "r")
dat_name = f.read()
print(dat_name)
f.close()

all_tiles_list = None
all_tiles_dict = None

with open(dat_name, "rb") as file:
    data = pickle.load(file)
    all_tiles_list = data["list"]
    all_tiles_dict = data["dictionary"]

exit_coordinates = []
for tile in all_tiles_list:
    if tile.color == "maroon":
        exit_coordinates.append([tile.x, tile.y])

with open("exits.dat", "wb") as exits:
    pickle.dump(exit_coordinates, exits)



# Define a function that will be executed in the new thread
def my_function():
    for neighbour in dataset


# Create a new thread
my_thread = threading.Thread(target=my_function, name='MyThread')

# Start the thread
my_thread.start()
