import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

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
center_window(500,225)
root.title("Login Page")
#root.configure(background="grey")

# mysql SELECT

def submit():
    user_ch = username.get()
    passw_ch = password.get()
    print(f"The name entered by you is {user_ch} {passw_ch}")
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
        print("Error Occured")


l1=Label(root,text='Login Page',bg='black',fg='white',font=("New Times Roman", 25,))
l1.pack(fill=X,ipady=10)

fm1=Frame(root)
fm1.pack(pady=10)
fm2=Frame(root)
fm2.pack(pady=10)
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

Button(fm3, text='Submit',width=10,command=submit,font=("bold", 15)).pack()


root.mainloop()
