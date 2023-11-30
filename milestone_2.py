#This is the first task in Hangman game, where a list is created and input is taken 
import random

word_list = ['banana', 'kiwi', 'mango', 'berry', 'pears'] #create a list for the game
print(word_list)
word = random.choice(word_list) # select a random word from the list
print(word)

# Ask the user for a input
guess = input("Enter a single character: ")
# Check if the input is a single character and alphabetical
if ((len(guess) == 1 ) and (guess.isalpha()== True)) :
    print('Good guess')
else:
    print("Oops, that is not a valid input")
    