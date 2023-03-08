import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

screen.listen()
screen.onkeypress(player.up, "Up")

is_game_on = True
loop_counter = 0
while is_game_on:
    time.sleep(car_manager.move_speed)
    screen.update()
    car_manager.move_cars()
    if loop_counter % 6 == 0:
        car_manager.generate_batch_rand_car()
    car_manager.remove_passed_cars()

    if player.ycor() == 280:
        scoreboard.increment_level()
        car_manager.increase_speed()
        player.back_to_starting_position()

    if car_manager.check_is_collided(player):
        scoreboard.game_over()
        is_game_on = False
    loop_counter += 1

screen.exitonclick()