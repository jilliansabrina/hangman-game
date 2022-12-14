import random
import os
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo
from hangman_art import fireworks
from hangman_art import you_suck

# Lets the player know when they win the game.
def check_win(display):
    for char in display:
        if char == '_':
            return False
    print(fireworks)
    print("Congratulations, you win!")
    return True


# Ends the game when the player has run out of lives.
def end_game(lives, chosen_word):
    print(stages[lives])
    print(
        f'\nYou lost. The correct solution was \'{chosen_word}\'. Game over.\n'
    )
    print(you_suck)

# Asks the user to input a letter, verifies if right or wrong
def guess_letter(lives, display, chosen_word, wrong_guesses):
    # Printing lives and the current stage of the hangman.
    print(f"\nYou have {lives} lives left.\n\nCorrect guesses: {display}\n")
    # When the player has less than seven lives, it will start displaying the hangman.
    if lives < 7:
      print(f'Wrong guesses: {sorted(wrong_guesses)}\n')
      print(f'{stages[lives]}\n')
    # User inputs the letter guess.
    guess = input('Guess a letter: ').lower()
    # Checks if the user already guessed the letter.
    while guess in display or guess in wrong_guesses:
      guess = input(f"You've already guessed {guess}. Try again: ")
    # Checks that the guess is a single alphabetical character.
    while len(guess) != 1 or not guess.isalpha():
      guess = input('The guess entered is not valid. Please enter a single alphabetic character. Try again: ')
    os.system('clear')
    # Variable change lets us keep track of the correct and wrong guesses.
    change = False
    # Verifies if the letter guess is in the chosen word.
    for idx in range(len(chosen_word)):
        # If the letter is in the word, it will display all of its occurences.
        if guess == chosen_word[idx]:
            display[idx] = guess
            change = True
    # If the guess is wrong, the player loses a life.
    if change == False:
        lives -= 1
        wrong_guesses.append(guess)
        print(f"You guessed \'{guess}\'. That\'s not in the word. You lose a life.")
        if lives <= 0:
            end_game(lives, chosen_word)
    # While the player has not won or ran out of lives, the game keeps running.
    if not check_win(display) and lives > 0: return guess_letter(lives, display, chosen_word, wrong_guesses)

def main():
  # Setting chosen word, the hidden letter display and 7 lives at the start of the game.
  chosen_word = random.choice(word_list)
  display, wrong_guesses = [], []
  for char in chosen_word:
      display += '_'
  lives = 7
  
  # Print the heading logo of the hangman game.
  print(f'{logo}\n')
  
  guess_letter(lives, display, chosen_word, wrong_guesses)

if __name__ == "__main__":
    main()
