import random

#now we define a function
#randint() brackets are parameters
#x is made a parameter for guess() because we need to pass this into
#randint()
def guess(x):
    random_number = random.randint(1,x)
    #we will need to keep looping until we get the right number.
    #the computer needs to tell us whether our guess is too high or too low
    guess = 0 #to make sure random number will never be 0
    while guess != random_number:
        guess = int(input(f'guess a number between 1 and {x}. '))
        if guess < random_number:
            print('sorry, guess again. too low')
        elif guess > random_number:
            print('sorry, guess again. too high')
    #you are out of the loop once you guessed the correct random number.
    print('yay, congrats. you guessed the number right.')

guess(10) #first entry starts up the guess function and gives x the
#max value that calls the computer to stop the random number here.

   