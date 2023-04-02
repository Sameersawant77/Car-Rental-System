from tkcalendar import DateEntry
from datetime import date
import tkinter as tk
from dateutil.relativedelta import relativedelta
from tkinter import *
from tkinter import messagebox

week = date.today() + relativedelta(days=+7)
print(week)
today = date.today() + relativedelta(days=+1)
print(today)
root = tk.Tk()

def p(calpick, caldrop):
        result = caldrop.get_date() - calpick.get_date()
        lst = str(result)
        lst = lst.split()
        if lst[0] == '0:00:00':
            global total_days
            noOfDays = 1
            total_days = noOfDays
            booked_popup(total_days)
            root.destroy()
        else:
            noOfDays = int(lst[0])
            # if noOfDays < 1:
            #     popup_1()
            if noOfDays > 0:

                total_days = noOfDays + 1
                booked_popup(total_days)
                root.destroy()


def booked_popup(total_days):
    response = messagebox.showinfo("Thank You!",
                                   "Your booking is successful for {} days and Total amount to be paid is {}\n\nThank You!".format(
                                       total_days, total_days * 2000))

root.geometry('400x300')
root.resizable(False, False)
header_label = Label(root, text="BOOK CAR", bg='black', fg='white', font=("New Times Roman", 25,))
header_label.pack(fill=X)
pickUp = Label(root, text="PICK-UP DATE", bg='grey', fg='white')
pickUp.place(x=60, y=55)
calPick = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2,
                    date_pattern='yyyy-mm-dd',mindate=today,maxdate=week)
calPick.place(x=60, y=75)
dropOff = Label(root, text='DROP-OFF DATE', bg='grey', fg='white')
dropOff.place(x=230, y=55)
calDrop = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2,
                    date_pattern='yyyy-mm-dd',mindate=today,maxdate=week)
calDrop.place(x=230, y=75)
btnOk = Button(root, text="BOOK", height=2, width=10, command=lambda: p(calPick, calDrop))
btnOk.place(x=150, y=120)


root.mainloop()
