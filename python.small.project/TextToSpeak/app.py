from tkinter import *
from gtts import gTTS

#function
def Convert():
    # Get Text
    word=text_entry.get()
    language='th'
    output=gTTS(text=word,lang=language,slow=False)
    output.save("Sound.mp3")

root=Tk()
root.title("text to sound")
canvas=Canvas(root,width=400,height=300)
canvas.pack()

# Head
app_label=Label(text="Text To Sound",font=('Arial',20,'bold'))
canvas.create_window(200,100,window=app_label)

# Text
text_entry=Entry(root)
canvas.create_window(200,180,window=text_entry)

#button
bt1=Button(text="Convert",command=Convert)
canvas.create_window(200,230,window=bt1)

root.mainloop()