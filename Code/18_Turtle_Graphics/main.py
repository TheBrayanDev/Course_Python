from turtle import Turtle, Screen, colormode # importing Turtle class and instantiating
import random

graphics = Turtle()
print(graphics)
graphics.shape("turtle")
graphics.color("coral")
graphics.speed(20)

# defining a function to generate random RGB colour values
def random_color():
    """Generates a random RGB colour value.
    Returns:
        tuple: A tuple containing the RGB colour values (r, g, b).
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Draw a square

for _ in range(4):
    graphics.forward(100)
    graphics.left(90)

graphics.color("blue")

# Draw a dashed line
turtle.begin_fill()
for _ in range(15):
    graphics.forward(10)
    graphics.penup()
    graphics.forward(10)
    graphics.pendown()

Screen().clearscreen()

# Draw different shapes (according to # of sides) with different colours 

graphics.setposition(0, 0)
graphics.shape("turtle")
colormode(255)

def draw_shape(num_sides):
    angle = 360 / num_sides
    side_length = 100
    for side in range(num_sides):
        graphics.forward(side_length)
        graphics.right(angle)

for _ in range(3, 11, 1):
    graphics.color(random_color())
    draw_shape(_)

Screen().clear()

# Random Walk

graphics.setposition(0, 0)
graphics.shape("turtle")
directions = [0, 90, 180, 270]
graphics.pensize(10)
colormode(255)

for _ in range(200):
    graphics.color(random_color())
    graphics.forward(30)
    graphics.right(random.choice(directions))

# Spirograph
graphics.setposition(0, 0)
Screen().clear()
colormode(255)
graphics.pensize(1)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        graphics.color(random_color())
        graphics.circle(100)
        graphics.right(size_of_gap)
    return

draw_spirograph(5)


Screen().exitonclick()
#from pretty_table_printer import pretty_table_printer
#table = pretty_table_printer()
#print(table)