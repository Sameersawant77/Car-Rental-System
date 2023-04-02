from tkinter import *
from tkinter import ttk
from tkinter import Scrollbar
from PIL import Image, ImageTk

root = Tk()
root.title("Car Rental Service")
root.geometry('1200x700')
root.resizable(False, False)


label_Title = Label(root, text="Car Rental Service", bg="black", fg='white',font=("Showcard Gothic", 30))
label_Title.pack(side=TOP, fill=X)

# Tab Style
style = ttk.Style(root)
style.configure('tab.Notebook', tabposition='wn')

# Tab Layout
tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)

# Add tabs to notebook
tab_control.add(tab1, text=f"{'Home':^20s}")
tab_control.add(tab2, text=f"{'Search':^20s}")
tab_control.add(tab3, text=f"{'Account':^20s}")
tab_control.add(tab4, text=f"{'About us':^20s}")

tab_control.pack(expand=1, fill=BOTH)

# Find car Tab
# Search frame
frame_search = Frame(tab2, bg="black")
frame_search.pack(expand=True, fill=BOTH)
# Search Frame Design
Find_Car_Label = Label(frame_search, text="Find Vehicle", font=('Showcard Gothic', 25), bg='blue')
Find_Car_Label.place(rely=0.27, x=60)
search_bar = Entry(frame_search, font=("cosmicsans", 20), width=40)
search_bar.place(relx=0.25, rely=0.34)
img = Image.open('C:/Python/Project/1/Omkar/Lables/Search.png')
img = img.resize((32, 32), Image.ANTIALIAS)
image = ImageTk.PhotoImage(img)
search_label = Button(frame_search, image=image)
search_label.place(x=950, y=33)

# Result frame
frame_result = Frame(tab2, bg="grey", height=400)
frame_result.pack(after=frame_search, fill=BOTH, expand=True)
Display_canvas = Canvas(frame_result, height=600)
frame_result_scrollbar = Scrollbar(frame_result, orient="vertical",command=Display_canvas.yview)
frame_result_scrollbar.pack(side=RIGHT, fill=Y)
Display_canvas.configure(yscrollcommand=frame_result_scrollbar.set)
Display_canvas.pack(expand=True)


root.mainloop()
