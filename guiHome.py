from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Dorm On Fire Simulator')
width = root.winfo_screenwidth()  # width of screen
height = root.winfo_screenheight()  # height of screen
root.winfo_toplevel().geometry("%dx%d%+d%+d" % (width, height, 0, 0))

rootHeight = root.winfo_height()
rootWidth = root.winfo_width()
# Say you want it to be 20 pixels smaller
frame = Frame(root, height=rootHeight-10, width=rootWidth-10)
frame.pack()

newMapFrame = None
existingPlansFrame = None

def newMap():
    frame.destroy()
    newMapFrame = Frame(root, height=rootHeight-10, width=rootWidth-10)
    newMapFrame.pack()

def preloaded():
    frame.destroy()
    existingPlansFrame = Frame(root, height=rootHeight-10, width=rootWidth-10)
    existingPlansFrame.pack()
    #drop = ttk.Combobox(existingPlansFrame, value = "     ", "      ")
    #drop.current(0)

#Buttons
myButton = Button(frame, text = "Create New Map", padx = 50, pady = 50, command = newMap)
myButton.pack()

myButton2 = Button(frame, text = "Load Existing Map", padx = 50, pady = 50, command = preloaded)
myButton2.pack()



root.mainloop()
