import random
from words import words

def get_vaild_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)


    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(str.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        print('you have used these letters: ' ', ' ' '.join(used.letters))

    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('current word: ', ' '.join(word_list))


    user_letter = input('guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letter.add(user_letter)
        if user_letter in word_letters:
            word.letters.remove(user_letter)


        elif user_letter in used_letters:
            print ('you have already used that character. Please try again.')

            user_input = input