# Connector import for c=able to connect to database
import mysql.connector
#Import from tkinter module
import tkinter as tk
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
#Import from car_Main.py
from car_Main import center_window

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
center_window(500,240)
root.title("Login Page")
#root.configure(background="grey")



def submit():
    user_ch = username.get()
    passw_ch = password.get()
    if len(user_ch) == 0 or len(passw_ch) == 0:
        messagebox.showinfo('Message',"All Fields must be filled")
    query = """SELECT * FROM `login_register_table`
               WHERE `user_name` = %s AND `user_pass` = %s
            """
    cursor.execute(query,(user_ch,passw_ch))
    r = cursor.fetchall()
    if r:
        print("Query Executed successfully")
        messagebox.showinfo('Message','Login Successful')
    else:
        con.rollback()
        print("Invalid Username or Password")

def register():
    root.destroy()
    import main_page2




l1=Label(root,text='Login Page',bg='black',fg='white',font=("New Times Roman", 25,))
l1.pack(fill=X,ipady=10)

fm1=Frame(root)
fm1.pack(pady=10)
fm2=Frame(root)
fm2.pack(pady=20)
fm3=Frame(root)
fm3.pack(pady=0)


l1=Label(fm1,text='Username :',fg='black',font=("bold", 15))
l1.pack(side=LEFT)
username=Entry(fm1)
username.pack(padx=20)

l2=Label(fm2,text='Password :',fg='black',font=("bold", 15))
l2.pack(side=LEFT)
password=Entry(fm2,show="*")
password.pack(padx=20)

b1 = Button(fm3, text='Login',width=10,command=submit,font=("bold", 15))
b1.pack(side=LEFT,padx=20)



root.mainloop()
