def lab6():
     year=raw_input("input year: ")
     year=int(year)
     if(year%4==0):
         print "Leap year"
     else:
         print "Not Leap year"



def highlow():
    import random
    guessesTaken = 0
    number = random.randint(1,50)
    print('I am thinking of a number between 1 and 50.')
    while guessesTaken < 100:
        print ('Take a guess.')
        guess = input()
        guess = int(guess)
        guessesTaken = guessesTaken + 1
        if guess < number:
            print('your guess is too low.')
        if guess > number:
            print('your guess is too high.')
        if guess==number:
            break
    if guess== number:
        guessesTaken = str(guessesTaken)
        print('You did Good!'+' You guessed my number in'+ ' guessesTaken'+'guesses!')
    if guess !=number:
        number = str(number)
        print('No. the number that I was thinking of was '+number)
def main():
    lab6()
    highlow()	

main()