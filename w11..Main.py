import turtle 
wn=turtle.Screen() 
t1=turtle.Turtle() 
def isInRectangle(curpos,coord): 
    xs=coord[0][0] 
    xe=coord[1][0] 
    ys=coord[0][1] 
    ye=coord[1][1] 
    if (xs <= curpos[0] <= xe and ys <= curpos[1] <=ye): 
        print ("True") 
    else: 
        print ("False") 
coord=[(100,100),(150,150)] 
t1.penup() 
t1.goto(100,100) 
t1.pendown() 
for i in range(4): 
	t1.fd(50) 
	t1.lt(90) 
t1.penup() 
t1.home() 
def keyup(): 
    t1.fd(30) 
    curpos=t1.pos() 
    isInRectangle(curpos,coord) 
wn.onkey(keyup,"Up") 
def keyleft(): 
    t1.left(90) 
def keyright(): 
    t1.right(90) 
def keydown(): 
    t1.back(30) 
    curpos=t1.pos() 
    isInRectangle(curpos,coord) 
wn.onkey(keyleft,"Left") 
wn.onkey(keyright,"Right") 
wn.onkey(keydown,"Down") 
wn.listen() 

 
wn.exitonclick()  

