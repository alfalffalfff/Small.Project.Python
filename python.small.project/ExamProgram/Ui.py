from cgitb import text
from tkinter import *
from controller import Controller
THEME_APP = '#375362'

class UserInterface:
    def __init__(self,controller:Controller):
        
        self.controller = controller
        # Display Program
        self.window=Tk()
        self.window.title("QuizProgram")
        self.window.config(padx=30,pady=30,bg=THEME_APP)
        
        # Point Field
        self.scoreLabel=Label(text="Point : 0",fg="white",bg=THEME_APP)
        self.scoreLabel.grid(row=0,column=2)

        # quiz field
        self.canvas=Canvas(width=300,height=300,bg="white")
        self.question_text=self.canvas.create_text(
            150,
            125,
            width=280,
            text=" 1+1=2 ",
            font=('Arai',18,'bold'),
            fill=THEME_APP
        )
        self.canvas.grid(row=1,column=1,columnspan=2,pady=50)

        # Button
        true_image=PhotoImage(file="images/check.png")
        self.ture_button=Button(image=true_image,command=self.true_pressed)
        self.ture_button.grid(row=2,column=1)

        false_image=PhotoImage(file="images/remove.png")
        self.false_button=Button(image=false_image,command=self.false_pressed)
        self.false_button.grid(row=2,column=2)
        self.get_next_question()
      
        self.window.mainloop()

    def get_next_question(self):
        if self.controller.hasQuestion():
            q_text=self.controller.nextquestion()
            self.scoreLabel.config(text=f"Point : {self.controller.score}")
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.scoreLabel.config(text=f"Point : {self.controller.score}")
            self.canvas.itemconfig(self.question_text,text='End Of Exam')
            self.ture_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.controller.CheckAns("true")
        self.waitNextQuestion()

    def false_pressed(self):
        self.controller.CheckAns("false")
        self.waitNextQuestion()

    def waitNextQuestion(self):
        self.window.after(1000,self.get_next_question)