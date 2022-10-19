from tkinter import *
from pytube import YouTube
from moviepy.editor import *

# function in program
def Download():
    # Get URL
    video_path=link.get()
    mp4=YouTube(video_path).streams.get_highest_resolution().download()
    video_clip=VideoFileClip(mp4)
    video_clip.close()
    print("Finish Download {}".format(video_path))

# Display monitor
root=Tk()
root.title("YT Download")
canvas=Canvas(root,width=400,height=200)
canvas.pack()

# Name of program
app_title=Label(root,text="Download VDO from YT",font=('Arial',20,'bold'))
canvas.create_window(200,30,window=app_title)

# Link and Dowload BUtton
label=Label(root,text="URL")
canvas.create_window(200,80,window=label)

link=Entry(root,width=60)
canvas.create_window(200,100,window=link)

bt1=Button(text="Download",fg="white",bg="red",command=Download)
canvas.create_window(200,150,window=bt1)

root.mainloop()