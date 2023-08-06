import turtle
import time
import scoreboard
import player
import car

myScreen=turtle.Screen()
myScreen.setup(width=600,height=600)
myScreen.bgcolor("white")
myScreen.tracer(0)
myScreen.listen()

myPlayer=player.Player()
myScreen.onkey(key="Up",fun=myPlayer.moveUp)
myScreen.onkey(key="Down",fun=myPlayer.moveDown)
cars=car.Traffic()
myScore=scoreboard.ScoreBoard()

game_is_on=True
loop=0
num=6
while game_is_on:
    time.sleep(0.1)
    myScreen.update()
    cars.move()
    if loop%num==0:
        cars.add()
    if myPlayer.ycor()>=280:
        myScore.level+=1
        myPlayer.restart()
        cars.increase()
        if num>4:
            num-=1
    myScore.refresh()
    for car in cars.car:
        if myPlayer.distance(car)<=21:
            myScore.loose()
            game_is_on=False
    loop+=1

myScreen.exitonclick()