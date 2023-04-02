from tkinter import *
from tkinter import ttk
from tkinter import Scrollbar
from PIL import Image, ImageTk


class Gui:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Rental Service")
        self.root.geometry('1200x700')
        self.root.resizable(False, False)

        self.label_Title = Label(self.root, text="Car Rental Service", bg="black", fg='white', font=("Showcard Gothic", 30))
        self.label_Title.pack(side=TOP, fill=X)

        # tabbing Frame
        self.tab_frame = Frame(self.root, bg='grey')
        self.tab_frame.pack(fill=BOTH, expand=True, after=self.label_Title)

        # Tab Style
        style = ttk.Style(self.tab_frame)
        style.configure('tab.Notebook', tabposition='wn')

        # Tab Layout
        self.tab_control = ttk.Notebook(self.tab_frame)

        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab4 = ttk.Frame(self.tab_control)

        # Add tabs to notebook
        self.tab_control.add(self.tab1, text=f"{'Home':^30s}")
        self.tab_control.add(self.tab2, text=f"{'Search':^30s}")
        self.tab_control.add(self.tab3, text=f"{'Account':^30s}")
        self.tab_control.add(self.tab4, text=f"{'About us':^30s}")

        self.tab_control.pack(expand=1, fill=BOTH)

    # Home Tab Code

    # Find car Tab
        # Search frame
        self.frame_search = Frame(self.tab2, bg="black")
        self.frame_search.pack(expand=True, fill=BOTH)
        # Search Frame Design
        self.Find_Car_Label = Label(self.frame_search, text="Find Vehicle", font=('Showcard Gothic', 25), bg='blue')
        self.Find_Car_Label.place(rely=0.27, x=60)
        self.search_bar = Entry(self.frame_search, font=("cosmicsans", 20), width=40)
        self.search_bar.place(relx=0.25, rely=0.34)
        self.img = Image.open('Lables/Search.png')
        self.img = self.img.resize((32, 32), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.img)
        self.search_label = Button(self.frame_search, image=self.image)
        self.search_label.place(x=950, y=33)
        # Result frame
        self.frame_result = Frame(self.tab2, bg="grey", height=400)
        self.frame_result.pack(after=self.frame_search, fill=BOTH, expand=True)
        self.frame_result_scrollbar = Scrollbar(self.frame_result)
        self.frame_result_scrollbar.pack(side=RIGHT, fill=Y)
        self.frame_display_text = Text(self.frame_result, width=125, yscrollcommand=self.frame_result_scrollbar.set)
        self.frame_result_scrollbar.configure(command=self.frame_display_text.yview)
        self.frame_display_text.pack(pady=20, expand=True, fill=Y)


        # Account tab
        self.Account_tab_Frame = Frame(self.tab3, bg='grey')
        self.Account_tab_Frame.pack(expand=True, fill=BOTH)
        self.User_name = Label(self.Account_tab_Frame, bg='grey', text="User name : Omkar Bhoir", fg='white', font=("cosmicsans", 15))
        self.User_name.place(relx=0.4, y=140)
        self.user_icon = Image.open('C:\Python\Project/1/Omkar/Lables/User_profile.png')
        self.user_icon = self.user_icon.resize((100, 100), Image.ANTIALIAS)
        self.user_icon_ttk = ImageTk.PhotoImage(self.user_icon)
        self.User_ID = Label(self.Account_tab_Frame, image=self.user_icon_ttk, bg='white')
        self.User_ID.place(relx=0.45, y=10)


root = Tk()
obj = Gui(root)
root.mainloop()
