from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        file = open("data.txt")
        self.high_score = int(file.read())
        self.scoring()

    def scoring(self):
        self.clear()
        self.write(f"SCORE : {self.score} HIGH SCORE: {self.high_score}",False,"center",("Times New Roman",10,"bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("data.txt","w")
            file.write(f"{self.high_score}")
        self.score = 0
        self.scoring()

    def update(self):
        self.score += 1
        self.scoring()
