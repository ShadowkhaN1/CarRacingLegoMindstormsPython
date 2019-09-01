#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from random import randint

# Write your program here
brick.sound.beep()

widthScreen = 180
heightScreen = 126

motor = Motor(Port.B)

playerPosition_X = 60
playerPosition_Y = 84
playerWidth = 60
playerHeight = 42


car1Position_X = randint(1, 3) * 60
car1Position_Y = -42

car2Position_X = randint(1, 3) * 60
car2Position_Y = -126

car3Position_X = randint(1, 3) * 60
car3Position_Y = -210

speedEnemy = 10

playerPositionNow = 1
playerPositionThen = 1



def updatePositionCarEnemy():
    global car1Position_X, car1Position_Y, car2Position_X, car2Position_Y, car3Position_X, car3Position_Y, speedEnemy
    car1Position_Y += speedEnemy
    car2Position_Y += speedEnemy
    car3Position_Y += speedEnemy

    if(car1Position_Y >= 126):
        car1Position_Y = -42
        car1Position_X = randint(1, 3) * 60

    if(car2Position_Y >= 126):
        car2Position_Y = -42
        car2Position_X = randint(1, 3) * 60

    if(car2Position_Y >= 126):
        car2Position_Y = -42
        car2Position_X = randint(1, 3) * 60


while True:
    brick.display.image("car.jpg", (playerPosition_X, playerPosition_Y), clear=False)
    brick.display.image("carEnemy.jpg", (car1Position_X, car1Position_Y), clear=False)
    brick.display.image("carEnemy.jpg", (car2Position_X, car2Position_Y), clear=False)
    brick.display.image("carEnemy.jpg", (car3Position_X, car3Position_Y), clear=False)


    if(motor.angle() >= -30 and motor.angle() <= 30):
        playerPosition_X = 60
        playerPositionNow = 1
    elif(motor.angle() >= 30):
        playerPosition_X = 120
        playerPositionNow = 2
    elif(motor.angle() <= -30):
        playerPosition_X = 0
        playerPositionNow = 0

    if(playerPositionThen != playerPositionNow):
        playerPositionThen = playerPositionNow
        brick.sound.beep()
        

    updatePositionCarEnemy()


    wait(60)
    brick.display.clear()