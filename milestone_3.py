import random

word_list = ['banana', 'kiwi', 'mango', 'berry', 'pears'] #create a list for the game
print(word_list)
word = random.choice(word_list) # select a random word from the list
print(word)

#guess = input("Enter a single character: ")

def check_guess(guess):
    guess = guess.lower()

    #This code is to check whether the letter guessed by the user is in the word that was randomly chosen by the computer.
    if guess in word:
        print(f"Good guess!'{guess}' is in the word.")
    else:
        print(f"Sorry,'{guess}' is not in the word. Try again.")


def ask_for_input():
# This code is to  continuously ask the user for a letter and validate it.
    while(True):
        guess = input("Enter a single character: ") # Ask the user for a input
        if ((len(guess) == 1 ) and (guess.isalpha()== True)):  # Check if the input is a single character and alphabetical
            break # Exit the loop if it satisfies the above condition
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()
