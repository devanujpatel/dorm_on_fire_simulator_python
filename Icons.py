from tkinter import *

root = Tk()
root.title("Learn To Code")
root.iconbitmap('c:/')
button_font = ("Futura", 12)

button_quit = Button(root, text = "Exit Program", font = button_font, command = root.quit)
button_quit.pack()

root.mainloop()
