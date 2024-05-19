from p5 import *
import time

def setup():  
	global x,y,velocityX,velocityY, accelerationY,imageCounter, leftorright, maliostand
	imageCounter = 0
	velocityX = 0
	maliostand = True
	velocityY = 0
	accelerationY = -1
	leftorright = 'right'
	x = 0
	y = 400
	createCanvas(windowWidth, windowHeight)
	loadImage("Stand.png","stand")
	loadImage("W2.svg","walk2")
	loadImage("W1.png","walk1")
	loadImage("W3.svg","walk3")
	loadImage("Jump.png","jump")
	loadImage("b2.svg", "b2")
	
def draw():
	global x,y,velocityX,velocityY, accelerationY, imageCounter,leftorright, maliostand
	
	background('black')
	drawTickAxes()
	image(assets["b2"],0,0)
 #70

	mario()

	fill("white")
	text(velocityY, 200, 200)


	

def didCollideWithFloor(marioX, marioY, floorX, floorY, floorW, floorH):
	isBetweenLeftAndRight = marioX >= floorX and marioX <= floorX + floorW
	isBetweenTopAndBottom = marioY >= floorY and marioY <= floorY + floorH
	if isBetweenLeftAndRight and isBetweenTopAndBottom:
		return True
	else:
		return False

def keyPressed():
	global velocityY, y,x
	if keyCode == 38 and didCollideWithFloor(x,y,0, 0, 496, 75): # up arrow 
		velocityY = 30
# sheep



def mario():
	global x,y,velocityX,velocityY, accelerationY, imageCounter,leftorright, maliostand
	y+=velocityY


	x+=velocityX
	# if 1 > velocityY:
	velocityX*=0.87
	accelerationY = -1

	velocityY += accelerationY
	
	#velocityY*=0.87
	if (didCollideWithFloor(x,y,0, 0, 496, 61)):
		y = 61
		velocityY = -(velocityY * 2/3)

	# rect(200,300,100,60)
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
			translate(x * 2 + 43, 0)
			scale(-1, 1)
			leftorright = 'right'
			velocityX+=1
			image(assets["jump"],x,y,47,46)
		pop()

	if not keyIsDown(LEFT_ARROW) and not keyIsDown(RIGHT_ARROW) and not y > 60:
		imageCounter = 0
		maliostand = True
		if leftorright == 'right':
			image(assets["stand"],x,y,34,45)

		else:

			maliostand = True
			translate(x * 2 + 43, 0)
			scale(-1, 1)
			image(assets["stand"],x,y,34,45)
			maliostand = True
	if keyIsDown(RIGHT_ARROW) and not keyIsDown(UP_ARROW):
		leftorright = 'right'
		velocityX+=1
		imageCounter+=1
		maliostand = False
		if imageCounter < 7:
			image(assets["walk1"],x,y,43,46)
		elif imageCounter < 14:
			image(assets["walk2"],x,y,40.5,46.5)
		elif imageCounter < 21:
			image(assets["walk3"],x,y,34.5,46.5)
		elif imageCounter < 28:
			image(assets["walk1"],x,y,36,45)
		else:
			image(assets["walk1"],x,y,43,46)
			imageCounter = 0

	if keyIsDown(LEFT_ARROW) and not keyIsDown(UP_ARROW):
		push()
		translate(x * 2 + 43, 0)
		scale(-1, 1)
		maliostand = False
		leftorright = 'left'
		velocityX-=1
		imageCounter+=1
		if imageCounter < 7:
			image(assets["walk1"],x,y,43,46)
		elif imageCounter < 14:
			image(assets["walk2"],x,y,40.5,46.5)
		elif imageCounter < 21:
			image(assets["walk3"],x,y,34.5,46.5)
		elif imageCounter < 28:
			image(assets["walk1"],x,y,36,45)
		else:
		#LINE 111 🔥🔥🔥
			image(assets["walk1"],x,y,43,46)
			imageCounter = 0
		pop()

	if y > 60 and not keyIsDown(LEFT_ARROW) and not keyIsDown(RIGHT_ARROW):
		push()
		if leftorright == 'right':
			translate(x * 2 + 43, 0)
			scale(-1, 1)
			image(assets["jump"],x,y,47,46)
		if leftorright == 'left':
			scale(1, 1)
			image(assets["jump"],x,y,47,46)
		pop()
