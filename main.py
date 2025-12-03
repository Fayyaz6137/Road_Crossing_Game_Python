import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from score_board import ScoreBoard

game_on = True
game_over = False
screen = Screen()


def setup():
    setup_screen()
    setup_objects()
    screen_listeners()


def setup_objects():
    global player
    player = Player()
    global score
    score = ScoreBoard()
    global cars
    cars = CarManager()


def player_move():
    if game_on:
        player.move()
        score.score_up()
        score.update()


def setup_screen():
    global screen
    screen.clear()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.tracer(0)


def screen_listeners():
    screen.listen()
    screen.onkey(player_move, 'Up')
    screen.onkey(player.move_back, 'Down')
    screen.onkey(player.move_right, 'Right')
    screen.onkey(player.move_left, 'Left')
    screen.onkey(restart, 'v')
    screen.onkey(pause, 'space')


def gameplay():
    global game_on
    global game_over
    while game_on:
        time.sleep(0.1)
        screen.update()
        cars.create_cars()
        cars.move_cars()

        for car in cars.all_cars:
            if car.distance(player) < 25:
                game_on = False
                score.game_over()
                game_over = True

        if player.has_finished():
            player.go_to_start()
            cars.level_up()
            score.level_up()
            score.update()


def pause():
    global game_on, game_over
    game_on = not game_on if not game_over else False
    gameplay()


def restart():
    global game_over, game_on
    if game_over:
        game_over = False
        game_on = True
        start()


def start():
    setup()
    gameplay()


start()

screen.exitonclick()
