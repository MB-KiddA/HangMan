import random, time
from words import words
import string
import os

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def Retry():
    retry = input('Play Again? (Y/N): ')
    retry = str(retry.upper())
    if retry == 'Y':
        os.system('cls')
        hangman()
    if retry == 'N':
        SystemExit
    else:
        os.system('cls')
        Retry

def s_print(string, letter_speed = 0.01):
    for character in string:
        print(f"{character}",end="",flush=True)
        time.sleep(letter_speed)

def e_print(string, color = 36, letter_speed = 0.001):
    for character in string:
        print(f"{character}",end="",flush=True)
        time.sleep(letter_speed)

def get_valid_word(words):
    word = random.choice(list(set(words)-{"kwantlen", "rai", "zimmerman"}))
    # randomly chooses something from the list
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    lives = 6
    pic = 0

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        os.system('cls')
        s_print(f"You have {lives} lives left and you have used these letters: {' '.join(used_letters)}")
        e_print(HANGMANPICS[pic])
        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print([lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                pic = pic + 1
                os.system('cls')

                e_print(F"\nYour letter {user_letter} is not in the word.")

        elif user_letter in used_letters:
            e_print('\nYou have already used that letter. Guess another letter.')

        else:
            e_print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        os.system('cls')
        e_print(HANGMANPICS[6])
        s_print(f"\nOOF You Lost! The Word is:' {word} '!!")
        Retry()
        
    if len(word_letters) == 0:
        s_print('CONGRATS! YOU WIN!')
        Retry()

if __name__ == '__main__':
    hangman()