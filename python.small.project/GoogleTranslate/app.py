from tkinter import *
from googletrans import Translator

def translate():
    text2.delete(1.0,END)
    message = text1.get('1.0','end-1c') #ดึงข้อความมาใช้
    translator = Translator()
    output=translator.translate(text=message,src='en',dest='th')
    text2.insert('end',output.text)

def reset():
    text1.delete(1.0,END)
    text2.delete(1.0,END)

# display
root = Tk()
root.title("Google Translate (EN-TH)")
root.geometry('530x300')
root.maxsize(530,300)
root.minsize(530,300)

# widget
labeel=Label(text="English - Thai",font=('Arial',20,'bold'))
labeel.place(x=150,y=20)

# Text for English
text1 = Text(root,width=30,height=10)
text1.place(x=10,y=70)
# Text for Thai
text2 = Text(root,width=30,height=10)
text2.place(x=275,y=70)

#button Translate
btTran=Button(root,text="Translate",command=translate)
btTran.place(x=180,y=250)
#button Clear
btClear=Button(root,text="Clear",command=reset)
btClear.place(x=290,y=250)

root.mainloop()