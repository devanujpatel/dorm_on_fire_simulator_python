import pickle

with open("mckeldin.dat", "rb") as file:
    loaded_data = pickle.load(file)
    # print(loaded_data["list"])
    # print(loaded_data["dictionary"])
    # for x in loaded_data["dictionary"]:
    #     for y in loaded_data["dictionary"][x]:
    #         if loaded_data["dictionary"][x][y] is not None:
    #             print(loaded_data["dictionary"][x][y].x, loaded_data["dictionary"][x][y].y, loaded_data["dictionary"][x][y].color)
    print("   --- -- - - -- ")
    for tile in loaded_data["list"]:
        print(tile.x, tile.y, tile.cost_imposed_on_weight)