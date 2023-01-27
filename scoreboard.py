from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.color("blue")
        self.penup()
        self.show_level()

    def show_level(self):
        self.clear()
        self.goto(-250, +250)
        self.write(arg=f"Level: {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.level += 1
        print("leveling_up")
        self.show_level()

    def end_game(self):
        self.goto(0, 0)
        self.color("black")
        self.write(arg="Game Over!", move=False, align=ALIGNMENT, font=("Arial", 36, "normal"))

