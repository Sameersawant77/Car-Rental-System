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
center_window(450,250)
root.title("Register Page")

cursor.execute("SELECT * FROM login_register_table limit 0,10")
e=Label(root,width=10,text='ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=0)
e=Label(root,width=10,text='Real Name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=1)
e=Label(root,width=10,text='Username',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=2)
e=Label(root,width=10,text='Password',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=3)
e=Label(root,width=10,text='Mobile_no',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=4)
e=Label(root,width=10,text='Date',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=5)
i=1
for login_register_table in cursor:
    for j in range(len(login_register_table)):
        e = Label(root, width=10, fg='blue',text=login_register_table[j],borderwidth=2,relief='ridge', anchor="w")
        e.grid(row=i, column=j)
        #e.insert(END, login_register_table[j])
    i=i+1






root.mainloop()
#root.configure(background="grey")
