import turtle 
wn=turtle.Screen()  
t1=turtle.Turtle()
def saveTracks():
    tracks=list()
    t1.speed(1) 
    t1.penup() 
    t1.goto(-400,300)
    t1.pendown() 
    t1.pencolor("Red") 
    t1.right(90) 
    t1.fd(400)
    tracks.append(t1.pos())
    t1.backward(150)
    tracks.append(t1.pos())
    t1.left(90) 
    t1.fd(300)
    tracks.append(t1.pos())
    t1.left(90) 
    t1.fd(300)
    tracks.append(t1.pos())
    t1.back(150)
    tracks.append(t1.pos())
    t1.right(90) 
    t1.fd(300)
    tracks.append(t1.pos())
    t1.left(90) 
    t1.right(90) 
    t1.right(90) 
    t1.fd(200)
    tracks.append(t1.pos())
    t1.fd(300)
    tracks.append(t1.pos())
    t1.back(100)
    tracks.append(t1.pos())
    t1.left(90) 
    t1.fd(200)
    tracks.append(t1.pos())
    return tracks

def replayTracks(tracks):
    t1.penup()
    t1.goto(-400,300)
    t1.pendown()
    t1.pencolor("RED")
    for i in mytracks:
            t1.goto(i)
def lab7():
    tracks=saveTracks()
    replayTracks(tracks)
    
def main():
    lab7()

main()

wn.exitonclick()