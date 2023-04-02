import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from tkcalendar import DateEntry
import datetime
from datetime import date

# mysql connection
con = mysql.connector.connect(
user = "root",
password = "",
host = "localhost",
database = "login_register")
# This is just a connection
cursor = con.cursor()

#To centerialize the tkinter window
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
root.title("Register Page")
#root.configure(background="grey")

# mysql SELECT
def submit():
    full_name_ch = full_name.get()
    user_ch = username.get()
    passw_ch = password.get()
    con_pass_ch = confirm_password.get()
    mob_no_ch = mob_no.get()
    date_ch = date_dob.get()
    if full_name_ch == "" or user_ch == "" or passw_ch == "" or con_pass_ch == "" or mob_no_ch == "" or date_ch == "":
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
    cursor.execute(f"SELECT `user_name` FROM `login_register_table` WHERE `user_name`='{user_ch}'")
    if cursor.fetchall(): # checking if something found with this username
        messagebox.showinfo('Message','Username already exists please choose another Username')
    elif age < 15:
        messagebox.showinfo('Message','Your Age should be greater than 15 for registration')
    elif not full_name_ch.isalpha():
        messagebox.showinfo('Message','No Digits are allowed in Name')
    elif not passw_ch == con_pass_ch:
         messagebox.showinfo('Message','Confirm Password does not match entered Password')
    elif not mob_no_ch.isdigit():
        messagebox.showinfo('Message','Only Digits allowed in Mobile No. field')
    elif not len(mob_no_ch) == 10:
        messagebox.showinfo('Message','Please re=enter your Mobile No.')
    else:
        try:
            query = """INSERT INTO `login_register_table` (ID,real_name,user_name,user_pass,mobile_no,dob) VALUES (NULL,%s,%s,%s,%s,%s)"""
            cursor.execute(query,(full_name_ch,user_ch,passw_ch,mob_no_ch,date_ch))
            messagebox.showinfo('Message','Registration successful')

        except:
                con.rollback()
                messagebox.showinfo('Message','Error Occured')



l1=Label(root,text='Register Page',bg='black',fg='white',font=("New Times Roman", 25,))
l1.pack(fill=X,ipady=10)



l3=Label(root,text="Name :",fg="black",font=("bold",15))
l3.place(x=135,y=70)
full_name=Entry(root)
full_name.place(x=250,y=75)

l1=Label(root,text='Username :',fg='black',font=("bold", 15))
l1.place(x=100,y=120)
username=Entry(root)
username.place(x=250,y=125)

l2=Label(root,text='Password :',fg='black',font=("bold", 15))
l2.place(x=100,y=170)
password=Entry(root,show="*")
password.place(x=250,y=175)

l2=Label(root,text='Confirm Password :',fg='black',font=("bold", 15))
l2.place(x=30,y=220)
confirm_password=Entry(root,show="*")
confirm_password.place(x=250,y=225)

l2=Label(root,text='Mobile No. :',fg='black',font=("bold", 15))
l2.place(x=100,y=270)
mob_no=Entry(root)
mob_no.place(x=250,y=275)

l2=Label(root,text='Date of Birth :',fg='black',font=("bold", 15))
l2.place(x=85,y=320)
date_dob = DateEntry(root,date_pattern='yyyy-mm-dd',state='readonly',width=12,background='darkblue', foreground='white')
date_dob.place(x=250,y=325)

main_btn_register = Button(root, text='Submit',width=10,command=submit,font=("bold", 15))
main_btn_register.place(x=70,y=370)

main_window_btn = Button(root, text='Back to Main Page',width=15,command=submit,font=("bold", 15))
main_window_btn.place(x=230,y=370)

root.mainloop()
