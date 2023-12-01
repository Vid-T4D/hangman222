#This is the first task in Hangman game, where a list is created and input is taken 
import random

word_list = ['banana', 'kiwi', 'mango', 'berry', 'pears'] #create a list for the game
print(word_list)
word = random.choice(word_list) # select a random word from the list
print(word)


class Hangman:
    def __init__(self, word_list, num_lives=5):

        # parameters
        self.word_list = [] # Initialize an empty list
        self.num_lives = num_lives

        #attributes
        self.num_letters = len(set(word))
        self.list_of_guesses = [] # Initialize an empty list
        self.word = word

        self.word_guessed = ['_' for item in word]




 #This method is to check whether the letter guessed by the user is in the word that was randomly chosen by the computer

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in word:
            print(f"Good guess!'{guess}' is in the word.")
            for index, letter in enumerate(word):
                if letter == guess: 
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry,'{guess}' is not in word.")
            print(f"You have '{self.num_lives}' lives left")

# This method is to  continuously ask the user for a letter and validate it.
    def ask_for_input(self):
        while(True):
            guess = input("Enter a single character: ") # Ask the user for a input
            if ((len(guess) != 1 ) and (guess.isalpha()== False)):
                print("Invalid letter. Please, enter a single alphabetical character.")
            
            elif any(item in guess for item in self.list_of_guesses): # Checks if the guess is already in the list_of_guesses
                print("You already tried that letter")
            else: 
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break
                
        

my_instance = Hangman(word_list)
my_instance.ask_for_input()
