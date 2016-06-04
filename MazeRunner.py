import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
import math
import time
timelog=list()
t1.shape("Turtle")

def Maze_1():
    t1.penup()
    t1.goto(-200,200)
    t1.pendown()
    t1.fd(400)
    t1.right(90)
    t1.fd(150)
    t1.right(90)
    t1.penup()
    t1.goto(200,0)
    t1.pendown()
    t1.fd(400)
    t1.right(90)
    t1.fd(150)
    t1.penup()
    t1.goto(-100,200)
    t1.pendown()
    t1.right(180)
    t1.fd(150)
    t1.penup()
    t1.goto(200,150)
    t1.pendown()
    t1.right(90)
    t1.fd(200)
    t1.penup()
    t1.goto(100,0)
    t1.pendown()
    t1.right(90)
    t1.fd(100)
    t1.penup()
    t1.goto(350,-100)
    t1.pendown()
    t1.fillcolor("RED")
    t1.begin_fill()
    t1.fd(50)
    t1.right(90)
    t1.fd(50)
    t1.right(90)
    t1.fd(50)
    t1.right(90)
    t1.fd(50)
    t1.end_fill()
    t1.penup()
    t1.goto(-200,175)
    t1.right(180)
    Time()
    
def Time():
    Time=time.strftime('%M %S')
    Time=Time.split()
    sec=int(Time[0])*60+int(Time[1])
    timelog.append(sec)
    
def Score():
    score=timelog[1]-timelog[0]
    Rank_a=open('Ranking.txt','a')
    Rank_a.write(str(score)+" s\n")
    Rank_a.close()
    Rank_r=open('Ranking.txt','r')
    for line in Rank_r:
        print line
    Rank_r.close()

def Maze_2():
    t1.penup()
    t1.goto(-250,250)
    t1.pendown()
    t1.fd(500)
    t1.right(90)
    t1.fd(250)
    t1.right(90)
    t1.penup()
    t1.goto(250,-50)
    t1.pendown()
    t1.fd(500)
    t1.right(90)
    t1.fd(250)
    t1.penup()
    t1.goto(-180,250)
    t1.pendown()
    t1.right(180)
    t1.fd(80)
    t1.penup()
    t1.goto(50,250)
    t1.pendown()
    t1.fd(150)
    t1.penup()
    t1.goto(250,190)
    t1.pendown()
    t1.right(90)
    t1.fd(100)
    t1.penup()
    t1.goto(150,-50)
    t1.pendown()
    t1.right(90)
    t1.fd(180)
    t1.penup()
    t1.goto(-50,-50)
    t1.pendown()
    t1.fd(150)
    t1.back(60)
    t1.right(90)
    t1.fd(100)
    t1.penup()
    t1.goto(-250,10)
    t1.pendown()
    t1.fd(100)
    t1.penup()
    t1.goto(-250,130)
    t1.pendown()
    t1.fd(150)
    t1.left(90)
    t1.fd(80)
    t1.penup()
    t1.goto(350,-100)
    t1.pendown()
    t1.fillcolor("ORANGE")
    t1.begin_fill()
    t1.fd(50)
    t1.right(90)
    t1.fd(50)
    t1.right(90)
    t1.fd(50)
    t1.right(90)
    t1.fd(50)
    t1.end_fill()
    t1.penup()
    t1.goto(-250,225)
    t1.right(180)
    Time()
    
def Time():
    Time=time.strftime('%M %S')
    Time=Time.split()
    sec=int(Time[0])*60+int(Time[1])
    timelog.append(sec)

def Maze_3():
    t1.penup()
    t1.goto(-300,300)
    t1.pendown()
    t1.fd(600)
    t1.right(90)
    t1.fd(350)
    t1.right(90)
    t1.penup()
    t1.goto(300,-100)
    t1.pendown()
    t1.fd(600)
    t1.right(90)
    t1.fd(350)
    t1.penup()
    t1.goto(-200,300)
    t1.pendown()
    t1.right(180)
    t1.fd(100)
    t1.penup()
    t1.goto(100,300)
    t1.pendown()
    t1.fd(100)
    t1.penup()
    t1.goto(300,0)
    t1.pendown()
    t1.right(90)
    t1.fd(200)
    t1.penup()
    t1.goto(100,-100)
    t1.pendown()
    t1.right(90)
    t1.fd(80)
    t1.penup()
    t1.goto(-100,-100)
    t1.pendown()
    t1.fd(300)
    t1.penup()
    t1.goto(-300,0)
    t1.pendown()
    t1.right(90)
    t1.fd(50)
    t1.penup()
    t1.goto(-200,50)
    t1.pendown()
    t1.fillcolor("RED")
    t1.begin_fill()
    t1.circle(50)
    t1.end_fill()
    t1.penup()
    t1.goto(0,0)
    t1.pendown()
    t1.fillcolor("ORANGE")
    t1.begin_fill()
    t1.circle(80)
    t1.end_fill()
    t1.penup()
    t1.goto(200,40)
    t1.pendown()
    t1.fillcolor("GREEN")
    t1.begin_fill()
    t1.circle(60)
    t1.end_fill()
    t1.penup()
    t1.goto(350,-100)
    t1.pendown()
    t1.fillcolor("BLUE")
    t1.begin_fill()
    t1.left(90)
    t1.fd(50)
    t1.right(90)
    t1.fd(50)
    t1.right(90)
    t1.fd(50)
    t1.right(90)
    t1.fd(50)
    t1.end_fill()
    t1.penup()
    t1.goto(-300,275)
    t1.right(180)
    Time()
    
def Time():
    Time=time.strftime('%M %S')
    Time=Time.split()
    sec=int(Time[0])*60+int(Time[1])
    timelog.append(sec)

def RSPGame():
    print "Let's start rock scissors paper game"
    Player1 = raw_input("P1 : ")
    Player2 = raw_input("P2 : ")
    if(Player1==Player2):
        print "Draw"
        print "play miro 2!!!"
        Maze_2()
    elif(Player1=="S"):
        if(Player2=="P"):
            print 'Player1 Win'
            Maze_1()
        elif(Player2=="R"):
            print 'Player2 Win'
            print "p1 lose.."
            Maze_3()
    elif(Player1=="R"):
        if(Player2=="S"):
            print 'Player1 Win'
            Maze_1()
        elif(Player2=="P"):
            print 'Player2 Win'
            print "p1 lose.."
            Maze_3()
    elif(Player1=="P"):
        if(Player2=="S"):
            print 'Player2 Win'
            print "p1 lose.."
            Maze_3()
        elif(Player2=="R"):
            print 'Player1 Win'
            Maze_1()
    else:
        print 'Input Error'

def isInCircle(center,radius,pos):
    return 0<math.sqrt(math.pow(center[0]-pos[0],2) + math.pow(center[1]-pos[1],2))<radius

def isInRectangle(curpos,coord):
    xs=coord[0][0]
    xe=coord[1][0]
    ys=coord[0][1]
    ye=coord[1][1]
    return xs<=curpos[0]<=xe and ys<=curpos[1]<=ye

def keyup():
    pos=t1.pos()
    t1.forward(20)
    if isInCircle((-200,100),50,pos):
        t1.goto(-300,275)
    elif isInCircle((0,80),80,pos):
	t1.goto(-300,275)
    elif isInCircle((200,100),60,pos):
	t1.goto(-300,275)
    elif isInRectangle(pos,((350,-100),(400,-50))):
        t1.write("FINISH")
        print "You Win!"
        Time()
        Score()
def keyleft():
    t1.left(45)

def keyright():
    t1.right(45)

def keydown():
    pos=t1.pos()
    t1.forward(20)
    if isInCircle((-200,100),50,pos):
        t1.goto(-300,275)
    elif isInCircle((0,80),80,pos):
	t1.goto(-300,275)
    elif isInCircle((200,100),60,pos):
	t1.goto(-300,275)
    elif isInRectangle(pos,((350,-100),(400,-50))):
        t1.write("FINISH")
        print "You Win!"
        Time()
        Score()
def addKeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keyleft, "Left")
    wn.onkey(keyright, "Right")
    wn.onkey(keydown, "Down")
def gamePlay():
    RSPGame()
    addKeys()
    wn.listen()
    turtle.mainloop()      
gamePlay()