class Controller:
    def __init__(self,data):
        self.question_list = data
        self.question_number = 0
        self.score = 0
        self.current=None

# To the next question
    def nextquestion(self):
        self.current = self.question_list[self.question_number]
        self.question_number+=1
        #print(self.question_number,":",current.text," = ? (T/f)")
        #user_answer = input("You Answer :")
        #self.CheckAns(user_answer,current.answer)
        return f"{self.question_number}) {self.current.text}"

    def hasQuestion(self):
        return self.question_number<len(self.question_list)

    def CheckAns(self,userInput):
        correct_answer=self.current.answer
        if(userInput.lower()==correct_answer.lower()):
            self.score+=1
            return True
        else :
            return False
