#program to demonstrate use of setposition(), pendown() and penup() methods

from turtle import *
from time import *
bgcolor("green")
color("red")# color of the pen
shape("turtle")# shape of turtle
sleep(1)
setposition(50,-70)
forward(50)
sleep(1)
penup()
sleep(1)
forward(150)
sleep(1)
pendown()
forward(200)
exitonclick()

