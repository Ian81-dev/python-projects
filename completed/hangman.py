import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    #a way to track what is a valid letter, what is not
    word = get_valid_word(words) #assign the previous function to 'word'
    #saving all the letters in 'word' as a set. tracking what has been
    #guessed in a word
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    #we don't want the user to guess infinitely, as this is hangman!
    lives = 6



    #getting user input
    while len(word_letters) > 0 and lives > 0: #the condition that user still needs to guess is when the length is not 0
        #we have to inform the user the letters used
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # show the user what current word is (ie. W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters: #if this is a valid letter in the alphabet I haven't used yet, I am going to 
            #add this to my used_letters set
            used_letters.add(user_letter)
            #if the letter i just guessed is in the word, then i will remove it from word_letters
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 #takes one life away if wrong 
                print("Letter is not in word.")    
        
        elif user_letter in used_letters:
            print("You have already used that character. Try again.")

        else:
            print('Invalid character. Please try again')

    if lives == 0:
        print('You died, sorry. The word was', word)
    
    else:
        print('You guessed the word', word, '!!')

hangman()

