from turtle import Turtle

FONT = ('Courier', 14, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.level = 1
        self.score = 0
        self.goto(-240, 250)
        self.update()

    def level_up(self):
        self.level += 1

    def score_up(self):
        self.score += 1

    def update(self):
        self.clear()
        self.write(f'Level: {self.level}\nScore : {self.score}', align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)
