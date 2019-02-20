import turtle
from turtle import Turtle
screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2

turtle.setup(screen_width *2, screen_height*2)
rSPEED = 
rCOLOR = 
rPOSITION = 
rWIDTH = 
class Car(Turtle):
	def __init__(self,speed,color,pos,width):
		Turtle.__init__(self)
		self.penup()
		self.speed(speed)
		self.color(color)
		self.shape("square")
		self.goto(pos)
		self.shapesize(1,width,None)
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

	def choose_color():
		self.
def show_coordination(x, y):
	print(str(x)+","+str(y))

turtle.onscreenclick(show_coordination)

colors = ["purple","lime","lavender","cyan","salmon","gold","lawngreen"]

CARS = []
for i in range(20):
	c = Car(rSPEED, rCOLOR, rPOSITION, rWIDTH)
	CARS.append(c)

while True:
	for c in CARS:
		c.move()


turtle.mainloop()