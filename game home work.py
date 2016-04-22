def game():
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    t1.shape("turtle")
    import random
    A = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    B = random.sample(A,3)
    C = set()
    D = (0,0)
    while D != D < (100,0) or D != D > (-100,0) :
        p1 = input('Give me random a number. (From 1 to 10)')
        p2 = input('Give me random other number. (From 1 to 10)')
        p3 = input('Give me random another number. (From 1 to 10)') 
        C.add(p1)
        C.add(p2)
        C.add(p3) 
        print B
        print C
        E = C & set(B)
        print E
        if(len(E))== 0: 
            D = D + (-30,0)
            print "All wroung!"
        elif(len(E))== 1:
            D = D + (10,0)
            print "You got only 1"
        elif(len(E))== 2:
            D = D + (30,0)
            print "You got 2"
        elif(len(E))== 3:
            D = D + (50,0)
            print "All correct!"

game()