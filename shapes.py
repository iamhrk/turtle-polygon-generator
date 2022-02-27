from turtle import Turtle, Screen
import random

brush = Turtle()
brush.penup()
brush.goto(-100, 100)
screen = Screen()
screen.colormode(255)


def color_generator():
    """Generates a random rgb color"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    gen_color = (r, g, b)
    return gen_color


n_side_of_lar_polygon = int(
    screen.textinput("Choose your largest polygon size", "Enter the number of sides of the largest "
                                                         "polygon you want to draw"))
brush.pendown()
for i in range(3, n_side_of_lar_polygon + 1):
    brush.color(color_generator())
    for _ in range(i):
        brush.forward(100)
        brush.right(360 / i)

screen.exitonclick()
