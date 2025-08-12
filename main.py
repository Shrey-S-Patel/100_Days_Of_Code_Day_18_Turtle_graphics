# Boys and girls this is frowned upon
# from turtle import *
# And you can even import the whole thing and simply give it an Alias
# import turtle as t

# Instead just do this.
from turtle import Turtle,Screen

# And when you want a package that's not in-built, simply ask PyCharm to do the work for you.
# Like here:
import heroes

print(heroes.WORDLIST)

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