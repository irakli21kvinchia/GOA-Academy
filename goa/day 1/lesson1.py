from turtle import *


#we want to paint a house

#stwp 1:  draw a square

width(7)
color("purple")
speed(2)
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door 

forward(70)
begin_fill()
color("yellow")
left(90)

forward(90)       #height of the door
right(90)

forward(50)
right(90)

forward(90)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(130)
forward(150)
left(88)
forward(130)
end_fill()

left(42)
forward(30)
color("green")
begin_fill()
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

color("purple")
forward(30)

color("red")
right(90)
forward(200)

color("purple")
right(90)
forward(30)

begin_fill()
color("green")
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()


exitonclick()