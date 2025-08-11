from turtle import *

timmy_turtle = Turtle()
timmy_turtle.shape("turtle")
timmy_turtle.color("lime green")

def draw_a_square():
    timmy_turtle.fd(100)
    timmy_turtle.right(90)
    timmy_turtle.fd(100)
    timmy_turtle.right(90)
    timmy_turtle.fd(100)
    timmy_turtle.right(90)
    timmy_turtle.fd(100)
    timmy_turtle.right(90)

draw_a_square()
screen = Screen()
screen.exitonclick()