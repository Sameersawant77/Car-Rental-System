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
database = "image")
# This is just a connection = Login and Register part
image_cursor = con5.cursor()

root = tk.Tk()
#C:/Users/kunal/Desktop/car_images/bmw.png
root.title('Insert')
def insert():
    FilePath = ety1.get()
    with open(FilePath, 'rb') as File:
        BinaryData = File.read()
    query = "INSERT INTO image_data (ID,image) VALUES (NULL,%s)"
    image_cursor.execute(query, (BinaryData, ))



lbl = Label(root,text="Filepath :")
lbl.pack(pady=10,padx=10)
ety1 = Entry(root)
ety1.pack(pady=10,padx=10)
btn1 = Button(root,text="Add Image",command=insert)
btn1.pack(pady=10,padx=10)

root.mainloop()
