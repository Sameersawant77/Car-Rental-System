import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from tkcalendar import DateEntry
import datetime
from datetime import date
from datetime import datetime
from PIL import ImageTk, Image
from dateutil.relativedelta import relativedelta

#--------- Databases -----------------------

# mysql connection = Login and Register part
con1 = mysql.connector.connect(
user = "root",
password = "",
host = "localhost",
database = "login_register")
# This is just a connection = Login and Register part
login_register_cursor = con1.cursor()
# if (con1):
#     # Carry out normal procedure
#     print("Connection successful 1")
# else:
#     # Terminate
#     print("Connection unsuccessful 1")

# mysql connection = Rental Car part
con2 = mysql.connector.connect(
user = "root",
password = "",
host = "localhost",
database = "rental_car")
# This is just a connection
rental_car_cursor = con2.cursor()
# if (con2):
#     # Carry out normal procedure
#     print("Connection successful 2 ")
# else:
#     # Terminate
#     print("Connection unsuccessful 2")

#---------------------------------------------


#-------- Main Window -----------------------
root = tk.Tk()
#---------------------------------------------

#------- To make window of GUI CENTER --------
def center_window(w, h, ws, hs):
    # get screen width and height
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    return ('%dx%d+%d+%d' % (w, h, x, y))
#---------------------------------------------

#-------- Main window dimensions -------------
root.geometry(center_window(450,420,root.winfo_screenwidth(),root.winfo_screenheight()))
#---------------------------------------------

# test

# ----

#-------- Car Booking / Payment code Code -----------------

#y1 = username y2 = CAR_ID
def car_Booking(y1,y2):
    y1 = y1
    y2 = y2
    def booking_db():
        booking_query = """INSERT INTO `car_booking` (ID,user_name,car_id,start_date,end_date,bill_detail) VALUES (NULL,%s,%s,%s,%s,%s)"""
        rental_car_cursor.execute(booking_query,(y1,y2,calpick_start,caldrop_end,msg))
        messagebox.showinfo('Message','Booking Successful')
        payment_Window.destroy()
        root.deiconify()

    def final_payment():
        booking_db()
    def payment(x_pay):

        #No of Total Days
        z = x_pay

        #To Get all the car details
        payment_query = "SELECT * FROM `rental_car_details` WHERE `ID` = %d"%y2
        rental_car_cursor.execute(payment_query)
        pay = rental_car_cursor.fetchall()



        result = []

        for t in pay:
            for x5 in t:
                result.append(x5)
        t1 = result

        # Price calculations
        z1 = z*t1[7]
        print(t1[7])

        #To get current Time
        now_time = datetime.now()
        #To get current Date
        today_date = date.today()

        global payment_Window
        payment_Window = Toplevel(root)
        payment_Window.title("Bill Details")
        payment_Window.geometry(center_window(300,250,root.winfo_screenwidth(),root.winfo_screenheight()))

        def on_closing_payment():
            payment_Window.destroy()
            root.deiconify()

        global msg


        msg = """Username : {}\nTime :{}\nDate of Booking :{}\nPickUp Date :{}\nDropOff Date :{}\nAmount to be paid : Rs {}\nCar Info Below
                \nCar Brand :{}\nCar Name :{}\nCar Plate No :{}\nCar Seat No :{}\nCar Color :{}
                """.format(y1,now_time,today_date,calpick_start,caldrop_end,z1,t1[1],t1[2],t[3],t[4],t[5])
        #msg2= "Hello"
        T = Text(payment_Window, height = 7, width = 34)
        header_label = Label(payment_Window, text="Bill Receipt", bg='black', fg='white', font=("New Times Roman", 25,))
        header_label.pack(fill=X)
        l = Label(payment_Window,text="Bill Details",font=("New Times Roman",10))
        l2 = Label(payment_Window,text="*Payment must be paid in cash by customer")
        b1 = Button(payment_Window,text="Complete Payment",command=final_payment)
        l.pack()
        T.pack()
        l2.pack()
        b1.pack(pady=5)
        T.insert(tk.END, msg)
        T.config(state=DISABLED)

        payment_Window.protocol("WM_DELETE_WINDOW", on_closing_payment)


    # To only allow to select from week of dates
    week = date.today() + relativedelta(days=+7)
    # To allow not to select previous dates
    today = date.today() + relativedelta(days=+1)

    root.withdraw()

    booking_Window = Toplevel(root)
    booking_Window.title("Book a Car")
    booking_Window.geometry(center_window(400,200,root.winfo_screenwidth(),root.winfo_screenheight()))

    def p(calpick, caldrop):
            global caldrop_end
            global calpick_start
            caldrop_end = caldrop.get_date()
            calpick_start = calpick.get_date()

            result = caldrop.get_date() - calpick.get_date()
            lst = str(result)
            lst = lst.split()
            if lst[0] == '0:00:00':
                global total_days
                noOfDays = 1
                total_days = noOfDays
                #booked_popup(total_days)
                if messagebox.askokcancel("Are you Sure", "Do you want to move to billing page?"):
                    payment(total_days)
                    booking_Window.withdraw()



            else:
                noOfDays = int(lst[0])
                # if noOfDays < 1:
                #     popup_1()
                if noOfDays > 0:
                    total_days = noOfDays + 1
                    if messagebox.askokcancel("Are you Sure", "Do you want to move to billing page?"):
                        payment(total_days)
                        booking_Window.withdraw()

    def back_to_display():
        booking_Window.destroy()
        car_Display(y1)


    # def booked_popup(total_days):
    #     response = messagebox.showinfo("Thank You!",
    #                                    "Your booking is successful for {} days and Total amount to be paid is {}\n\nThank You!".format(
    #                                        total_days, total_days * 2000))

    header_label = Label(booking_Window, text="Book Car", bg='black', fg='white', font=("New Times Roman", 25,))
    header_label.pack(fill=X)
    pickUp = Label(booking_Window, text="PICK-UP DATE", bg='grey', fg='white')
    pickUp.place(x=60, y=55)
    calPick = DateEntry(booking_Window, width=12, background='darkblue', foreground='white', borderwidth=2,
                        date_pattern='yyyy-mm-dd',mindate=today,maxdate=week)
    calPick.place(x=60, y=75)
    dropOff = Label(booking_Window, text='DROP-OFF DATE', bg='grey', fg='white')
    dropOff.place(x=230, y=55)
    calDrop = DateEntry(booking_Window, width=12, background='darkblue', foreground='white', borderwidth=2,
                        date_pattern='yyyy-mm-dd',mindate=today,maxdate=week)
    calDrop.place(x=230, y=75)
    btnOk = Button(booking_Window, text="BOOK", height=2, width=10, command=lambda: p(calPick, calDrop))
    btnOk.place(x=250, y=120)

    btn_back_display = Button(booking_Window,text="Back to Display",height=2,width=15,command=back_to_display)
    btn_back_display.place(x=50,y=120)
#-------------------------------------------

#--------- Car Adding Code -----------------
def car_Adder(x):

    x2 = x

    car_Adder_Window = Toplevel(root)
    car_Adder_Window.title("Car Adder")
    car_Adder_Window.geometry(center_window(700,300,root.winfo_screenwidth(),root.winfo_screenheight()))

    def on_closing_adder():
        car_Adder_Window.destroy()
        car_Display(x2)

    def car_Adding_Submit():
        ety_car_brand_get = ety_car_brand.get()
        ety_car_name_get = ety_car_name.get()
        ety_car_plate_get =  ety_car_plate.get()
        ety_car_seat_get = ety_car_seat.get()
        ety_car_color_get = ety_car_color.get()
        entry_path_get = ety_car_img.get()
        ety_car_price_get = ety_car_price.get()
        entry_pic_get = absolute_path+entry_path_get+extension_of_path

        # try:
        query_add ="""INSERT INTO `rental_car_details` (`ID`, `car_brand`, `car_name`, `car_plate_no`, `car_no_seats`, `car_color`, `car_img`,`car_price`) VALUES (NULL,%s,%s,%s,%s,%s,%s,%s)"""
        rental_car_cursor.execute(query_add,(ety_car_brand_get,ety_car_name_get,ety_car_plate_get,ety_car_seat_get,ety_car_color_get,entry_pic_get,ety_car_price_get))

        messagebox.showinfo("Successful", "Successfully added to database")
        on_closing_adder()

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
        global ety_car_price


        frame_adding_1 = Frame(car_Adder_Window,borderwidth=2, relief="groove")
        frame_adding_1.pack(side=LEFT,expand=1,fill=BOTH)

        frame_adding_2 = Frame(car_Adder_Window)
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

        #car car_price
        lbl_car_price = Label(frame_adding_1,text="Price :",fg="black",font=("bold",10))
        lbl_car_price.grid(row = 6, column = 0, padx=5, pady=5, sticky=E)
        ety_car_price = Entry(frame_adding_1)
        ety_car_price.grid(row=6, column = 1, padx=5, pady=5)

        #car Image
        lbl_car_image = Label(frame_adding_1,text="Image name :",fg="black",font=("bold",10))
        lbl_car_image.grid(row=5 , column=0, pady=10, padx=0)

        lbl_car_img = Label(frame_adding_2,image=default_pic,borderwidth=2, relief="groove")
        lbl_car_img.grid(row=0,column=0,pady=10,padx=10)

        ety_car_img = Entry(frame_adding_1,width=20)
        ety_car_img.grid(row=5,column=1,padx=10,pady=10)

        btn_img = Button(frame_adding_2,text="Click to Add Image",command=addThis,anchor=CENTER)
        btn_img.grid(pady=10,padx=10)

        btn_main = Button(frame_adding_1,text="Add to database",command=car_Adding_Submit,anchor=CENTER)
        btn_main.grid(row=7,column=0,padx=10,pady=2)

    car_Adder_Window.protocol("WM_DELETE_WINDOW", on_closing_adder)

    car_add()
#-------------------------------------------

#-------- Car Display Code ------------------
def car_Display(x):
    #print(x)

    #Another variable to have it : x is The logged in username
    x1 = x
    root.withdraw()

    display_Window = Toplevel(root)
    display_Window.geometry(center_window(800,400,root.winfo_screenwidth(),root.winfo_screenheight()))
    display_Window.title("Car Display")

    def back():
        display_Window.destroy()
        root.deiconify()

    #
    #Main Label
    car_display_head = Label(display_Window,text='Car Availabe',bg='black',fg='white',font=("New Times Roman", 25,))
    car_display_head.pack(fill=X,ipady=10)

    #Button to Back to Main Page
    car_display_head = Button(display_Window,text='<- Back to Main Page',command=back,font=("New Times Roman", 10,))
    car_display_head.place( x=50,y=20)

    # Welcome Label
    car_display_welcome = Label(display_Window,text="Welcome, {}".format(x),bg='black',fg='white',font=("New Times Roman", 15,))
    car_display_welcome.place( x=600,y=15)

    #Main Frame
    frame_display = Frame(display_Window,highlightthickness=1,highlightbackground="black")
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

    # Car Price label
    l3_price=Label(frame_display,text="Price Per Day:",fg="black",font=("blod",20))
    l3_price.grid(row = 5, column =0, sticky = E)

    # Car Price Info label
    l4_price=Label(frame_display,fg="black",font=("bold",20))
    l4_price.grid(row = 5, column = 1)

    # Car query to give ID for number of cars
    query_car_id = "SELECT `ID` FROM `rental_car_details` WHERE `ID` NOT IN (SELECT `car_id` FROM `car_booking`)"
    rental_car_cursor.execute(query_car_id)
    r1 = rental_car_cursor.fetchall()
    result = []

    for t in r1:
        for x in t:
            result.append(x)
    t1 = result


    global CAR_ID
    CAR_ID = t1[0]

    #Display Info of Car function
    def display(CAR_ID):

        # Car Query 2 to display all cars details
        query_car_display = "SELECT * FROM `rental_car_details` WHERE `ID`= %d"%CAR_ID
        rental_car_cursor.execute(query_car_display)
        r2 = rental_car_cursor.fetchall()

        # To  make the tuple into list
        for t in r2:
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
            # Car Price Info
            l4_price.configure(text=t[7])

            # Image Frame
            lbl_img=Label(frame_display_in,image=new_pic,fg="black",borderwidth=2, relief="groove")
            lbl_img.grid(row = 0, column =5, sticky = E,padx=100)


            lbl_img.image = new_pic


    # Booking Window functions
    def rent():
        display_Window.destroy()
        car_Booking(x1,CAR_ID)

    def car_Adder_call():
        display_Window.destroy()
        car_Adder(x1)

    def already_booked():

        def close_booked():
            booked_Window.destroy()

        booked_Window = Toplevel(root)
        booked_Window.geometry(center_window(300,200,root.winfo_screenwidth(),root.winfo_screenheight()))
        booked_Window.title("Booking Details")
        query_booked_bill = f"SELECT `bill_detail` FROM `car_booking` WHERE `user_name`='{x1}'"
        rental_car_cursor.execute(query_booked_bill)
        booked = rental_car_cursor.fetchall()
        result_2 = []

        for t_2 in booked:
            for x6 in t_2:
                result_2.append(x6)
        t1_booked = result_2


        T = Text(booked_Window, height = 7, width = 34)

        l = Label(booked_Window,text="Bill Details",font=("New Times Roman",10))

        b1 = Button(booked_Window,text="OK",command=close_booked)
        l.pack()
        T.pack()

        b1.pack(pady=15)
        i = 1
        if len(t1_booked)>1:
            while (i <= len(t1_booked)):
                T.insert(tk.END, t1_booked[i-1])
                T.insert(tk.END, "\n")
                i = i + 1
        else:
            T.insert(tk.END, t1_booked[0])
        T.config(state=DISABLED)

    #To hide the rent button if login in as guest
    def btn_Rent_disabled():
        if x1 == "Guest":
            btn_Rent.grid_forget()
        elif x1 =="admin":
            print("Hello admin")
            btn_adding = Button(display_Window,text="< Add Car >",command=car_Adder_call)
            btn_adding.place(x=200,y=365)
            btn_booked = Button(display_Window,text="See Booking Detail ->",command=already_booked)
            btn_booked.place(x=600,y=365)
            btn_Rent.grid(row=6,column=3,pady=15)
        else:
            rental_car_cursor.execute(f"SELECT `user_name` FROM `car_booking` WHERE `user_name`='{x1}'")
            if rental_car_cursor.fetchall():
                btn_booked = Button(display_Window,text="See Booking Detail ->",command=already_booked)
                btn_booked.place(x=600,y=365)
                btn_Rent.grid(row=6,column=3,pady=15)
            else:
                btn_Rent.grid(row=6,column=3,pady=15)


    #Rent Button to call booking fucntion
    btn_Rent = Button(frame_display,text="RENT NOW",command=rent)
    btn_Rent.grid(row=7,column=3,pady=15)
    btn_Rent.grid_forget()

    btn_adding = Button(frame_display,text="< ADD CAR >",command=rent)
    btn_adding.place(x=200,y=365)

    btn_Rent_disabled()

    # To call car display
    display(CAR_ID)

    global index
    index =0

    #Button increase function
    def increase():
        global CAR_ID
        global index

        len_1 = len(t1)
        index = index + 1
        CAR_ID = t1[index]

        if not CAR_ID == t1[0] :
            b1.place(x=300,y=365)
        if CAR_ID == t1[len_1 - 1]:
            b2.place_forget()
        display(CAR_ID)

    # Button decrease function
    def decrease():
        global CAR_ID
        global index
        len_2 = len(t1)
        index = index - 1
        CAR_ID = t1[index]

        if CAR_ID == t1[0] :
            b1.place_forget()
        if not CAR_ID == t1[len_2 - 1]:
            b2.place(x=450,y=365)
        display(CAR_ID)

    # Backward Button
    b1 = Button(display_Window,text="<",width=10,command=decrease)
    b1.place(x=300,y=365)
    b1.place_forget()

    # Forward Button
    b2 = Button(display_Window,text=">",width=10,command=increase)
    b2.place(x=450,y=365)
    if len(t1) == 1:
         b2.place_forget()
    # Adding car button

    btn_adding.place_forget()

#--------------------------------------------

#-------- Change Password -------------------

def change_password():

    def back_to_login():
        chg_pass_Window.destroy()
        login_code()

    def check_chg_pass():
        check_chg_pass_usnm = ety_usnm.get()
        check_chg_pass_dob = ety_dob.get()
        check_chg_pass_PASS = ety_chg_pass.get()
        check_chg_pass_PASS_CONF = ety_chg_pass_conf.get()


        if check_chg_pass_usnm == "" or check_chg_pass_PASS == "" or check_chg_pass_PASS_CONF == "":
            messagebox.showinfo('Error','Fill all the fields')
        elif not check_chg_pass_PASS == check_chg_pass_PASS_CONF:
            messagebox.showinfo('Error','Password should match Confirm Password')
        #Check if username and dob matchs
        else:
            query_check_chg_pass = "SELECT * FROM login_register_table WHERE user_name = %s AND dob = %s"

            login_register_cursor.execute(query_check_chg_pass,(check_chg_pass_usnm,check_chg_pass_dob,))
            r = login_register_cursor.fetchall()
            if r:
                # Password update function
                query_chg_pass = "UPDATE login_register_table SET user_pass = %s WHERE user_name = %s"
                login_register_cursor.execute(query_chg_pass,(check_chg_pass_PASS,check_chg_pass_usnm,))
                messagebox.showinfo('Successful','Password have been successful changed')
                chg_pass_Window.destroy()
                login_code()
            else:
                messagebox.showinfo('Error','Invalid Username or Date of Birth')

    global ety_usnm
    global ety_dob
    global ety_chg_pass
    global ety_chg_pass_conf

    chg_pass_Window = Toplevel(root)
    chg_pass_Window.title("Change Password")
    chg_pass_Window.geometry(center_window(350,180,root.winfo_screenwidth(),root.winfo_screenheight()))

    # Enter username lbl
    lbl_usnm = Label(chg_pass_Window,text="Enter your Username :",font=("bold", 12))
    lbl_usnm.place(x=30,y=5)

    # Enter username ety
    ety_usnm = Entry(chg_pass_Window)
    ety_usnm.place(x=200,y=8)

    # Choose date of birth lbl
    lbl_dob = Label(chg_pass_Window,text="Choose your Date of Birth :",font=("bold", 12))
    lbl_dob.place(x=5,y=35)

    # Choose date of birth ety
    ety_dob = DateEntry(chg_pass_Window,date_pattern='yyyy-mm-dd',state='readonly',width=17,background='darkblue', foreground='white')
    ety_dob.place(x=200,y=38)

    # Enter new pass lbl
    lbl_chg_pass = Label(chg_pass_Window,text="Enter your New Password :",font=("bold", 12))
    lbl_chg_pass.place(x=5,y=65)

    # Enter new pass ety
    ety_chg_pass = Entry(chg_pass_Window,show='*')
    ety_chg_pass.place(x=200,y=68)

    # Enter pass conf lbl
    lbl_chg_pass_conf = Label(chg_pass_Window,text="Confirm Password :",font=("bold", 12))
    lbl_chg_pass_conf.place(x=40,y=95)

    # Ener pass conf ety
    ety_chg_pass_conf = Entry(chg_pass_Window,show='*')
    ety_chg_pass_conf.place(x=200,y=98)

    # CHnage pass confirm
    chg_pass_btn = Button(chg_pass_Window,text="Submit",command=check_chg_pass,font=("bold", 12))
    chg_pass_btn.pack(side=RIGHT,pady=10,anchor=SE,padx=50)

    # Back to login page
    chg_pass_login = Button (chg_pass_Window,text="Back to Login Page",command=back_to_login,font=("bold",12))
    chg_pass_login.pack(side=LEFT,pady=10,padx=20,anchor=SE)

#--------------------------------------------

#-------- Login Code -------------------------
def login_code():
    #To hide the main Window
    root.withdraw()

    login_Window = Toplevel(root)
    login_Window.geometry(center_window(500,300,root.winfo_screenwidth(),root.winfo_screenheight()))
    login_Window.title("Login Page")
    #root.configure(background="grey")

    # Login Function
    def login_submit():
        USER_CH = username.get()        # MAIN PART (REQUIRED IN AHEAD FUCNTIONS)
        passw_ch = password.get()
        # To check if all fields are filled
        if USER_CH=="" or passw_ch =="":
            messagebox.showinfo('Message','Fill all the fields')
        else:
            query = """SELECT * FROM `login_register_table`
                       WHERE `user_name` = %s AND `user_pass` = %s
                    """
            login_register_cursor.execute(query,(USER_CH,passw_ch))
            r = login_register_cursor.fetchall()
            if r:
                print("Query Executed successfully")
                messagebox.showinfo('Message','Login Successful')
                # login_register_cursor.close()
                login_Window.destroy()
                # Car query to give ID for number of cars
                query_car_id = "SELECT `ID` FROM `rental_car_details` WHERE `ID` NOT IN (SELECT `car_id` FROM `car_booking`)"
                rental_car_cursor.execute(query_car_id)
                r1 = rental_car_cursor.fetchall()
                if not r1:

                    empty_Window = Toplevel(root)
                    empty_Window.title("No Car Availabe")
                    empty_Window.geometry(center_window(300,200,root.winfo_screenwidth(),root.winfo_screenheight()))

                    def already_booked_2():

                        def close_booked():
                            booked_Window.destroy()

                        booked_Window = Toplevel(root)
                        booked_Window.geometry(center_window(300,200,root.winfo_screenwidth(),root.winfo_screenheight()))
                        query_booked_bill = f"SELECT `bill_detail` FROM `car_booking` WHERE `user_name`='{USER_CH}'"
                        rental_car_cursor.execute(query_booked_bill)
                        booked = rental_car_cursor.fetchall()
                        result_2 = []

                        for t_2 in booked:
                            for x6 in t_2:
                                result_2.append(x6)
                        t1_booked = result_2
                        #print(len(t1_booked))

                        T = Text(booked_Window, height = 7, width = 34)

                        l = Label(booked_Window,text="Bill Details",font=("New Times Roman",10))

                        b1 = Button(booked_Window,text="OK",command=close_booked)
                        l.pack()
                        T.pack()

                        b1.pack(pady=15)
                        T.insert(tk.END, t1_booked[0])
                        T.config(state=DISABLED)

                    l_1 = Label(empty_Window,text="No Car Availabe fot this week, Sorry For inconvience")
                    l_1.pack(pady=10)

                    def empty_main():
                        empty_Window.destroy()
                        root.deiconify()

                    rental_car_cursor.execute(f"SELECT `user_name` FROM `car_booking` WHERE `user_name`='{USER_CH}'")
                    if rental_car_cursor.fetchall():
                        btn_booked = Button(empty_Window,text="See Booking Detail ->",command=already_booked_2)
                        btn_booked.pack(pady=10)
                        btn_main_page = Button(empty_Window,text="Back to Main Page",command=empty_main)
                        btn_main_page.pack(pady=10)
                    else:
                        btn_main_page = Button(empty_Window,text="Back to Main Page")
                        btn_main_page.pack(pady=10)

                else:
                    car_Display(USER_CH)


            else:
                con1.rollback()
                messagebox.showinfo('Message','Invalid Username or Password')

    # Message box when force closing
    def on_closing_login():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            login_Window.destroy()
            root.deiconify()

    # Back to Main Page function
    def main_page_login():
        login_Window.destroy()
        root.deiconify()

    # Login Big Label
    l1=Label(login_Window,text='Login Page',bg='black',fg='white',font=("New Times Roman", 25,))
    l1.pack(fill=X,ipady=10)

    # Login = Username label and button
    l1=Label(login_Window,text='Username :',fg='black',font=("bold", 15))
    l1.place(x=70,y=80)
    username=Entry(login_Window)
    username.place(x=250,y=85)

    # Login = Passowrd Label and Button
    l2=Label(login_Window,text='Password :',fg='black',font=("bold", 15))
    l2.place(x=70,y=130)
    password=Entry(login_Window,show="*")
    password.place(x=250,y=135)

    # Login = Call fucntion to check if users able to login
    b1 = Button(login_Window, text='Login',width=10,command=login_submit,font=("bold", 15))
    b1.place(x=70,y=240)

    # Login = Back to Main Page
    b2 = Button(login_Window, text='Back to Main Page',width=15,command=main_page_login,font=("bold", 15))
    b2.place(x=250,y=240)

    def change_password_go():
        login_Window.destroy()
        change_password()

    # Login =  For got password button
    b3 =  Button(login_Window, text="Forgot Password",width=15,command=change_password_go,font=("bold",10))
    b3.place(x=180,y=190)

    login_Window.protocol("WM_DELETE_WINDOW", on_closing_login)
#---------------------------------------------


#-------- Registration Code ------------------
def register_code():

    #To hide the main Window
    root.withdraw()

    register_Window = Toplevel(root)

    register_Window.geometry(center_window(450,480,root.winfo_screenwidth(),root.winfo_screenheight()))
    register_Window.title("Register Page")
    #root.configure(background="grey")

    #Registration Button function
    def register_submit():
        full_name_ch = full_name.get()
        user_ch = username.get()
        passw_ch = password.get()
        con_pass_ch = confirm_password.get()
        mob_no_ch = mob_no.get()
        date_ch = date_dob.get()
        address_ch = t_address.get(1.0, "end-1c")
        # No Field should be empty
        if full_name_ch == "" or user_ch == "" or passw_ch == "" or con_pass_ch == "" or mob_no_ch == "" or date_ch == "" or address_ch =="":
            messagebox.showinfo('Message','Fill all the fields')
        #------ Age calculation ----

        year= date_ch[:4]
        month = date_ch[5:7]
        day = date_ch[8:]
        today = date.today()
        # getting birthdate using .get() method
        birthDate = date(int(year),int(month),int(day))
        # calculating age by subtracting birthdate from today's date
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

        # ------ Age calculation Above --------

        # to check if username already exist in database
        login_register_cursor.execute(f"SELECT `user_name` FROM `login_register_table` WHERE `user_name`='{user_ch}'")
        if login_register_cursor.fetchall(): # checking if something found with this username
            messagebox.showinfo('Message','Username already exists please choose another Username')
        # Age should be above 15 checker
        elif age < 15:
            messagebox.showinfo('Message','Your Age should be greater than 15 for registration')
        # Name should only be alphabet
        elif not full_name_ch.isalpha():
            messagebox.showinfo('Message','No Digits are allowed in Name')
        # Password should match Confirm Password
        elif not passw_ch == con_pass_ch:
             messagebox.showinfo('Message','Confirm Password does not match entered Password')
        # Mobile No should be only digits
        elif not mob_no_ch.isdigit():
            messagebox.showinfo('Message','Only Digits allowed in Mobile No. field')
        # Len of Mobile No should be 10
        elif not len(mob_no_ch) == 10:
            messagebox.showinfo('Message','Mobile No should be only 10 digits')
        else:
            #Inset data into database
            try:
                query = """INSERT INTO `login_register_table` (ID,real_name,user_name,user_pass,mobile_no,dob,address) VALUES (NULL,%s,%s,%s,%s,%s,%s)"""
                login_register_cursor.execute(query,(full_name_ch,user_ch,passw_ch,mob_no_ch,date_ch,address_ch,))
                messagebox.showinfo('Message','Registration successful')
                register_Window.destroy()
                root.deiconify()
            # If error occurs in connection
            except:
                    con1.rollback()
                    messagebox.showinfo('Message','Error Occured')

    # Message box when force closing
    def on_closing_register():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            register_Window.destroy()
            root.deiconify()

    # Back to Main Page button Function
    def main_page_register():
        register_Window.destroy()
        root.deiconify()

    # Register Big Label
    l1=Label(register_Window,text='Register Page',bg='black',fg='white',font=("New Times Roman", 25,))
    l1.pack(fill=X,ipady=10)


    # Name field for register window
    l3=Label(register_Window,text="Name :",fg="black",font=("bold",15))
    l3.place(x=135,y=70)
    full_name=Entry(register_Window)
    full_name.place(x=250,y=75)

    # Username field for register window
    l1=Label(register_Window,text='Username :',fg='black',font=("bold", 15))
    l1.place(x=100,y=120)
    username=Entry(register_Window)
    username.place(x=250,y=125)

    # Password field for register window
    l2=Label(register_Window,text='Password :',fg='black',font=("bold", 15))
    l2.place(x=100,y=170)
    password=Entry(register_Window,show="*")
    password.place(x=250,y=175)

    # Confirm Password field for register window
    l2=Label(register_Window,text='Confirm Password :',fg='black',font=("bold", 15))
    l2.place(x=30,y=220)
    confirm_password=Entry(register_Window,show="*")
    confirm_password.place(x=250,y=225)

    # Mobile No field for register window
    l2=Label(register_Window,text='Mobile No. :',fg='black',font=("bold", 15))
    l2.place(x=100,y=270)
    mob_no=Entry(register_Window)
    mob_no.place(x=250,y=275)

    # Date Entry field for register window
    l2=Label(register_Window,text='Date of Birth :',fg='black',font=("bold", 15))
    l2.place(x=85,y=320)
    date_dob = DateEntry(register_Window,date_pattern='yyyy-mm-dd',state='readonly',width=17,background='darkblue', foreground='white')
    date_dob.place(x=250,y=325)

    # Adress Entry field for register window
    lbl_address = Label(register_Window,text="Address :",width=10,fg='black',font=("bold", 15))
    lbl_address.place(x=100,y=375)
    t_address = tk.Text(register_Window, width=20, height=3)
    t_address.place(x=250,y=375)


    # Submit Button for register window
    main_btn_register = Button(register_Window, text='Submit',width=10,command=register_submit,font=("bold", 15))
    main_btn_register.place(x=70,y=435)

    # Back to Main page Button
    main_window_btn = Button(register_Window, text='Back to Main Page',width=15,command=main_page_register,font=("bold", 15))
    main_window_btn.place(x=230,y=435)

    register_Window.protocol("WM_DELETE_WINDOW", on_closing_register)
#---------------------------------------------

#-------- Main Code --------------------------
root.title("Car Rental")


main_lbl_head = Label(root,text='Car Rental System',bg='black',fg='white',font=("New Times Roman", 25,))
main_lbl_head.pack(fill=X,ipady=10)


main_frame = Frame(root,highlightthickness=1,highlightbackground="black")
main_frame.pack(pady=20,padx=20,expand=1)

#Guest Button Code
def guest():
    g = "Guest"
    car_Display(g)


def empty():
    empty = Label(main_frame)
    empty.pack(pady=12)

#Main window part ========== Guest Label and Button part
main_btn_guest = Button(main_frame,text="Guest",width=8,command=guest,font=("New Times Roman", 15,))
main_btn_guest.pack(pady=5)

main_lbl_guest = Label(main_frame,text="                 If you just want to Broswe, click above                 ",font=("New Times Roman", 10,))
main_lbl_guest.pack(pady=2)

empty()

#Main window part ========== Login Label and Button part
main_btn_login = Button(main_frame,text="Login",command=login_code,width=8,font=("New Times Roman", 15,))
main_btn_login.pack(pady=5)

main_lbl_login = Label(main_frame,text="If already have a account, click above",font=("New Times Roman", 10,))
main_lbl_login.pack(pady=2)

empty()

#Main window part ========== Register Label and Button part
main_btn_register = Button(main_frame,text="Register",width=8,command=register_code,font=("New Times Roman", 15,))
main_btn_register.pack(pady=5)

main_lbl_register = Label(main_frame,text="Want to create a account, click above",font=("New Times Roman", 10,))
main_lbl_register.pack(pady=2)

empty()
#---------------------------------------------


root.mainloop()
