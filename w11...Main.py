import turtle 
wn=turtle.Screen() 
t1=turtle.Turtle() 
import math 
t1.penup() 
t1.goto(0,100) 
t1.pendown() 
t1.circle(100) 
t1.penup() 
t1.home() 
def isIncircle(curpos): 
    radius=100 
    pos=(0,200) 
    if math.sqrt(math.pow(curpos[0]-pos[0],2) + math.pow(curpos[1]-pos[1],2))<=radius: 
        print "True" 
    else: 
        print "False" 
def keyup(): 
    t1.fd(50) 
    curpos=t1.pos() 
    isIncircle(curpos) 
wn.onkey(keyup,"Up") 
def keyleft(): 
    t1.left(90) 
def keyright(): 
    t1.right(90) 
def keydown(): 
    t1.back(30) 
    curpos=t1.pos() 
    isIncircle(curpos) 
wn.onkey(keyleft,"Left") 
wn.onkey(keyright,"Right") 
wn.onkey(keydown,"Down") 
wn.listen() 
wn.exitonclick() 
