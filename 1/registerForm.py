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



    try:
        query = """INSERT INTO `login_register_table` (ID,real_name,user_name,user_pass,mobile_no,dob) VALUES (NULL,%s,%s,%s,%s,%s)"""
        cursor.execute(query,(full_name_ch,user_ch,passw_ch,mob_no_ch,date_ch))

    except:
            con.rollback()
            messagebox.showinfo('Message','Error Occured')


l1=Label(root,text='Register Page',bg='black',fg='white',font=("New Times Roman", 25,))
l1.pack(fill=X,ipady=10)

fm1=Frame(root)
fm1.pack(pady=10)
fm2=Frame(root)
fm2.pack(pady=10)
fm3=Frame(root)
fm3.pack(pady=10)
fm4=Frame(root)
fm4.pack(pady=10)
fm5=Frame(root)
fm5.pack(pady=10)
fm6=Frame(root)
fm6.pack(pady=10)
fm7=Frame(root)
fm7.pack(pady=0)

l3=Label(fm1,text="      Name :",fg="black",font=("bold",15))
l3.pack(side=LEFT)
full_name=Entry(fm1)
full_name.pack(padx=20)

l1=Label(fm2,text='Username :',fg='black',font=("bold", 15))
l1.pack(side=LEFT)
username=Entry(fm2)
username.pack(padx=20)

l2=Label(fm3,text='Password :',fg='black',font=("bold", 15))
l2.pack(side=LEFT)
password=Entry(fm3,show="*")
password.pack(padx=20)

l2=Label(fm4,text='Confirm Password :',fg='black',font=("bold", 15))
l2.pack(side=LEFT)
confirm_password=Entry(fm4,show="*")
confirm_password.pack(padx=0)

l2=Label(fm5,text='Mobile No. :',fg='black',font=("bold", 15))
l2.pack(side=LEFT)
mob_no=Entry(fm5,show="*")
mob_no.pack(padx=20)

l2=Label(fm6,text='Date of Birth :',fg='black',font=("bold", 15))
l2.pack(side=LEFT)
date_dob = DateEntry(fm6,date_pattern='yyyy-mm-dd',width=12,background='darkblue', foreground='white')
date_dob.pack(padx=10, pady=10)

Button(fm7, text='Submit',width=10,command=submit,font=("bold", 15)).pack()


root.mainloop()
