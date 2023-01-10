import random
from words import words 
import string

def get_valid_word(words):
  word = random.choice(words) # randomly chooses something from the list
  while '-' in word or ' ' in word: # don't want to choose a word with a dash or space
    word = random.choice(words)
  
  return word.upper()

def hangman():
  word = get_valid_word(words)
  word_letters = set(word)  # letters in the word
  alphabet = set(string.ascii_uppercase)
  used_letters = set() # what the user has guessed

  lives = 7

  # getting user input
  while len(word_letters) > 0 and lives > 0:
    # letters used
    print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

    # current word
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('Current word: ', ' '.join(word_list))

    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters: # if its a valid character in the alphabet that the user hasn't used yet, add it to used_letters
      used_letters.add(user_letter)
      if user_letter in word_letters: # if the guessed letter is in the word, remove it from word_letters
        word_letters.remove(user_letter)
        print('')
      else:
        lives = lives - 1
        print('\nYour letter,', user_letter, 'is not in the word.')

    elif user_letter in used_letters:
      print("\nYou already used that character. Please try again")
    else:
      print("\nInvalid character. Please try again")
  
  # when len(word_letters) == 0 or lives == 0
  if lives == 0:
    print('You died, sorry. The word was', word)
  else:
    print('YAY! You guessed the word', word, '!!')

hangman()