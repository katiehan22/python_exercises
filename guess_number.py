import random 

def guess(x):
  random_number = random.randint(1, x)

  keep_guessing = True 
  while(keep_guessing):
    guess = int(input("Enter a number: "))
    if guess == random_number:
      keep_guessing = False
      print(f'{guess} was the correct number!')
    elif guess < random_number:
      print(f'{guess} is too low')
    else:
      print(f'{guess} is too high')

def computer_guess(x):
  low = 1
  high = x 
  feedback = ''

  while feedback != 'c':
    if low != high:
      guess = random.randint(low, high)
    else: 
      guess = low # could also be high bc low = high
    
    feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower()

    if feedback == 'h':
      high = guess - 1
    elif feedback == 'h':
      low = guess + 1 
  
  print(f'Yay! The computer guessed your number {guess} correctly!')


# guess(50)
computer_guess(10)