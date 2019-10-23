import random

guess = random.randint(1, 10)
numberGuessed = False

while not numberGuessed:
    userNumber = input('Guess a number between 1 to 10: ')
    if userNumber == guess:
        print('Well guessed!')
        numberGuessed = True

