import random

num = random.randint(0, 100)

print "The random number is: " + str(num)
rand = 0
guess = 50
inc = 25
while guess != num :
    if guess > num:
        print "Try again computer your guess was " + str(guess)
        guess -= inc
        rand+=1
        inc/=2
    elif guess < num:
        print "Try again computer your guess was " + str(guess)
        guess +=inc
        rand+=1
        inc/=2

    if inc==0:
        inc=1

    if guess == num:
        print "The computer's guess is : " + str(guess) + " Congrats!"
        print "The computer guessed it in: " + str(rand) + " times"


