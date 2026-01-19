import random

secret_number = random.randint(1,20)
print('I\'m thinking of a number between 1 and 20 \nTake a guess.')
for guesses_taken in range(1,4):
    guess = int(input('>'))
    guesses_left = 3 - guesses_taken
    if guess < secret_number:
        print('Your guess is too low! You have ' + str(guesses_left) + ' guesses left.')
    elif guess > secret_number:
        print('Your guess is too high ' + str(guesses_left) + ' guesses left.')
        break
if guess == secret_number:
    print('Good job! You got it in ' + str(guesses_taken) + ' guesses!')
else:
    print('Nope, the number was ' + str(secret_number))        