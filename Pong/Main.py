# Pong

import turtle

# build window
window = turtle.Screen()
window.title("Pong by Tiffany Luo")
window.bgcolor("black")
windowWidth = 1000
windowHeight = 600
window.setup(width = windowWidth, height = windowHeight)
window.tracer(0)

paddleWidthStretch = 8
paddleLengthStretch = 1

# left paddle
paddleLeft = turtle.Turtle()
paddleLeft.speed(0)
paddleLeft.shape("square")
paddleLeft.color("white")
paddleLeft.shapesize(stretch_wid=paddleWidthStretch, stretch_len=paddleLengthStretch)
paddleLeft.penup()
paddleLeft.goto((windowWidth/-2) + 50, 0)

# right paddle
paddleRight = turtle.Turtle()
paddleRight.speed(0)
paddleRight.shape("square")
paddleRight.color("white")
paddleRight.shapesize(stretch_wid=paddleWidthStretch, stretch_len=paddleLengthStretch)
paddleRight.penup()
paddleRight.goto((windowWidth/2) - 50,0)

# ball
ball = turtle.Turtle
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

# functions


# main game loop
while True:
    window.update()
