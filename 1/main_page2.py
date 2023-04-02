import tkinter as tk
from tkinter import ttk
from tkinter import *
import mysql.connector
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

#Function used to center the window
def center_window(w, h):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    return '%dx%d+%d+%d' % (w, h, x, y);
    # root.geometry('%dx%d+%d+%d' % (w, h, x, y))

#Tkinter main content
root = tk.Tk()
cal = center_window(1000,600)
root.geometry(cal)
root.title("CaR Rental System")
root.configure(background="grey")

#Header of the application
label_Title = Label(root, text="Car Rental Service", bg="black", fg='white',font=("Showcard Gothic", 30))
label_Title.pack(side=TOP, fill=X)

#Parent Tab
tab_parent = ttk.Notebook(root)

#Children Tab
tab_1 = ttk.Frame(tab_parent)
tab_2 = ttk.Frame(tab_parent)

#Parent to Children Tab connection
tab_parent.add(tab_1, text = "Start Page")

def unhide():
    tab_parent.add(tab_2, text= "Main Page")
    tab_parent.hide(tab_1)

def main_page_after_login():
    real_name_ch = 'Guest'
    tab_parent.add(tab_2, text= "Main Page")
    tab_parent.hide(tab_1)

    fm1=Frame(tab_2,background='blue')
    fm1.pack(side='top',expand=1,fill=BOTH)

    fm2=Frame(tab_2,background='white')
    fm2.pack(side='bottom',ipady=270,expand=1,fill=BOTH)

    l1 = Label(fm1, text='Welcome, '+real_name_ch,bg='grey',font=("New Times Roman",15,"bold"))
    l1.pack(side='right',pady=5,padx=10)

def guest():
    real_name_ch = 'Guest'
    tab_parent.add(tab_2, text= "Main Page")
    tab_parent.hide(tab_1)

    fm1=Frame(tab_2,background='grey')
    fm1.pack(side='top',expand=1,fill=BOTH)

    fm2=Frame(tab_2,background='white')
    fm2.pack(side='bottom',ipady=270,expand=1,fill=BOTH)

    l1 = Label(fm1, text='Welcome, '+real_name_ch,bg='grey',font=("New Times Roman",15,"bold"))
    l1.pack(side='right',pady=5,padx=10)

#Login Page
def login():
    #To hide the main Window
    root.withdraw()

    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)

    # sets the title of the
    # Toplevel widget
    # sets the geometry of toplevel
    cal2 = center_window(500,240)
    newWindow.geometry(cal2)
    newWindow.title("Login Page")

    #Login database
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
            main_page_after_login()
            root.deiconify()
        else:
            con.rollback()
            print("Invalid Username or Password")


    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            newWindow.destroy()
            root.deiconify()

    # widget of Toplevel
    l1=Label(newWindow,text='Login Page',bg='black',fg='white',font=("New Times Roman", 25,))
    l1.pack(fill=X,ipady=10)

    fm1=Frame(newWindow)
    fm1.pack(pady=10)
    fm2=Frame(newWindow)
    fm2.pack(pady=20)
    fm3=Frame(newWindow)
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

    #If window is closed by x mark
    newWindow.protocol("WM_DELETE_WINDOW", on_closing)

def register():

    #To hide the main Window
    root.withdraw()

    # Toplevel object which will
    # be treated as a new window
    newWindow2 = Toplevel(root)

    # sets the title of the
    # Toplevel widget
    # sets the geometry of toplevel
    cal3 = center_window(450,420)
    newWindow2.geometry(cal3)
    newWindow2.title("Register Page")

    #Tp code
    def submit():
        full_name_ch = full_name.get()
        user_ch = username.get()
        passw_ch = password.get()
        con_pass_ch = confirm_password.get()
        mob_no_ch = mob_no.get()
        date_ch = date_dob.get()


        if not full_name_ch.isalpha():
            messagebox.showerror('Only letters','Only letters are allowed in Name !')


        try:
            query = """INSERT INTO `login_register_table` (ID,real_name,user_name,user_pass,mobile_no,dob) VALUES (NULL,%s,%s,%s,%s,%s)"""
            cursor.execute(query,(full_name_ch,user_ch,passw_ch,mob_no_ch,date_ch))
            messagebox.showinfo('Message','Registration Successful')
            newWindow2.withdraw()
            root.deiconify()

        except:
                con.rollback()
                messagebox.showinfo('Message','Error Occured')

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            newWindow2.destroy()
            root.deiconify()

    l1=Label(newWindow2,text='Register Page',bg='black',fg='white',font=("New Times Roman", 25,))
    l1.pack(fill=X,ipady=10)

    fm1=Frame(newWindow2)
    fm1.pack(pady=10)
    fm2=Frame(newWindow2)
    fm2.pack(pady=10)
    fm3=Frame(newWindow2)
    fm3.pack(pady=10)
    fm4=Frame(newWindow2)
    fm4.pack(pady=10)
    fm5=Frame(newWindow2)
    fm5.pack(pady=10)
    fm6=Frame(newWindow2)
    fm6.pack(pady=10)
    fm7=Frame(newWindow2)
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
    mob_no=Entry(fm5)
    mob_no.grid(row = 0, column = 1, sticky = W)

    l2=Label(fm6,text='Date of Birth :',fg='black',font=("bold", 15))
    l2.grid(row = 0, column = 0, sticky = W)
    date_dob = DateEntry(fm6,date_pattern='yyyy-mm-dd',width=12,background='darkblue', foreground='white')
    date_dob.delete(0, "end")
    date_dob.grid(row = 0, column = 1, sticky = W)

    Button(fm7, text='Submit',width=10,command=submit,font=("bold", 15)).pack()

    newWindow2.protocol("WM_DELETE_WINDOW", on_closing)




#To hide the tab

# Start Page(Tab 1)
fm1=Frame(tab_1)
fm1.pack(pady=20)
l1 = Label(fm1,text="Welcome to Car Rental Service",font=("New Times Roman",15,"bold"))
l1.grid(column=0,row=0)

#Browse Directly
fm2=Frame(tab_1)
fm2.pack(pady=20)
b1 = Button(fm2,text="Login As Guest",command=guest,font=("bold",20))
b1.grid(column=0,row=0)
l2 = Label(fm2,text="If u just want to Browse click above",font=("New Times Roman",10,"bold"))
l2.grid(column=0,row=1)

#Login Button
fm3=Frame(tab_1)
fm3.pack(pady=20)
b2 = Button(fm3,text="Login",command=login,font=("bold",20))
b2.grid(column=0,row=0)
l3 = Label(fm3,text="Already have an account click above",font=("New Times Roman",10,"bold"))
l3.grid(column=0,row=1)

#Register Button
fm4=Frame(tab_1)
fm4.pack(pady=20)
b3 = Button(fm4,text="Register",command=register,font=("bold",20))
b3.grid(column=0,row=0)
l4 = Label(fm4,text="Want to create an account click above",font=("New Times Roman",10,"bold"))
l4.grid(column=0,row=1)

#Tab 2

#Browse Directly
# fm1=Frame(tab_2,background='grey')
# fm1.pack(side='top',ipady=20,expand=1,fill=BOTH)
#
# fm2=Frame(tab_2,background='white')
# fm2.pack(side='bottom',ipady=190,expand=1,fill=BOTH)
#










tab_parent.pack(expand=1,fill='both')

root.mainloop()
