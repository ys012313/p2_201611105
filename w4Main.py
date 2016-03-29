import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def makeSwirlSquare(size,angle,bigger,sides):
    for i in range(0,sides):
        if(i%2):
            size=size+bigger
            t1.fd(size)
            t1.right(angle)
        else:
            size=size
            t1.fd(size)
            t1.right(angle)
makeSwirlSquare(10,90,10,20)
wn.exitonclick()