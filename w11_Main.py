 import turtle

 wn=turtle.Screen()

 t1=turtle.Turtle()

 def Touchline():
     t1.penup()
     t1.goto(-50,50)
     t1.pendown()
     t1.fd(100)
     t1.penup()
     t1.home()


 def keyup():
     t1.fd(50)
     (x,y)=t1.pos()
     if (-50<x<50 and y==50):
         print "Touch!"


 def keyback():
     t1.back(50)
     (x,y)=t1.pos()
     if (-50<x<50 and y==50):
         print "Touch!"


 def keyright():
     t1.right(90)


 def keyleft():
     t1.left(90)


 def mousegoto(x,y):
     t1.setpos(x,y)
     (x,y)=t1.pos()
     if (-50<x<50 and y==50):
         print "Touch!"


 def addKeys():
     wn.onkey(keyup,"Up")
     wn.onkey(keyback,"Down")
     wn.onkey(keyright,"Right")
     wn.onkey(keyleft,"Left")
     wn.onkey(wn.bye,"q")


 def addMouse():
     wn.onclick(mousegoto)


 def lab11():
     Touchline()
     addKeys()
     addMouse()
     wn.listen()
     turtle.mainloop()


 lab11()