from turtle import Turtle

class ScoreBoard(Turtle):   
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,260)
        self.color("white")
        self.update_score()
        self.hideturtle() 

    def update_score(self):
        self.write(f"El puntaje es: {self.score} ",font=("Arial",20,"bold"), align="center")

    def increase_score (self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over (self):
        self.clear()
        self.write(f"Juego terminado por malo :( ",font=("Arial",20,"bold"), align="center")