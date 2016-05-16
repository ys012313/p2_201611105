import turtle 
wn=turtle.Screen() 
t1=turtle.Turtle() 
coord = [(100,100),(200,200)] 
xs=coord[0][0] 
ys=coord[0][1] 
xe=coord[1][0] 
ye=coord[1][1] 

 
def Sqaure(): 
    t1.penup() 
    t1.goto(50,50) 
    t1.pendown() 
    for i in range(0,4): 
        t1.fd(100) 
        t1.left(90) 
    t1.penup() 
    t1.home() 
def isinRectangle(coord,curpos): 
    if xs<=curpos[0]<=xe and ys<=curpos[1]<=ye: 
        t1.color("red") 
        Square() 
 
def keyup(): 
    t1.fd(50) 
    curpos=t1.pos() 
    isinRectangle(coord,curpos) 

def keydown(): 
    t1.back(50) 

def keyright(): 
    t1.right(90) 

def keyleft(): 
    t1.left(90) 

def mousegoto(x,y): 
    t1.setpos(x,y) 
    curpos=t1.pos() 
    isinRectangle(coord,curpos) 

def addkeys(): 
    wn.onkey(keyup, "Up") 
    wn.onkey(keydown, "Down") 
    wn.onkey(keyright, "Right") 
    wn.onkey(keyleft, "Left") 

def addmouse(): 
    wn.onclick(mousegoto) 

def lab11():
    addkeys() 
    addmouse() 
    wn.listen() 
    turtle.mainloop() 
