import turtle
FONT = ("Courier", 24, "normal")

class ScoreBoard(turtle.Turtle):

    level=1
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200,260)
        self.refresh()
    
    def refresh(self):
        self.clear()
        self.write(arg=f"Level : {self.level}",move=False,align="center",font=FONT)
    
    def loose(self):
        self.goto(0,0)
        self.clear()
        self.write("You loose",move=False,align="center",font=FONT)