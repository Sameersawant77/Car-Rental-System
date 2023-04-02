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
import time

# mysql connection = Login and Register part
con5 = mysql.connector.connect(
user = "root",
password = "",
host = "localhost",
database = "login_register")
# This is just a connection = Login and Register part
image_cursor = con5.cursor()

root = tk.Tk()
#C:/Users/kunal/Desktop/car_images/bmw.png
root.title('Download')
def insert():
    ID = ety1.get()
    query2 = "SELECT * FROM login_register_table WHERE user_name = '{0}'"
    image_cursor.execute(query2.format(str(ID)))
    MyResult = image_cursor.fetchone()[7]
    StoreFilePath = "C:/Users/kunal/Desktop/img{0}.png".format(ID)

    with open(StoreFilePath, "wb") as File:
        File.write(MyResult)
        File.close()



lbl = Label(root,text="Image ID :")
lbl.pack(pady=10,padx=10)
ety1 = Entry(root)
ety1.pack(pady=10,padx=10)
btn1 = Button(root,text="ID",command=insert)
btn1.pack(pady=10,padx=10)

root.mainloop()
