from turtle import Turtle


class MrTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("#f4d9a8")
        self.fillcolor("#bb742c")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -250)

    def move_up(self):
        self.forward(20)

    # def move_down(self):
    #     self.backward(20)
    #
    # def move_right(self):
    #     x = self.xcor()
    #     y = self.ycor()
    #     self.goto(x+20, y)
    #
    # def move_left(self):
    #     x = self.xcor()
    #     y = self.ycor()
    #     self.goto(x-20, y)

    def reset_position(self):
        self.goto(0, -250)




