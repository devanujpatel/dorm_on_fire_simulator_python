from tkinter import *

root = Tk()
root.title('Dorm On Fire Simulator')
width = root.winfo_screenwidth()  # width of screen
height = root.winfo_screenheight()  # height of screen
root.winfo_toplevel().geometry("%dx%d%+d%+d" % (width, height, 0, 0))

rootHeight = root.winfo_height()
rootWidth = root.winfo_width()

# Frame to contain the buttons
frame = Frame(root, height=rootHeight - 10, width=rootWidth - 10)
frame.pack()

button_font = ("Futura", 24)


# all the frames stored
newMapFrame = None
existingPlansFrame = None

# temporary variables
tempName = None
e = None

# Button for the project label (non-clickable)
projectButton = Button(frame, text="Dorm On Fire Simulation (DOFS)", font=("Futura", 30, "bold"),
                       state=DISABLED, padx=100, pady=90)
projectButton.pack(pady=80)


def newMap():
    root.destroy()
    import edit_building_plan
def preloaded():
    frame.destroy()
    existingPlansFrame = Frame(root, height=rootHeight - 10, width=rootWidth - 10)
    existingPlansFrame.pack()
    # drop = ttk.Combobox(existingPlansFrame, value = "     ", "      ")
    # drop.current(0)
def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()


# Buttons
myButton = Button(frame, text="Create New Map", font=button_font, padx=120, pady=80, command=newMap)  # Replace with your actual command
myButton.pack(side=LEFT, padx=(70,50), pady=(150, 10))

myButton2 = Button(frame, text="Load Existing Map",font=button_font, padx=120, pady=80, command=preloaded)  # Replace with your actual command
myButton2.pack(side=RIGHT, padx=(70,50), pady=(150, 10))

# Run the main loop
root.mainloop()
