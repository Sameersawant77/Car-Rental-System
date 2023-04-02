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

# INSERT INTO `rental_car_details` (`ID`, `car_brand`, `car_name`, `car_plate_no`, `car_no_seats`, `car_color`, `car_img`)
#  VALUES (NULL, 'Maruti Dzire', 'Swift', 'KA19P8488', '4', 'blue', 'sw');

def car_Adding_Submit():
    ety_car_brand_get = ety_car_brand.get()
    ety_car_name_get = ety_car_name.get()
    ety_car_plate_get =  ety_car_plate.get()
    ety_car_seat_get = ety_car_seat.get()
    ety_car_color_get = ety_car_color.get()
    entry_path_get = ety_car_img.get()
    entry_pic_get = absolute_path+entry_path_get+extension_of_path

    # try:
    query ="""INSERT INTO `rental_car_details` (`ID`, `car_brand`, `car_name`, `car_plate_no`, `car_no_seats`, `car_color`, `car_img`) VALUES (NULL,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(query,(ety_car_brand_get,ety_car_name_get,ety_car_plate_get,ety_car_seat_get,ety_car_color_get,entry_pic_get))
    # except:
    #     con.rollback()
    #     messagebox.showinfo('Message','Error Occured')
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

#Default img to load at start
absolute_path = "C://Users//kunal//Desktop//car_images//"
default_img = "no_image"
extension_of_path = ".png"

default_path = absolute_path+default_img+extension_of_path
im = Image.open(default_path)
default_pic = im.resize((280,180), Image.ANTIALIAS)
default_pic = ImageTk.PhotoImage(default_pic)

def addThis():
    #To get image name

    try:
        entry_path = ety_car_img.get()
        entry_pic = absolute_path+entry_path+extension_of_path
        my_pic = Image.open(entry_pic)

        #Resize image
        resized = my_pic.resize((280,180), Image.ANTIALIAS)

        new_pic = ImageTk.PhotoImage(resized)
        lbl_car_img.configure(image=new_pic)
        #To not collect the new img while throwing old image
        lbl_car_img.image = new_pic

    except:
        messagebox.showinfo("Error Occured", "Wrong Image name")

def car_add():

    global ety_car_img
    global lbl_car_img

    global ety_car_brand
    global ety_car_name
    global ety_car_plate
    global ety_car_seat
    global ety_car_color


    #Making A toplevel window
    top_Window = Toplevel(root)
    #top_Window.geometry('700x500')
    top_Window.title("Car adding")

    frame_adding_1 = Frame(top_Window,borderwidth=2, relief="groove")
    frame_adding_1.pack(side=LEFT,expand=1,fill=BOTH)

    frame_adding_2 = Frame(top_Window)
    frame_adding_2.pack(side=RIGHT,expand=1,fill=BOTH)

    #car brand
    lbl_car_brand = Label(frame_adding_1,text="Brand :",fg="black", font=("bold",10))
    lbl_car_brand.grid(row = 0, column = 0, padx=5, pady=5, sticky=E)
    ety_car_brand = Entry(frame_adding_1)
    ety_car_brand.grid(row = 0, column = 1, padx=5, pady=5)

    #car Name
    lbl_car_name = Label(frame_adding_1,text="Name :",fg="black",font=("bold",10))
    lbl_car_name.grid(row = 1, column = 0, padx=5, pady=5, sticky=E)
    ety_car_name = Entry(frame_adding_1)
    ety_car_name.grid(row = 1, column = 1, padx=5, pady=5)

    #car plate
    lbl_car_plate = Label(frame_adding_1,text="License Plate :",fg="black",font=("bold",10))
    lbl_car_plate.grid(row = 2, column = 0, padx=5, pady=5, sticky=E)
    ety_car_plate = Entry(frame_adding_1)
    ety_car_plate.grid(row = 2, column = 1, padx=5, pady=5)

    #car seat no
    lbl_car_seat = Label(frame_adding_1,text="Seat No :",fg="black",font=("bold",10))
    lbl_car_seat.grid(row = 3, column = 0, padx=5, pady=5, sticky=E)
    ety_car_seat = Entry(frame_adding_1)
    ety_car_seat.grid(row = 3, column = 1, padx=5, pady=5)

    #car color
    lbl_car_color = Label(frame_adding_1,text="Colour :",fg="black",font=("bold",10))
    lbl_car_color.grid(row = 4, column = 0, padx=5, pady=5, sticky=E)
    ety_car_color = Entry(frame_adding_1)
    ety_car_color.grid(row = 4, column = 1, padx=5, pady=5)

    #car Image
    lbl_car_image = Label(frame_adding_1,text="Image name :",fg="black",font=("bold",10))
    lbl_car_image.grid(row=5 , column=0, pady=10, padx=30)

    lbl_car_img = Label(frame_adding_2,image=default_pic,borderwidth=2, relief="groove")
    lbl_car_img.grid(row=0,column=0,pady=10,padx=10)

    ety_car_img = Entry(frame_adding_1,width=20)
    ety_car_img.grid(row=5,column=1,padx=10,pady=10)

    btn_img = Button(frame_adding_2,text="Click to Add Image",command=addThis,anchor=CENTER)
    btn_img.grid(pady=10,padx=10)

    btn_main = Button(frame_adding_1,text="Add to database",command=car_Adding_Submit,anchor=CENTER)
    btn_main.grid(row=6,column=0,padx=10,pady=2)

car_add = Button(root, text='Add',width=10,command=car_add,font=("bold", 15)).grid(pady=10)


root.mainloop()
