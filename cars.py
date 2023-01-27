from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.move_speed = 0.03
        for i in range(0, 20):
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(1, 2)
            start_x = random.randint(-300, 400)
            start_y = random.randint(-180, 180)
            new_car.goto(start_x, start_y)
            new_car.setheading(180)
            self.cars.append(new_car)

    def move_cars(self):
        time.sleep(self.move_speed)
        for car in self.cars:
            y = car.ycor()
            x = car.xcor()
            if x < -300:
                car.goto(400, y)
            else:
                car.goto(x - 2, y)

    def speed_up(self):
        self.move_speed *= 0.5
        print(self.move_speed)

