import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        

    def refresh(self):
        xcordinate = random.randint(-280,280)
        ycordinate = random.randint(-280,280)
        self.goto(xcordinate,ycordinate)

        