import tkinter as tk
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from center_Window import center_window

root = tk.Tk()
root.geometry(center_window(450,420,root.winfo_screenwidth(),root.winfo_screenheight()))
root.title("Car Rental")

main_lbl_head = Label(root,text='Car Rental System',bg='black',fg='white',font=("New Times Roman", 25,))
main_lbl_head.pack(fill=X,ipady=10)


main_frame = Frame(root,highlightthickness=1,highlightbackground="black")
main_frame.pack(pady=20,padx=20,expand=1)

#Guest Button Code
def guest():
    import guestDisplay
    root.destroy


def empty():
    empty = Label(main_frame)
    empty.pack(pady=12)

#Guest Label and Button part
main_btn_guest = Button(main_frame,text="Guest",width=8,font=("New Times Roman", 15,))
main_btn_guest.pack(pady=5)

main_lbl_guest = Label(main_frame,text="                 If you just want to Broswe, click above                 ",font=("New Times Roman", 10,))
main_lbl_guest.pack(pady=2)

empty()

#Login Label and Button part
main_btn_login = Button(main_frame,text="Login",width=8,font=("New Times Roman", 15,))
main_btn_login.pack(pady=5)

main_lbl_login = Label(main_frame,text="If already have a account, click above",font=("New Times Roman", 10,))
main_lbl_login.pack(pady=2)

empty()

#Register Label and Button part
main_btn_register = Button(main_frame,text="Register",width=8,font=("New Times Roman", 15,))
main_btn_register.pack(pady=5)

main_lbl_register = Label(main_frame,text="Want to create a account, click above",font=("New Times Roman", 10,))
main_lbl_register.pack(pady=2)

empty()

root.mainloop()
