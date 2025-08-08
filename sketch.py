from p5 import *

def setup():
  createCanvas(500,500)
  global x,speedx, y, speedy
  x = 250
  speedx= random(1,5)
  y = 250 
  speedy= random(1,5)
  background("black")
  colorMode(HSB)
  #HUE
  #SATURATION
  #BRIGHTNESS
def draw():
  global x, speedx, y, speedy
  

  drawTickAxes()
  #fill(random(0,255))  #greyscale
  fill(x%250,y%250,(x*y)%250)
  noStroke()
  circle(x,y,75)
  x = x - speedx
  y = y + speedy 
  
  if x<=37.5:
    speedx= -speedx

  if x>=500-37.5:
    speedx = -speedx

  if y<=0+37.5:
    speedy = -speedy 

  if y>500-37.5:
    speedy = -speedy
    
