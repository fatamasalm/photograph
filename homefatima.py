import turtle

from turtle import *

#t = Turtle

speed(0)

color('brown')
forward(350)

left(90)	
forward(100)

color("alice blue")		#SKY VERTICAL left
begin_fill()
forward(250)

left(90)	#SKY HORIZONTAL
forward(490)

left(90)			#SKY VERTICAL right
forward(250)

left(90)
forward(491)
end_fill()


color("brown")	#GROUND
right(90)
forward(100)
right(90)
forward(630)

penup()
left(180)
forward(180)
left(90)
forward(45)



color("green") #green of tree
begin_fill()
right(385)


forward(170)

right(130)
forward(170)


right(115)
forward(82)
end_fill() #end of tree leaves


penup()	#TREE TRUNK
color("brown")
right(180)
forward(30)

pendown()
begin_fill()
right(90)
forward(45)

right(90)
forward(45)

right(90)
forward(45)

right(90)
forward(45)
end_fill() #end of tree trunk


penup()
right(90)
forward(45)

right(90)
forward(45)

#pendown()
color("brown")
forward(110)

color("brown")
right(90)
forward(105)
color("blue")
forward(105)

#penup()
color("black")
right(90)
forward(300)

right(180) 

pendown()

circle(30,50) #bird
right(90)
circle(30,50)

penup()
left(170)
forward(200)

pendown()            #SUN
color("yellow")
begin_fill()
circle(60) 
end_fill()

penup()
color("black")
right(90)

forward(206)

right(90)
forward(125)

pendown() 
color("brown")		#DOOR
begin_fill()
forward(25)

right(90) 
forward(40)
right(90)
forward(25)
right(90)
forward(40)

end_fill()

color("blue")      #HOUSE

left(90)
forward(50)

left(90)
forward(100)
left(90)
forward(125)
left(90)
forward(100)


left(90)
forward(50)

right(180)
forward(50)

right(90)
forward(100)

right(45)	#ROOF
forward(90)

right(90)
forward(90)

right(45)

penup()
forward(100)
right(90)
