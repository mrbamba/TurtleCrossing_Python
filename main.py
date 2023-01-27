from turtle import Turtle, Screen
from cars import Cars
from mr_turtle import MrTurtle
from scoreboard import Scoreboard
import random

BACKGROUND_COLORS = ["#edb879", "#44bcd8", "#b97455", "#cce7e8", "#b879ed", "#79ed7e", "#ed79e8", "#79edb8"]

# Create and setup the screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor(random.choice(BACKGROUND_COLORS))
screen.tracer(0)

cars = Cars()
game_is_on = True
mr_turtle = MrTurtle()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(mr_turtle.move_up, "Up")
# screen.onkey(mr_turtle.move_down, "Down")
# screen.onkey(mr_turtle.move_right, "Right")
# screen.onkey(mr_turtle.move_left, "Left")

while game_is_on:
    cars.move_cars()
    screen.update()

    # Detect collision with car
    for car in cars.cars:
        if mr_turtle.distance(car) < 20:
            scoreboard.end_game()
            game_is_on = False

    if mr_turtle.ycor() > 250:
        scoreboard.level_up()
        mr_turtle.reset_position()
        cars.speed_up()
        screen.bgcolor(random.choice(BACKGROUND_COLORS))


screen.exitonclick()
