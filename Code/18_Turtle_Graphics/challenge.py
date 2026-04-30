import colorgram
from turtle import Turtle, Screen, colormode
import random

graphics = Turtle()

# Extracting colours from an image using colorgram
# colours = colorgram.extract("painting.avif", 30)
# rgb_colours = []

# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     rgb_colours.append(new_colour)

color_list = [(208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (158, 45, 83), (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44), (36, 42, 70), (187, 93, 105), (187, 139, 170), (84, 123, 181), (59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72), (45, 74, 78), (161, 202, 220), (80, 73, 44), (57, 131, 121), (218, 176, 188), (220, 183, 166), (166, 207, 165)]

print(color_list)
graphics.hideturtle()
graphics.penup()
starting_position = [-500, -500]
graphics.setposition(starting_position)
step = 70 # 50 spacing + 2 radius
size = 20 # diameter of the dot
colormode(255)
graphics.speed("fastest")

def paint_rows(rows):
    for _ in range(rows - 1):
        graphics.dot(size, random.choice(color_list))
        graphics.penup()
        graphics.forward(step)
        graphics.pendown()
    graphics.dot(size, random.choice(color_list))
        
for _ in range(10):
    paint_rows(10)
    graphics.penup()
    graphics.setposition(starting_position[0], graphics.position()[1] + step)
    graphics.pendown()

Screen().exitonclick()