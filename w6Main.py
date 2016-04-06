import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def Multiple(begin,end):
    sum=0
    for i in range (begin,end):
        if not i%3 or i%5:
            sum=sum+i
	print (sum)

Multiple(1,1001)

wn.exitonclick()