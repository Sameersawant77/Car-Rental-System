from tkinter import *
from tkcalendar import *
from tkinter import messagebox
from guestDisplay import id
root = Tk()
root.geometry('400x400')
root.configure(bg='grey')


def Book_Window():
    def p(calpick, caldrop):
        result = caldrop.get_date() - calpick.get_date()
        lst = str(result)
        lst = lst.split()
        noOfDays = int(lst[0])
        if noOfDays < 1:
            popup_1()
        else:
            global total_days
            total_days = noOfDays
            print(total_days)

    def popup_1():
        response = messagebox.showinfo('Please Enter Porper date')

    book_wn = Toplevel(root, bg='grey')
    book_wn.geometry('400x300')
    book_wn.resizable(False, False)
    header_label = Label(book_wn, text="BOOK CAR", bg='black', fg='white', font=('Showcard Gothic', 25))
    header_label.pack(fill=X)
    label_id = Label(book_wn,text="1", bg='black', fg='white', font=('Showcard Gothic', 25))
    label_id.pack()
    pickUp = Label(book_wn, text="PICK-UP DATE", bg='grey', fg='white')
    pickUp.place(x=60, y=55)
    calPick = DateEntry(book_wn, width=12, background='darkblue',foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
    calPick.place(x=60, y=75)
    dropOff = Label(book_wn, text='DROP-OFF DATE', bg='grey', fg='white')
    dropOff.place(x=230, y=55)
    calDrop = DateEntry(book_wn, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
    calDrop.place(x=230, y=75)
    btnOk = Button(book_wn, text="BOOK", height=2, width=10, command=lambda: p(calPick, calDrop))
    btnOk.place(x=150, y=120)


btn = Button(root, text="BOOK", height=5, width=10, command=Book_Window)
btn.place(relx=.4, rely=.35)

root.mainloop()
