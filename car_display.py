import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from tkcalendar import DateEntry
import datetime

# mysql connection
con = mysql.connector.connect(
user = "root",
password = "",
host = "localhost",
database = "rental_car")
# This is just a connection
cursor = con.cursor()

def center_window(w, h):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))




root = tk.Tk()
center_window(450,420)
root.title("Car Rental")


frame_display=Frame(root,highlightthickness=1,highlightbackground="black")
frame_display.pack(pady=10,fill=X,side=TOP)
def display():
    # lbl_1 = Label(frame_display,text)
    id_no = 4
    z = "a" + str(id_no)
    query = "SELECT * FROM `rental_car_details` WHERE ID="+str(id_no)
    cursor.execute(query)
    r = cursor.fetchall()
    if r:
        for t in r:
            t = list(t)
            t = t[1]
            print(t)
            print(z)
        print("Query Executed successfully")
        messagebox.showinfo('Message','Login Successful')

#[(3, 'Maruti Dzire', 'Swift', 'KA19P8488', 4, 'Blue', 'C://Users//kunal//Desktop//car_images//sw.png')]

l3=Label(frame_display,text="Brand :",fg="black",font=("bold",10))
l3.grid(row = 0, column = 0, sticky = E)

l3=Label(frame_display,text="Name :",fg="black",font=("bold",10))
l3.grid(row = 1, column = 0, sticky = E)

l3=Label(frame_display,text="License Plate :",fg="black",font=("bold",10))
l3.grid(row = 2, column = 0, sticky = E)

l3=Label(frame_display,text="Seat No:",fg="black",font=("bold",10))
l3.grid(row = 3, column = 0, sticky = E)

l3=Label(frame_display,text="Colour :",fg="black",font=("bold",10))
l3.grid(row = 4, column = 0, sticky = E)

l3=Label(frame_display,text="Image :",fg="black",borderwidth=2, relief="groove",font=("bold",10))
l3.grid(row = 0, column =5,rowspan=4, sticky = E)

display()


root.mainloop()
