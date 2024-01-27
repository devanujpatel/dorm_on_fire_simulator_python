from tkinter import *
import os
import glob

root = Tk()
root.title("")

width = root.winfo_screenwidth()  # width of screen
height = root.winfo_screenheight()  # height of screen
root.winfo_toplevel().geometry("%dx%d%+d%+d" % (width, height, 0, 0))

rootHeight = root.winfo_height()
rootWidth = root.winfo_width()
# Say you want it to be 20 pixels smaller
frame = Frame(root, height=rootHeight - 10, width=rootWidth - 10)
frame.pack()
n = StringVar(frame)


def on_button_click():
    frame.destroy()
    f = open("temp_for_file_name.txt", "w")
    f.write(n.get())
    f.close()
    root.destroy()
    import reading_building_plan


def listOfExisting():
    # Create a StringVar for each question
    var = StringVar(frame)
    var.set("")  # default value

    var_label = Label(frame, text="Pre-existing Maps")
    var_label.pack()
    try:
        # Get the current working directory
        current_directory = os.getcwd()

        dat_files = glob.glob(os.path.join(current_directory, '*.dat'))
        dat_file_names = [os.path.basename(file) for file in dat_files]
        print(dat_file_names)
        var_options = dat_file_names
        n.set(var_options[0])
        var_dropdown = OptionMenu(frame, n, *var_options)
        var_dropdown.pack()
        button = Button(frame, text="OK", command=on_button_click)
        button.pack()
    except Exception as e:
        print(f"Error: {e}")


listOfExisting()

root.mainloop()
