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

def back():
    root.destroy()
    import car_Main


root = tk.Tk()
center_window(800,400)
root.title("Car Rental")

#Main Label
car_display_head = Label(root,text='Car Availabe',bg='black',fg='white',font=("New Times Roman", 25,))
car_display_head.pack(fill=X,ipady=10)

#Button to Back to Main Page
car_display_head = Button(root,text='<- Back to Main Page',command=back,font=("New Times Roman", 10,))
car_display_head.place( x=50,y=20)

# Welcome Label
x = "Hello"
car_display_welcome = Label(root,text="Welcome, {}".format(x),bg='black',fg='white',font=("New Times Roman", 15,))
car_display_welcome.place( x=600,y=15)

#Main Frame
frame_display = Frame(root,highlightthickness=1,highlightbackground="black")
frame_display.pack(pady=10,fill=X,side=TOP)
frame_display.pack_propagate(0)

#Inside Frame for Image
frame_display_in = Frame(frame_display)
frame_display_in.pack(pady=10,fill=X,side=RIGHT,anchor=NE)
frame_display_in.pack_propagate(0)

# Car Brand Label
l3=Label(frame_display,text="Brand :",fg="black",font=("bold",20))
l3.grid(row = 0, column = 0, sticky = E)

# Car Brand Info Label
lbl_brand=Label(frame_display,fg="black",font=("bold",20))
lbl_brand.grid(row=0,column = 1)

# Car Name Label
l3=Label(frame_display,text="Name :",fg="black",font=("bold",20))
l3.grid(row = 1, column = 0, sticky = E)

# Car Name Info Label
lbl_name=Label(frame_display,fg="black",font=("bold",20))
lbl_name.grid(row=1,column = 1)

# Car Plate Label
l3=Label(frame_display,text="License Plate :",fg="black",font=("bold",20))
l3.grid(row = 2, column = 0, sticky = E)

# Car Plate Info Label
lbl_plate=Label(frame_display,fg="black",font=("bold",20))
lbl_plate.grid(row=2,column = 1)

# Car Seat No. Label
l3=Label(frame_display,text="Seat No:",fg="black",font=("bold",20))
l3.grid(row = 3, column = 0, sticky = E)

# Car Seat No. Unfo Label
lbl_seat_no=Label(frame_display,fg="black",font=("bold",20))
lbl_seat_no.grid(row=3,column = 1)

# Car Color Label
l3=Label(frame_display,text="Colour :",fg="black",font=("bold",20))
l3.grid(row = 4, column = 0, sticky = E)

# Car Color Info Label
lbl_color=Label(frame_display,fg="black",font=("bold",20))
lbl_color.grid(row=4,column = 1)

# Car query to give ID for number of cars
query1 = "SELECT `ID` FROM `rental_car_details`"
cursor.execute(query1)
r1 = cursor.fetchall()
result = []

for t in r1:
    for x in t:
        result.append(x)
t1 = result

id = t1[0]

#Display Info of Car function
def display(id):

    # Car Query 2 to display all cars details
    query = "SELECT * FROM `rental_car_details` WHERE `ID`= %d"%id
    cursor.execute(query)
    r = cursor.fetchall()

    # To  make the tuple into list
    for t in r:
        t = list(t)

        # Making Image fit
        entry_path = t[6]
        entry_pic = entry_path
        my_pic = Image.open(entry_pic)
        #Resize image
        resized = my_pic.resize((280,180), Image.ANTIALIAS)
        new_pic = ImageTk.PhotoImage(resized)
        #To not collect the new img while throwing old image

        # Car Brand Info
        lbl_brand.configure(text=t[1])
        # Car Name Info
        lbl_name.configure(text=t[2])
        # Car Plate Info
        lbl_plate.configure(text=t[3])
        # Car Seat No, Info
        lbl_seat_no.configure(text=t[4])
        # Car Color Info
        lbl_color.configure(text=t[5])


        # Image Frame
        lbl_img=Label(frame_display_in,image=new_pic,fg="black",borderwidth=2, relief="groove")
        lbl_img.grid(row = 0, column =5, sticky = E,padx=100)


        lbl_img.image = new_pic


def rent():
    print(id)


#Rent Button to call booking fucntion
btn_Rent = Button(frame_display,text="RENT NOW",command=rent)
btn_Rent.grid(row=6,column=3,pady=15)

display(id)

index = 0

#Button increase function
def increase():
    global id
    global index
    len_1 = len(t1)
    index = index + 1
    id = t1[index]

    if not id == t1[0] :
        b1.place(x=300,y=350)
    if id == t1[len_1 - 1]:
        b2.place_forget()
    display(id)

# Button decrease function
def decrease():
    global id
    global index
    len_2 = len(t1)
    index = index - 1
    id = t1[index]

    if id == t1[0] :
        b1.place_forget()
    if not id == t1[len_2 - 1]:
        b2.place(x=450,y=350)
    display(id)

# Backward Button
b1 = Button(root,text="<",width=10,command=decrease)
b1.place(x=300,y=350)
b1.place_forget()

# Forward Button
b2 = Button(root,text=">",width=10,command=increase)
b2.place(x=450,y=350)
root.mainloop()
