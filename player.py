from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.setheading(90)
        self.penup()
        self.go_to_start()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def move_back(self):
        self.backward(MOVE_DISTANCE)

    def move_right(self):
        self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

    def move_left(self):
        self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())

    def has_finished(self):
        return True if self.ycor() > 280 else False

    def go_to_start(self):
        self.goto(STARTING_POSITION)
