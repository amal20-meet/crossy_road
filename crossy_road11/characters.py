from turtle import *
import turtle
import time

screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2
NUMBER_OF_STREETS = 10
width = screen_height/NUMBER_OF_STREETS

class Character(Turtle):
	def __init__(self,x,y,shape,step,level):
		Turtle.__init__(self)
		self.penup()
		self.step = step
		self.shape(shape)
		self.level = level
		self.r = 10
		self.shapesize(self.r/10)
		self.goto(x,-screen_width+(self.level)*width)
		update()
	def go_up(self):
		self.seth(90)
		if self.level != 20:
			self.level+=1
		else:
			self.level+=1
			self.goto(self.pos()[0],-screen_width+(self.level)*width)
			self.level = 2
			self.ht()
		self.goto(self.pos()[0],-screen_width+(self.level)*width)
		update()
		self.st()
	def go_down(self):
		self.seth(270)
		if self.level > 2:
			self.level-=1
		else:
			self.level-=1
			self.goto(self.pos()[0],-screen_width+(self.level)*width)
			self.level = 20
			self.ht()
		self.goto(self.pos()[0],-screen_width+(self.level)*width)
		self.st()
	def go_left(self):
		self.seth(180)
		self.forward(self.step)
	def go_right(self):
		self.seth(0)
		self.forward(self.step)



