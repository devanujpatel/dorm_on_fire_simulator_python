from tkinter import *

root = Tk()
root.title("Learn To Code")
root.iconbitmap('c:/')

button_quit = Button(root, text = "Exit Program", command = root.quit)
button_quit.pack()

root.mainloop()
