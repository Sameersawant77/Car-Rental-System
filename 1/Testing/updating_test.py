
# importing everything from tkinter
from tkinter import *

# creating the tkinter window
Main_window = Tk()

# variable
my_text = "GeeksforGeeks updated !!!"

# function define for
# updating the my_label
# widget content
def counter():

    # use global variabel
    global my_text

    # configure
    my_label.config(text = my_text)

# create a button widget and attached
# with counter function
my_button = Button(Main_window,
                   text = "Please update",
                   command = counter)

# create a Label widget
my_label = Label(Main_window,
                 text = "geeksforgeeks")

# place the widgets
# in the gui window
my_label.pack()
my_button.pack()

# Start the GUI
Main_window.mainloop()
