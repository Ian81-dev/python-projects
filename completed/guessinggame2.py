import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    #first set the value that indicates that computer has guessed correctly
    while feedback != 'c':
        guess = random.randint(low,high)
        feedback = input(f'is {guess} too high (H), too low (L), or correct (C)?').lower()
        if feedback == 'h':
            #when guess is too high, we need to adjust the upper bound
            high = guess - 1
        if feedback == 'l':
            low = guess + 1
    #when the computer is correct, we exit the while loop
    print(f'Congratz! You have guessed correctly!The number is {guess}.')

#again, initialize the function with a manual random guess. note that this number entered 
#is the highest value that the computer can guess, else it will throw an error.
computer_guess(100) 