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
center_window(450,500)
root.title("Main Page")
root.configure(background="grey")

#Page Header
l1=Label(root,text='Car Rental Service',bg='black',fg='white',font=("New Times Roman", 25,))
l1.pack(fill=X,ipady=10)

fm1=Frame(root,background="grey")
fm1.pack(pady=20,)
fm2=Frame(root)
fm2.pack(pady=20)
fm3=Frame(root)
fm3.pack(pady=0)

#Browse as Guest
b1 = Button(fm1, text='Browse As A Guest',width=20,command="",font=("bold", 15))
b1.grid(row = 0, column = 0, sticky = N,pady=5)
l2=Label(fm1,text='If new to this and would like to browse then select above option',font=("New Times Roman", 10,))
l2.grid(row = 1, column = 0, sticky = S,pady=5)
#Login
b1 = Button(fm2, text='Login',width=10,command="",font=("bold", 15))
b1.grid(row = 0, column = 0, sticky = N)
l2=Label(fm2,text='If new to this and would like to browse then select above option',font=("New Times Roman", 10,))
l2.grid(row = 1, column = 0, sticky = S,pady=5)
#Register
b1 = Button(fm3, text='Register',width=10,command="",font=("bold", 15))
b1.grid(row = 0, column = 0, sticky = N)
l2=Label(fm3,text='If new to this and would like to browse then select above option',font=("New Times Roman", 10,))
l2.grid(row = 1, column = 0, sticky = S,pady=5)



root.mainloop()
