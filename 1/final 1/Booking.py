from tkinter import *
from tkcalendar import *
from tkinter import messagebox

root = Tk()
root.geometry('400x400')
root.configure(bg='grey')


def Book_Window():
    def p(calpick, caldrop):
        result = caldrop.get_date() - calpick.get_date()
        lst = str(result)
        lst = lst.split()
        if lst[0] == '0:00:00':
            popup_1()
        else:
            noOfDays = int(lst[0])
            # if noOfDays < 1:
            #     popup_1()
            if noOfDays > 0:
                global total_days
                total_days = noOfDays
                booked_popup(total_days)
                book_wn.destroy()

    def popup_1():
        response = messagebox.showinfo('Warning!', 'Please enter more than one day')

    def booked_popup(total_days):
        response = messagebox.showinfo("Thank You!",
                                       "Your booking is successful for {} days and Total amount to be paid is {}\n\nThank You!".format(
                                           total_days, total_days * 2000))

    book_wn = Toplevel(root, bg='grey')
    book_wn.geometry('400x300')
    book_wn.resizable(False, False)
    header_label = Label(book_wn, text="BOOK CAR", bg='black', fg='white', font=('Showcard Gothic', 25))
    header_label.pack(fill=X)
    pickUp = Label(book_wn, text="PICK-UP DATE", bg='grey', fg='white')
    pickUp.place(x=60, y=55)
    calPick = DateEntry(book_wn, width=12, background='darkblue', foreground='white', borderwidth=2,
                        date_pattern='dd/mm/yyyy')
    calPick.place(x=60, y=75)
    dropOff = Label(book_wn, text='DROP-OFF DATE', bg='grey', fg='white')
    dropOff.place(x=230, y=55)
    calDrop = DateEntry(book_wn, width=12, background='darkblue', foreground='white', borderwidth=2,
                        date_pattern='dd/mm/yyyy')
    calDrop.place(x=230, y=75)
    btnOk = Button(book_wn, text="BOOK", height=2, width=10, command=lambda: p(calPick, calDrop))
    btnOk.place(x=150, y=120)


btn = Button(root, text="BOOK", height=5, width=10, command=Book_Window)
btn.place(relx=.4, rely=.35)

root.mainloop()
