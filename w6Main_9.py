import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def lab6():
     year=raw_input("input year: ")
     year=int(year)
     if(year%4==0):
         print "Leap year"
     else:
         print "Not Leap year"


def main():
     lab6()


 main()
t1.exitonclick()