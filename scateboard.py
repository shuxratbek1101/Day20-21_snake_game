from turtle import Turtle,Screen


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(20,250)
        self.num = 0

    def count(self):

        self.write(f"Score: {self.num}", align="right", font = ('Arisl', 24, 'normal'))

    def update_board(self):
        self.num += 1
        self.clear()
        self.count()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="right", font=('Arisl', 16, 'normal'))

# screen = Screen()
# screen.bgcolor('black')
# a=Scaetboard()
# a.count()

# screen.exitonclick()