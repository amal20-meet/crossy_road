import turtle
from characters import *
from turtle import Turtle
import random
import math
tracer(0.7)
screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2

#game over pic

running = True

bg=turtle.clone()
turtle.setup(width=762,height=762)


NUMBER_OF_STREETS = 10
STREET_WIDTH = screen_height/NUMBER_OF_STREETS
MINIMUM_CARS = 1
MAXIMUM_CARS = 3
CARS = []
print(turtle.pos())

class Car(Turtle):
	def __init__(self,speed,color,pos,width,level):
		Turtle.__init__(self)
		self.penup()
		self.speed(speed)
		self.car_speed = speed
		self.color(color)
		self.shape("square")
		self.car_pos = pos
		self.goto(pos)
		self.shapesize(1,width,None)
		self.car_width = width
		self.level = level
		update()
	def move(self):
		if self.car_pos[0]<screen_width+(self.car_width*10) and self.car_pos[0]>-(screen_width+(self.car_width*10)):
			self.goto(self.car_pos[0]+self.car_speed, self.car_pos[1])
			self.car_pos = self.pos()
		else:
			print("out of screen")
			if self.car_speed > 0:
				self.new_car((-(screen_width+(self.car_width*10)),self.car_pos[1]))
				while self.car_pos[0]<-screen_width:
					self.goto(self.car_pos[0]+self.car_speed, self.car_pos[1])
					self.car_pos = self.pos()
			else:
				self.new_car((screen_width+(self.car_width*10),self.car_pos[1]))
				while self.car_pos[0]>screen_width:
					self.goto(self.car_pos[0]+self.car_speed, self.car_pos[1])
					self.car_pos = self.pos()
	def new_car(self,pos):
		self.car_pos = pos
		self.ht()
		self.speed(0)
		self.goto(self.car_pos)
		self.st()
		update()

class Street(Turtle):
	def __init__(self,stype,level,width):
		Turtle.__init__(self)
		self.pu()
		self.goto(0,-screen_width+(level+0.5)*width)
		self.isStreet = stype
		self.level = level
		self.width = width
		self.shape("square")
		self.shapesize(self.width/10,screen_width,None)
		if self.isStreet == 1:
			self.color("dark slate grey")
			self.number_of_cars = random.randint(MINIMUM_CARS,MAXIMUM_CARS)
		else:
			self.color("green2")
			self.number_of_cars = 0
		self.cars = []
		for i in range(self.number_of_cars):
			rSPEED = random.randint(-15,15)
			while (rSPEED > -10 and rSPEED <= 0) or (rSPEED < 10 and rSPEED >= 0):
				rSPEED = random.randint(-15,15)
			rCOLOR = (random.random(),random.random(),random.random())
			rPOS = (random.randint(-screen_width/2,screen_width/2),-screen_width+(level)*width)
			rWIDTH = random.randint(5,10)
			car = Car(rSPEED,rCOLOR,rPOS,rWIDTH,self.level)
			self.cars.append(car)
			CARS.append(car)
			update()


STREETS = []
for i in range(NUMBER_OF_STREETS*2):
	random_street_type = random.randint(0,3)
	if random_street_type>0:
		random_street_type=1
	street = Street(random_street_type,i+1,STREET_WIDTH)
	STREETS.append(street)
	update()

LANES = []
for i in STREETS:
	if i.isStreet == 0:
		LANES.append(i)
starting_lane = LANES[0]		
character = Character(0,0,"circle",50,starting_lane.level)
character.pd()
update()
turtle.onkey(character.go_up, "Up")
turtle.onkey(character.go_down, "Down")
turtle.onkey(character.go_right, "Right")
turtle.onkey(character.go_left, "Left")
turtle.listen()
update()
def collide(car, character):
	if car.level == character.level:
		if car.car_width*5+character.r >= math.fabs((car.pos()[0])-(character.pos()[0])):
			return True
		else:
			return False
	else:
		return False
update()
	



while running:
	for car in CARS:
		car.move()
		update()
		if collide(car, character):
			turtle.clone()
			running = False
			turtle.clearscreen()
			turtle.register_shape('gameover1.gif')
			turtle.shape("gameover1.gif")
			update()


'''rSPEED = 25
=======
turtle.bgpic("road.gif")
#comment
turtle.setup(screen_width *2, screen_height*2)
rSPEED = 25
>>>>>>> 7bb0e11dbb768d8202cfeed7a6b85c78104076bf
rCOLOR = (random.random(),random.random(),random.random()) 
rPOSITION = (3,8)
rWIDTH = 11
class Car(Turtle):
	def __init__(self,speed,color,pos,width):
		Turtle.__init__(self)
		self.penup()
		self.speed(speed)
		self.car_speed = speed
		self.color(color)
		self.shape("square")
		self.car_pos = pos
		self.goto(pos)
		self.shapesize(1,width,None)
		self.car_width = width
	def move(self):
		if self.car_pos[0]<screen_width+(self.car_width*10) and self.car_pos[0]>-(screen_width+(self.car_width*10)):
			self.goto(self.car_pos[0]+self.car_speed, self.car_pos[1])
			self.car_pos = self.pos()
		else:
			print("out of screen")
			if self.car_speed > 0:
				self.new_car((-(screen_width+(self.car_width*10)),self.car_pos[1]))
				while self.car_pos[0]<-screen_width:
					self.goto(self.car_pos[0]+self.car_speed, self.car_pos[1])
					self.car_pos = self.pos()
			else:
				self.new_car((screen_width+(self.car_width*10),self.car_pos[1]))
				while self.car_pos[0]>screen_width:
					self.goto(self.car_pos[0]+self.car_speed, self.car_pos[1])
					self.car_pos = self.pos()
	def new_car(self,pos):
		self.car_pos = pos
		self.ht()
		self.speed(0)
		self.goto(self.car_pos)
		self.st()'''

'''def choose_color():
		self.color'''
'''def show_coordination(x, y):
	print(str(x)+","+str(y))

turtle.onscreenclick(show_coordination)
speed = [3,-5,5,-3,4,-4,3.5,-3.5,4.2,-4.2]
colors = ["purple","lime","lavender","cyan","salmon","blue","lawngreen"]
CarStaringPos = [(-248,283),(-212,130),(-320,-41),(-280,-170),(-310,-295),(3,8)]
CARS = []
for i in range(len(CarStaringPos)):
	car = Car(speed[i], colors[i], CarStaringPos[i], rWIDTH)
	CARS.append(car)

while True:
	turtle.bgcolor("red")
	for car in CARS:
		car.move()


<<<<<<< HEAD
'''
turtle.mainloop()
