from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.allcars = []
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        chance= random.randint(1,6)
        if chance==6:
            car=Turtle()
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-250 , 250)
            car.goto(300 , random_y)
            self.allcars.append(car)

    def move_cars(self):
        for car in self.allcars:
            car.backward(self.car_speed)

    def car_speed_increase(self):
        self.car_speed+=10

