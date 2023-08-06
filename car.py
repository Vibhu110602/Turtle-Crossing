import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

class Car(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.goto((300,random.randint(-230,240)))
        self.shapesize(stretch_len=2,stretch_wid=1)

class Traffic:
    car=[]
    speed=STARTING_MOVE_DISTANCE
    def __init__(self):
        self.add()
    
    def add(self):
        newCar=Car()
        self.car.append(newCar)
    
    def move(self):
        for cars in self.car:
            cars.forward(self.speed)
    
    def increase(self):
        self.speed+=MOVE_INCREMENT
