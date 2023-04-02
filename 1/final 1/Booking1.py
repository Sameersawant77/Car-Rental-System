from tkinter import *
from tkcalendar import *
from tkinter import messagebox
from datetime import date

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
                booked_popup1(total_days, calpick, caldrop, total_days)
                book_wn.destroy()

    def popup_1():
        response = messagebox.showinfo('Warning!', 'Please enter more than one day')

    def booked_popup(total_days):
        response = messagebox.showinfo("Thank You!",
                                       "Your booking is successful for {} days and Total amount to be paid is {}\n\nThank You!".format(
                                           total_days, total_days * 2000))

    def booked_popup1(total_days, calpick, caldrop, noofdays):
        def Payment_Success_popup():
            response = messagebox.showinfo("Payment Successful", "Your payment is sucessful \nThank You")

        def OnlinePayment():
            def check_card(card_no, cvv):
                if card_no == '12345678' and cvv == '1234':
                    Payment_Success_popup()
                    Payment_portal.destroy()
                    booked.destroy()
                else:
                    CardNOEntry.delete(0, END)
                    CvvEntry.delete(0, END)
                    messagebox.showerror("Error", "Enter valid card details")


            Payment_portal = Toplevel(root, bg='grey')
            Payment_portal.title("Payment Portal")
            Payment_portal.geometry('400x400')
            Payment_portal_title_Label = Label(Payment_portal, text="Payment Portal", bg='black', fg='white', font=("Showcard Gothic", 30))
            Payment_portal_title_Label.pack(fill=X)
            Label_cardNo = Label(Payment_portal, text='Card No :', bg='grey', fg='White', font='bold')
            Label_cardNo.place(x=15, y=75)
            Label_cvv = Label(Payment_portal, text='CVV :', bg='grey', fg='White', font='bold')
            Label_cvv.place(x=15, y=120)
            CardNOEntry = Entry(Payment_portal)
            CardNOEntry.place(x=90, y=78)
            CvvEntry = Entry(Payment_portal)
            CvvEntry.place(x=70, y=120)
            pay_btn = Button(Payment_portal, text='Pay Now', command=lambda :check_card(CardNOEntry.get(), CvvEntry.get()))
            pay_btn.place(x=15, y=150)

        msg = "Bill: {} \t\t\tDate: {}\nPick-up Date: {}\t\t\tDrop-Off Date: {}"
        booked = Toplevel(root, bg='grey')
        booked.geometry('400x400')
        lbl_title = Label(booked, text='Bill Pay', bg='black', fg='White', font=("Showcard Gothic", 30))
        lbl_title.pack(fill=X)
        Bill_frame = Frame(booked, height=300, width=300, bg='white')
        Bill_frame.pack(pady=10)
        bill_msg = "Bill No : {}".format(10)
        current_date = 'Date : {}'.format(date.today().strftime("%d/%m/%Y"))
        pickUp_date = 'Pick-Up Date : {}'.format(calpick.get_date().strftime("%d/%m/%Y"))
        dropOff_date = 'Drop-Off Date : {}'.format(caldrop.get_date().strftime("%d/%m/%Y"))
        totalNoOfDays = 'Total Days : {}'.format(noofdays)
        Bill_label = Label(Bill_frame, bg='white', fg='black', text=bill_msg, font='bold')
        Bill_label.place(x=15, y=15)
        Date_label = Label(Bill_frame, bg='white', fg='black', text=current_date, font='bold')
        Date_label.place(x=150, y=15)
        Pick_date_label = Label(Bill_frame, bg='white', fg='black', text=pickUp_date, font='bold')
        Pick_date_label.place(x=15, y=40)
        Drop_date_label = Label(Bill_frame, bg='white', fg='black', text=dropOff_date, font='bold')
        Drop_date_label.place(x=15, y=65)
        Total_days_label = Label(Bill_frame, bg='white', fg='black', text=totalNoOfDays, font='bold')
        Total_days_label.place(x=15, y=90)
        ThankYouLabel = Label(Bill_frame, bg='white', fg='black', text='Thank You!', font='bold')
        ThankYouLabel.place(x=100, y=140)
        pay_msg = "Want to pay online? click Here"
        Pay_msg_Label = Label(Bill_frame, bg='white', fg='blue', text=pay_msg, font='bold')
        Pay_msg_Label.place(x=10, y=260)
        Pay_Now = Button(Bill_frame, text='Pay Now', command=OnlinePayment)
        Pay_Now.place(x=230, y=260)

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
