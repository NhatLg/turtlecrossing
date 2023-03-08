import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_manager = CarManager()

screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

screen.listen()
screen.onkeypress(player.up, "Up")

is_game_on = True
loop_counter = 0
while is_game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    if loop_counter % 6 == 0:
        car_manager.generate_batch_rand_car()
    car_manager.remove_passed_cars()
    loop_counter += 1

screen.exitonclick()