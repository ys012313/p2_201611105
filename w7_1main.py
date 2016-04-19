import turtle

wn=turtle.Screen()

t1=turtle.Turtle()

d=dict()

d=({1:(0,0),2:(25,0),3:(25,25),4:(0,25),5:(0,0)})



def lab7():
	for i in range(1,6):
		t1.setpos(d[i])


def main():
	lab7()


main()

wn.exitonclick()