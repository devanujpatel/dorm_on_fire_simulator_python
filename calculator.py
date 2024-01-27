from _ast import Lambda
from tkinter import * # adding all import; all are widgets

root = Tk()
#Buttons
root.title("simple calculator")


entryWidget = Entry(root, width = 50, borderwidth=5)
entryWidget.grid(row = 0, column = 1, columnspan = 3, padx = 10, pady = 9)

def button_add(number):
    entryWidget.delete(0,END)
    entryWidget.insert(0,number)
button_1 = Button(root, text = "1", padx = 10, pady = 5, command = lambda: button_add(1))
button_2 = Button(root, text = "2", padx = 10, pady = 5, command = lambda: button_add(2))
button_3 = Button(root, text = "3", padx = 10, pady = 5, command = lambda: button_add(3))
button_4 = Button(root, text = "4", padx = 10, pady = 5, command = lambda: button_add(4))
button_5 = Button(root, text = "5", padx = 10, pady = 5, command = lambda: button_add(5))
button_6 = Button(root, text = "6", padx = 10, pady = 5, command = lambda: button_add(6))
button_7 = Button(root, text = "7", padx = 10, pady = 5, command = lambda: button_add(7))
button_8 = Button(root, text = "8", padx = 10, pady = 5, command = lambda: button_add(8))
button_9 = Button(root, text = "9", padx = 10, pady = 5, command = lambda: button_add(9))
button_0 = Button(root, text = "0", padx = 10, pady = 5, command = lambda: button_add(0))
button_add = Button(root, text = "+", padx = 39, pady = 20, command = lambda: button_add())
button_clear = Button(root, text = "CLEAR", padx = 39, pady = 20, command = lambda: button_add())
button_equal = Button(root, text = "=", padx = 39, pady = 20, command = lambda: button_add())

#put buttons on screen correctly

button_1.grid(row = 3,column = 0)
button_2.grid(row = 3,column = 1)
button_3.grid(row = 3,column = 2)
button_4.grid(row = 2,column = 0)
button_5.grid(row = 2,column = 1)
button_6.grid(row = 2,column = 2)
button_7.grid(row = 1,column = 0)
button_8.grid(row = 1,column = 1)
button_9.grid(row = 1,column = 2)
button_0.grid(row = 4,column = 0)
button_clear.grid(row = 4, column = 1, columnspan=2)
button_add.grid(row=5,column = 0)
button_equal.grid(row = 5, column = 1, columnspan=2)


#entryWidget.insert(0, "Enter Name:")





#def myClick():
    #myLabel = Label(root,text = "hello " + entryWidget.get())
   # myLabel.pack() #must get called
#myButton = Button(root, text = "Name?", padx = 50, pady = 80, command = myClick, fg = "red" , bg = "#000000") #no paranthesis!
#myButton.pack()






#making label widget

#myLabel = Label(root,text="Hello").grid(row=0, column = 0) # can also just slap on the end!
#myLabel2 = Label(root,text="Hello Yerrr")
#myLabel3 = Label(root, text = "WHYYY")

#need to add packet now

#myLabel.grid(row = 9, column = 0) #does not give a lot of control, grid is better!
#myLabel2.grid(row = 0, column = 1) # since relative, the column/row doesnt change
#myLabel3.grid(row = 0, column = 2)
root.mainloop() #used to constantly loop and print
