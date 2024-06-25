from p5 import *
import time

def setup():  
	global x,y,velocityX,velocityY, accelerationY,imageCounter, leftorright, maliostand,enemy
	global floorWidth, floorHeight, floorList,floorsofgoomblaList,listofgoomblas
	imageCounter = 0
	velocityX = 0
	maliostand = True
	velocityY = 0
	accelerationY = -1
	leftorright = 'right'
	x = 0
	y = 400
	floorWidth = 989
	floorHeight = 64
	floorList = []
	floorsofgoomblaList = []
	listofgoomblas = []
	enemy =2
	decidegoombla()
	createFloors()
	createCanvas(windowWidth, windowHeight)
	loadImage("Stand.png","stand")
	loadImage("W2.svg","walk2")
	loadImage("W1.png","walk1")
	loadImage("W3.svg","walk3")
	loadImage("Jump.png","jump")
	loadImage("ground (1).svg", "b2")
	loadImage("goomba-waddle.png", "goomba")
	loadImage("goomba-waddle1.png", "goomba1")

def createFloors():
	global floorList
	for i in range(1000):
		floor = Floor(i*64, 0, 64, 64)
		floorList.append(floor)
		if i in floorsofgoomblaList:
			#create a goombla
			goombla = Goomba(i*64,64)
			listofgoomblas.append(goombla)
			

def draw():
	global x,y,velocityX,velocityY, accelerationY, imageCounter,leftorright, maliostan,enemy
	global floorWidth, floorHeight,floorList

	translate(-x,0)
	# x%=30
	background('skyblue')
	paintGoomblas()
	#drawTickAxes()
	# image(assets["b2"],0,0)
	# floor = Floor(0,0,floorWidth,floorHeight)
	# floor.drawFloor()
	drawFloors()
 #70
	text(f"list of goomblas: {len(listofgoomblas)}",200,300);
	text(len(floorsofgoomblaList),350,405);
	x += 3
	# push()
	# translate(x+2, 0)
	mario()
	# pop()

	fill("white")
	text(velocityY, 200, 200)

def drawFloors():
	global floorList
	for floor in floorList:
		floor.drawFloor()
		
def paintGoomblas():
	global listofgoomblas
	for goomba in listofgoomblas:
		goomba.paintgoombla()
	
		
def decidegoombla():
	global floorsofgoomblaList
	for i in range(1000):
		if int(random(1,4)) == 3:
			floorsofgoomblaList.append(i) 

			
			
	

def didCollideWithFloors(x,y,SHEEEP,SHEEP,SHEP,SHP):
	# for all floors, check if mario collided
	for floor in floorList:
		if didCollideWithFloor(x,y, floor.x, floor.y, floor.w, floor.h):
			return True
	
	return False

def didCollideWithFloor(marioX, marioY, floorX, floorY, floorW, floorH):
	isBetweenLeftAndRight = marioX >= floorX and marioX <= floorX + floorW
	isBetweenTopAndBottom = marioY >= floorY and marioY <= floorY + floorH
	if isBetweenLeftAndRight and isBetweenTopAndBottom:
		return True
	else:
		return False

def keyPressed():
	global velocityY, y,x
	global floorWidth, floorHeight
	if keyCode == 38 and didCollideWithFloors(x,y,0, 0, floorWidth, floorHeight): # up arrow 
		velocityY = 30
# sheep



def mario():
	global x,y,velocityX,velocityY, accelerationY, imageCounter,leftorright, maliostand
	global floorWidth, floorHeight, floorList
	y+=velocityY


	x+=velocityX
	# if 1 > velocityY:
	velocityX*=0.87
	accelerationY = -1



	velocityY += accelerationY

	if (y < floorHeight + 2):
		y = floorHeight

	#velocityY*=0.87
	if (didCollideWithFloors(x,y,0, 0, floorWidth, floorHeight)):
		velocityY = -(velocityY * 2/3)

	
	# rect(200,300,100,60)
	#LINE 111 🔥🔥🔥
	text(imageCounter, 400,400)

	if not maliostand == True:

		if keyIsDown(LEFT_ARROW) and y > 61:
			push()
			leftorright = 'left'
			velocityX-=1
			image(assets["jump"],x,y,47,46)
			pop()
		if keyIsDown(RIGHT_ARROW) and y > 61:
			push()
			translate(x * 2 + 200, 0)
			scale(-1, 1)
			leftorright = 'right'
			velocityX+=1
			image(assets["jump"],x,y,47,46)
		pop()
	# if y > 60 and not keyIsDown(LEFT_ARROW) and not keyIsDown(RIGHT_ARROW):
	# 	push()
	# 	if leftorright == 'right':
	# 		translate(x * 2 + 43, 0)
	# 		scale(-1, 1)
	# 	if leftorright == 'left':
	# 		scale(1, 1)
	# 		image(assets["jump"],x,y,47,46)
	# 	pop()

		
	if imageCounter < 5:
		image(assets["walk1"],x,y,40,46)
		imageCounter+=1
	elif imageCounter < 10:
		image(assets["walk2"],x,y,40.5,46)
		imageCounter+=1
	elif imageCounter < 15:
		image(assets["walk3"],x,y,36,46)
		imageCounter+=1
	elif imageCounter < 20:
		image(assets["walk1"],x,y,40,46)
		imageCounter+=1
		imageCounter = 0
	else:
		image(assets["walk1"],x,y,40,46)
		imageCounter+=1
		imageCounter = 0


	




class Floor:
	def __init__(self, x,y,w,h):
		# create these variables
		self.x = x
		self.y = y
		self.w = w
		self.h = h

	def drawFloor(self):
		image(assets["b2"],self.x,self.y,self.w,self.h)
		


# maybe do this in setup
# create the floor

# floorWidth = 989
# floorHeight = 61

# floorList = []
							

	#floorList.append(floor)





# -1 Sheep
# 0. create class for enemy
# 1. Create a subclass for Goomba
# 2. create a function which creates goombas, placing them randomly
# 3. Add the created goombas to a list to keep track of them
# 4. In draw, use a for loop going through the list of Goombas and draw them

class Enemy:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		
class Goomba(Enemy):
	def __init__(self,x,y):
		super().__init__(x,y)
		
	def paintgoombla(self):
		image(assets["goomba"],self.x,self.y, 50, 50)
	





















































































































































































































































































































































































































































































































































































































































































































































































# if not keyIsDown(LEFT_ARROW) and not keyIsDown(RIGHT_ARROW) and not y > 60:
# 	imageCounter = 0
# 	maliostand = True
# 	if leftorright == 'right':
# 		image(assets["stand"],x,y,34,45)

# 	else:

# 		maliostand = True
# 		translate(x * 2 + 43, 0)
# 		scale(-1, 1)
# 		image(assets["stand"],x,y,34,45)
# 		maliostand = True
# if keyIsDown(RIGHT_ARROW) and not keyIsDown(UP_ARROW):
# 	leftorright = 'right'
# 	velocityX+=1
# 	imageCounter+=1
# 	maliostand = False
# 	if imageCounter < 7:
# 		image(assets["walk1"],x,y,43,46)
# 	elif imageCounter < 14:
# 		image(assets["walk2"],x,y,40.5,46.5)
# 	elif imageCounter < 21:
# 		image(assets["walk3"],x,y,34.5,46.5)
# 	elif imageCounter < 28:
# 		image(assets["walk1"],x,y,36,45)
# 	else:
# 		image(assets["walk1"],x,y,43,46)
# 		imageCounter = 0

# if keyIsDown(LEFT_ARROW) and not keyIsDown(UP_ARROW):
# 	push()
# 	translate(x * 2 + 43, 0)
# 	scale(-1, 1)
# 	maliostand = False
# 	leftorright = 'left'
# 	velocityX-=1
# 	imageCounter+=1
# 	if imageCounter < 7:
# 		image(assets["walk1"],x,y,43,46)
# 	elif imageCounter < 14:
# 		image(assets["walk2"],x,y,40.5,46.5)
# 	elif imageCounter < 21:
# 		image(assets["walk3"],x,y,34.5,46.5)
# 	elif imageCounter < 28:
# 		image(assets["walk1"],x,y,36,45)
# 	else:
# 		image(assets["walk1"],x,y,43,46)
# 		imageCounter = 0
# 	pop()