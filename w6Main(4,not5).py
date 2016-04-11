x=list()

def sumLIST(x):
    x=list()
    for i in range(0,1000):
        if i%4==0 and not i%5==0:
            x.append(i)
    sum=0
    for i in range(0,len(x)):
        sum+=x[i]
    return sum


def lab6():
    print "GOOD"
    total=sumLIST(x)
    print total


def main():
    lab6()


main()
input()
