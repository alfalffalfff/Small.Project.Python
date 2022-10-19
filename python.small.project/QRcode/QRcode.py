from fileinput import filename
from tkinter import *
import pyqrcode
import png
from PIL import ImageTk,Image 

# function Button
def generateQRCODE():
    # GET link and qrcode
    link_name = name_entry.get()
    link = link_entry.get()
    file_name=link_name+".png"
    # Create QRCode
    url=pyqrcode.create(link)
    url.png(file_name,scale=5)
    # Project QRcode
    image=ImageTk.PhotoImage(Image.open(file_name))
    image_label=Label(image=image)
    image_label.image=image
    canvas.create_window(200,370,window=image_label)


# display
root = Tk()
root.title("QRCode Generator")
canvas=Canvas(root,width=400,height=500)
canvas.pack()

# Name Program 
app_label=Label(root,text="QRCode Generator",font=('Arial',20,'bold'))
canvas.create_window(200,50,window=app_label)

#ระบุชื่อ link
name_label=Label(root,text="Name of QRCode")
canvas.create_window(200,100,window=name_label)

link_label=Label(root,text="URL")
canvas.create_window(200,160,window=link_label)

#create textbox
name_entry=Entry(root)
canvas.create_window(200,130,window=name_entry)

link_entry=Entry(root)
canvas.create_window(200,180,window=link_entry)

#button
bt1=Button(text="Create QRCode",command=generateQRCODE)
canvas.create_window(200,230,window=bt1)


root.mainloop()