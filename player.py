import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    
    def moveUp(self):
        if(self.ycor()<280):
            self.forward(MOVE_DISTANCE)
    
    def moveDown(self):
        if self.ycor()>-280:
            self.backward(MOVE_DISTANCE)
    
    def restart(self):
        self.goto(STARTING_POSITION)