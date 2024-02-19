from tkinter import *
from quiz_brain import QuizBrain
THEME = "#375362"


class QuizInterface(QuizBrain):
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.win = Tk()
        self.win.title("Quizzler")
        self.win.config(padx=20, pady=20, bg=THEME)

        self.skor = Label(text=f"score: {self.quiz.score}", fg="white", bg=THEME,  font=("Arial", 15, "italic"))
        self.skor.grid(row=0,column=1, pady=10)
        
        self.tikfoto = PhotoImage(file="images/true.png")
        self.carpifoto = PhotoImage(file="images/false.png")
        
        self.canvas = Canvas(width=400,height=300,bg="white")
        self.question_text = self.canvas.create_text(200, 150, text="some question text", fill=THEME, font=("Arial", 20, "italic"), width=370)
        self.canvas.grid(row=1, column=0, columnspan=2,pady=40)

        self.tikbuton = Button(image=self.tikfoto, highlightthickness=0,  width=100, height=100, command=self.answer_true)
        self.tikbuton.grid(row=2,column=0)

        self.carpibuton = Button(image=self.carpifoto, highlightthickness=0, width=100, height=100, command=self.answer_wrong)
        self.carpibuton.grid(row=2,column=1)

        self.next_question()

        self.win.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.skor.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="testi bitirdin!")
            self.tikbuton.config(state="disabled")
            self.carpibuton.config(state="disabled")



    def answer_wrong(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def feedback(self,cevap):
        if cevap:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.win.after(1000, func=self.next_question)