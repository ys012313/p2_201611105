import turtle 
wn=turtle.Screen() 
wn.bgpic("myMaze.gif")
t1=turtle.Turtle() 
line=turtle.Turtle() 
 
 
 
def keyup(): 
    t1.fd(50) 
def keydown(): 
    t1.backward(50) 
def keyright(): 
    t1.right(90) 
def keyleft(): 
    t1.left(90) 
 
 
def mousegoto(x,y): 
    t1.setpos(x,y) 
 
 
def Arrive(x,y): 
    t1.setpos(x,y) 
    if t1.xcor()>=0 and t1.xcor()<=100 and t1.ycor()==0: 
        print "Arrive!" 
def addKeys(): 
    wn.onkey(keyup,"Up") 
    wn.onkey(keydown,"Down") 
    wn.onkey(keyleft,"Left") 
    wn.onkey(keyright,"Right") 
    wn.onkey(wn.bye,"q") 

 
def addMouse(): 
    wn.onclick(mousegoto) 
    wn.onclick(Arrive) 
 
 
def lab11(): 
    line.goto(100,0) 
    t1.penup() 
    t1.goto(-350, 350) 
    t1.pendown() 
    addKeys() 
    addMouse() 
    wn.listen() 
    turtle.mainloop() 

 
lab11() 
