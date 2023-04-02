# Connector import for c=able to connect to database
import mysql.connector
#Import from tkinter module
import tkinter as tk
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
#Import from center_window
from center_Window import center_window

# mysql connection
con = mysql.connector.connect(
user = "root",
password = "",
host = "localhost",
database = "login_register")
# This is just a connection
cursor = con.cursor()


root = tk.Tk()
root.geometry(center_window(500,240,root.winfo_screenwidth(),root.winfo_screenheight()))
root.title("Login Page")
#root.configure(background="grey")



def submit():
    USER_CH = username.get()
    passw_ch = password.get()
    if USER_CH=="" or passw_ch =="":
        messagebox.showinfo('Message','Fill all the fields')
    else:
        query = """SELECT * FROM `login_register_table`
                   WHERE `user_name` = %s AND `user_pass` = %s
                """
        cursor.execute(query,(USER_CH,passw_ch))
        r = cursor.fetchall()
        if r:
            print("Query Executed successfully")
            messagebox.showinfo('Message','Login Successful')
            cursor.close()
        else:
            con.rollback()
            messagebox.showinfo('Message','Invalid Username or Password')

def main_page_login():
    root.destroy()
    import car_Main

l1=Label(root,text='Login Page',bg='black',fg='white',font=("New Times Roman", 25,))
l1.pack(fill=X,ipady=10)



l1=Label(root,text='Username :',fg='black',font=("bold", 15))
l1.place(x=70,y=80)
username=Entry(root)
username.place(x=250,y=85)

l2=Label(root,text='Password :',fg='black',font=("bold", 15))
l2.place(x=70,y=130)
password=Entry(root,show="*")
password.place(x=250,y=135)

b1 = Button(root, text='Login',width=10,command=submit,font=("bold", 15))
b1.place(x=70,y=180)

b2 = Button(root, text='Back to Main Page',width=15,command=main_page,font=("bold", 15))
b2.place(x=250,y=180)


root.mainloop()
