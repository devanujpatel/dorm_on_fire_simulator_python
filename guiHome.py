from tkinter import *

root = Tk()
root.title('Dorm On Fire Simulator')
width = root.winfo_screenwidth()  # width of screen
height = root.winfo_screenheight()  # height of screen
root.winfo_toplevel().geometry("%dx%d%+d%+d" % (width, height, 0, 0))

rootHeight = root.winfo_height()
rootWidth = root.winfo_width()
# Say you want it to be 20 pixels smaller
frame = Frame(root, height=rootHeight - 10, width=rootWidth - 10)
frame.pack()

# all the frames stored
newMapFrame = None
existingPlansFrame = None

# temporary variables
tempName = None
e = None


def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()


def newMap():
    root.destroy()


def preloaded():
    frame.destroy()
    existingPlansFrame = Frame(root, height=rootHeight - 10, width=rootWidth - 10)
    existingPlansFrame.pack()
    root.destroy()
    import preexistingMaps


# Buttons
myButton = Button(frame, text="Create New Map", padx=50, pady=50, command=newMap)
myButton.pack()

myButton2 = Button(frame, text="Load Existing Map", padx=50, pady=50, command=preloaded)
myButton2.pack()

root.mainloop()
