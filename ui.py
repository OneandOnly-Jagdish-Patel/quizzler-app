import tkinter.messagebox
import time
from datetime import datetime
THEME_COLOR = "#375362"

from tkinter  import *
from quiz_brain import QuizBrain
class QuizInterface:

    def __init__(self):
        self.quiz_ques = QuizBrain()
        self.window = Tk()
        self.score = 0
        self.window.title("Quiz Interface")
        self.window.configure(bg=THEME_COLOR, padx=20,pady=20)
        #for mid white part
        self.canvas = Canvas(width=300,height=250,bg="white",highlightthickness=0)
        self.tex = self.canvas.create_text(150,125,text="example",fill=THEME_COLOR,width=300)
        self.canvas.grid(pady=50,row=1,column=0,columnspan=2)
        
        
        #for True
        true = PhotoImage(file='images/true.png')
        true_button =Button(padx=20,pady=20,image=true,command=self.true_ans)
        true_button.grid(row=2,column=0)
        #for False
        false = PhotoImage(file='images/false.png')
        false_button = Button(padx=20,pady=20,image=false,command=self.false_ans)
        false_button.grid(row=2, column=1)

        self.score_card = Label(text=f'Score:  ',fg='green')
        self.score_card.grid(row=0,column=1)
        self.show_question()
        self.window.mainloop()

    def show_question(self):
        q_text = self.quiz_ques.next_question()
        if q_text == "Done":
            self.Final_complete = tkinter.messagebox.askyesno("Result and feedback",f"Your Score is {self.score} out of 10.\nDid you liked this game and questions in it.")

            if self.Final_complete:
                with open("feedback.txt","a") as feed:
                    feed.write(f"An User Liked your program at {datetime.now()}")
            else:
                with open("feedback.txt","a") as feed:
                    feed.write(f"An User DisLiked your program at {datetime.now()}")
            self.window.destroy()

        else:
            self.canvas.itemconfig(self.tex,text = q_text)
    def true_ans(self):
        if self.quiz_ques.current_question["correct_answer"] == "True":
            self.score += 1
            self.score_card.config(text = f"Score: {self.score}")
            self.show_question()
        else:
            self.show_question()

    def false_ans(self):
        if self.quiz_ques.current_question["correct_answer"] == "False":
            self.score += 1
            self.score_card.config(text = f"Score: {self.score}")
            self.show_question()
        else:
            self.show_question()

        

