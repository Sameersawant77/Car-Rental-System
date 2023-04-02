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
    if not full_name_ch.isalpha():
        messagebox.showerror('Only letters','Only letters are allowed in Name !')
        full_name.delete(0,"END")




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
l3.grid(row = 0, column = 0, sticky = W)
full_name=Entry(fm1)
full_name.grid(row = 0, column = 1, sticky = E)

l1=Label(fm2,text='Username :',fg='black',font=("bold", 15))
l1.grid(row = 0, column = 0, sticky = W)
username=Entry(fm2)
username.grid(row = 0, column = 1, sticky = E)

l2=Label(fm3,text='Password :',fg='black',font=("bold", 15))
l2.grid(row = 0, column = 0, sticky = W)
password=Entry(fm3,show="*")
password.grid(row = 0, column = 1, sticky = W)

l2=Label(fm4,text="Confirm Password :",fg='black',font=("bold", 15))
l2.grid(row = 0, column = 0, sticky = 'w')
confirm_password=Entry(fm4,show="*")
confirm_password.grid(row = 0, column = 1, sticky = W)

l2=Label(fm5,text='Mobile No. :',fg='black',font=("bold", 15))
l2.grid(row = 0, column = 0, sticky = W)
mob_no=Entry(fm5,show="*")
mob_no.grid(row = 0, column = 1, sticky = W)

l2=Label(fm6,text='Date of Birth :',fg='black',font=("bold", 15))
l2.grid(row = 0, column = 0, sticky = W)
date_dob = DateEntry(fm6,date_pattern='yyyy-mm-dd',width=12,background='darkblue', foreground='white')
date_dob.delete(0, "end")
date_dob.grid(row = 0, column = 1, sticky = W)

Button(fm7, text='Submit',width=10,command=submit,font=("bold", 15)).pack()


root.mainloop()
