#Importing
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image

#Tkinter defination
root=Tk()
root.geometry("800x1200")
root.title("Image Adder")

#Default img to load at start
absolute_path = "C://Users//kunal//Desktop//car_images//"
default_img = "no_image"
extension_of_path = ".png"

default_path = absolute_path+default_img+extension_of_path
im = Image.open(default_path)
default_pic = im.resize((280,180), Image.ANTIALIAS)
default_pic = ImageTk.PhotoImage(default_pic)



def addThis():
    #To get image name
    try:
        entry_path = entry_img.get()
        entry_pic = absolute_path+entry_path+extension_of_path
        my_pic = Image.open(entry_pic)

        #Resize image
        resized = my_pic.resize((280,180), Image.ANTIALIAS)

        new_pic = ImageTk.PhotoImage(resized)
        label_img.configure(image=new_pic)
        #To not collect the new img while throwing old image
        label_img.image = new_pic
    except:
        messagebox.showinfo("Error Occured", "Wrong Image name")


label_img = Label(root,image=default_pic,borderwidth=2, relief="groove")
label_img.grid(row=0,column=0,rowspan=3,columnspan=3,pady=10,padx=10)
entry_img = Entry(root,width=20)
entry_img.grid(row=4,column=0,padx=10,pady=10)
btn_img = Button(root,text="Click to Add Image",command=addThis)
btn_img.grid(row=5,column=0,pady=10,padx=10)

root.mainloop()


#Code if failed
# from tkinter import *
# from PIL import ImageTk, Image
#
# root=Tk()
# root.geometry("800x500")
#
# #Open image
# my_pic = ")
#
# #Resize image
# resized = my_pic.resize((300,225), Image.ANTIALIAS)
#
# new_pic = ImageTk.PhotoImage(resized)
# #Image size
# my_label = Label(root, image=new_pic)
# my_label.pack(pady=20)
#
# root.mainloop()
