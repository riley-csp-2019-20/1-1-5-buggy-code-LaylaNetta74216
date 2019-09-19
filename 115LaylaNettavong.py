#   a115_buggy_image.py
import turtle as trtl


#pen and spider sizes
pen = trtl.Turtle()
pen.pensize(40)
# spider body
pen.circle(20)
pen.speed(0)
legs = 8
legsize = 100
legdistance = 10000 / legs
pen.pensize(5)
spider = 0

# making of spider and legs
while (spider < legs):
  pen.goto(0,20)
  pen.setheading(legdistance*spider)
  pen.forward(legsize)
  spider = spider + 1

# the spider head
pen.penup()
pen.goto(50,50)
pen.pendown()
pen.begin_fill()
pen.circle(25)
pen.end_fill()

#the spider eyes
pen.penup()
pen.goto(45,45)
pen.pendown()
pen.pencolor("purple")
pen.circle(5)
pen.penup()
pen.goto(30,65)
pen.pendown()
pen.pencolor("purple")
pen.circle(5)
# just hiding the turtle
pen.hideturtle() 
wn = trtl.Screen()
wn.mainloop()