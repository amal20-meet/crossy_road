from turtle import *
import turtle
import time

class Character(Turtle):
	def __init__(self,x,y,shape,step):
		Turtle.__init__(self)
		self.penup()
		self.step = step
		self.shape(shape)
		self.goto(x,y)
	def go_up(self):
		self.seth(90)
		self.forward(self.step)
	def go_down(self):
		self.seth(270)
		self.forward(self.step)
	def go_left(self):
		self.seth(180)
		self.forward(self.step)
	def go_right(self):
		self.seth(0)
		self.forward(self.step)

character = Character(100,100,"circle",50)

turtle.onkey(character.go_up, "Up")
turtle.onkey(character.go_down, "Down")
turtle.onkey(character.go_right, "Right")
turtle.onkey(character.go_left, "Left")
turtle.listen()
turtle.mainloop()