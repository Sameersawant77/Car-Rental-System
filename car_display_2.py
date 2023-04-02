import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from tkcalendar import DateEntry
import datetime
from PIL import ImageTk, Image

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
#center_window(450,420)
root.title("Car Rental")


def display():
    # lbl_1 = Label(z,text="Hi")
    # lbl_1.grid(row=0,column=1)
    # id_no = 3

    query = "SELECT * FROM `rental_car_details`"
    cursor.execute(query)
    r = cursor.fetchall()
    i = 1
    z = "frame_display_"+str(i)


    for t in r:
        t = list(t)
        z=Frame(root,highlightthickness=1,highlightbackground="black")
        z.pack(pady=10,fill=X,side=TOP)
        z.pack_propagate(0)

        entry_path = t[6]
        entry_pic = entry_path
        my_pic = Image.open(entry_pic)
        #Resize image
        resized = my_pic.resize((280,180), Image.ANTIALIAS)
        new_pic = ImageTk.PhotoImage(resized)
        #To not collect the new img while throwing old image



        l3=Label(z,text="Brand :",fg="black",font=("bold",10))
        l3.grid(row = 0, column = 0, sticky = E)

        l1=Label(z,text=t[1])
        l1.grid(row=0,column = 1)

        l3=Label(z,text="Name :",fg="black",font=("bold",10))
        l3.grid(row = 1, column = 0, sticky = E)

        l1=Label(z,text=t[2])
        l1.grid(row=1,column = 1)

        l3=Label(z,text="License Plate :",fg="black",font=("bold",10))
        l3.grid(row = 2, column = 0, sticky = E)

        l1=Label(z,text=t[3])
        l1.grid(row=2,column = 1)

        l3=Label(z,text="Seat No:",fg="black",font=("bold",10))
        l3.grid(row = 3, column = 0, sticky = E)

        l1=Label(z,text=t[4])
        l1.grid(row=3,column = 1)

        l3=Label(z,text="Colour :",fg="black",font=("bold",10))
        l3.grid(row = 4, column = 0, sticky = E)

        l1=Label(z,text=t[5])
        l1.grid(row=4,column = 1)



        lbl_img=Label(z,image=new_pic,fg="black",borderwidth=2, relief="groove",font=("bold",10))
        lbl_img.grid(row = 0, column =5, sticky = E,padx=100)


        lbl_img.image = new_pic
        i = i + 1
    messagebox.showinfo('Message','Connection Successful')

#[(3, 'Maruti Dzire', 'Swift', 'KA19P8488', 4, 'Blue', 'C://Users//kunal//Desktop//car_images//sw.png')]



display()


root.mainloop()
