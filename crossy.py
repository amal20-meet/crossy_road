import turtle
from turtle import Turtle
import random
screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2
turtle.bgpic("road.gif")
#comment
turtle.setup(screen_width *2, screen_height*2)
rSPEED = 25
rCOLOR = (random.random(),random.random(),random.random()) 
rPOSITION = (3,8)
rWIDTH = 11
class Car(Turtle):
	def __init__(self,speed,color,pos,width):
		Turtle.__init__(self)
		self.penup()
		self.speed(speed)
		self.speed = speed
		self.color(color)
		self.shape("square")
		self.car_pos = pos
		self.goto(pos)
		self.shapesize(1,width,None)
		self.car_width = width
	def move(self):
		if self.car_pos[0]<screen_width+(self.car_width*10) and self.car_pos[0]>-(screen_width+(self.car_width*10)):
			self.goto(self.car_pos[0]+self.speed, self.car_pos[1])
			self.car_pos = self.pos()
		else:
			print("out of screen")
			if self.speed > 0:
				self.new_car((-(screen_width+(self.car_width*10)),self.car_pos[1]))
				while self.car_pos[0]<-screen_width:
					self.goto(self.car_pos[0]+self.speed, self.car_pos[1])
					self.car_pos = self.pos()
			else:
				self.new_car((screen_width+(self.car_width*10),self.car_pos[1]))
				while self.car_pos[0]>screen_width:
					self.goto(self.car_pos[0]+self.speed, self.car_pos[1])
					self.car_pos = self.pos()
	def new_car(self,pos):
		self.car_pos = pos

	'''def choose_color():
		self.color'''
def show_coordination(x, y):
	print(str(x)+","+str(y))

turtle.onscreenclick(show_coordination)
speed = [3,-5,5,-3,4,-4,3.5,-3.5,4.2,-4.2]
colors = ["purple","lime","lavender","cyan","salmon","gold","lawngreen"]
CarStaringPos = [(-248,283),(-212,130),(-320,-41),(-280,-170),(-310,-295),(3,8)]
CARS = []
for i in range(len(CarStaringPos)):
	car = Car(speed[i], colors[i], CarStaringPos[i], rWIDTH)
	CARS.append(car)

while True:
	for car in CARS:
		car.move()



turtle.mainloop()
