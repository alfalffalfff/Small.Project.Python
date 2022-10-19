#Runprogram
from Qustion import Question
from data import question_data
from controller import Controller
from Ui import UserInterface

all_question=[]

# question
for i in question_data:
    text=i["text"]
    answer=i["answer"]
    question=Question(text,answer)
    all_question.append(question)

# Build Controller
controller = Controller(all_question)
userinterface=UserInterface(controller)




