import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_speed = 0.1
        self.generate_batch_rand_car() # first batch

    def generate_batch_rand_car(self):
        for i in range(2):
            randy = random.randint(-250, 250)
            newcar = Turtle()
            newcar.penup()
            newcar.shape("square")
            newcar.color(random.choice(COLORS))
            newcar.shapesize(stretch_wid=1, stretch_len=2)
            newcar.goto(340, randy)
            self.cars.append(newcar)

    def move_cars(self):
        for car in self.cars:
            new_x = car.xcor() - MOVE_INCREMENT
            car.goto(new_x, car.ycor())

    def remove_passed_cars(self):
        for car in self.cars:
            if car.xcor() < -340:
                self.cars.remove(car)

    def check_is_collided(self, playerObject):
        for car in self.cars:
            if car.distance(playerObject) < 22:
                return True

    def increase_speed(self):
        self.move_speed *= 0.9

