import random, sys

print('Welcome to Hangman challenge, you have to guess the word in 6 tries!')

words = ('Apple', 'Monkey', 'Train', 'Orange', 'Elephant', 'House', 'Hangman')
wrong_guesses = 0
wins = 0
losses = 0

while True:
    print('%s Wins, %s Losses' % (wins, losses))
    while True:
        print('If you wish to start type (s)tart or (q)uit to quit')
        user = input('> ')
        if user == 'q':
            print('Bye Bye')
            sys.exit()
        if user == 's':
            break

    computer_guess = random.randint(1,7)
    if computer_guess == 1:
        computer_word = 'Apple'
        print('A red or green fruit that keeps the doctor away')
    elif computer_guess == 2:
        computer_word = 'Monkey'
        print('A playful animal that loves bananas')
    elif computer_guess == 3:
        computer_word = "Train"
        print('A long vehicle that runs on tracks')
    elif computer_guess == 4:
        computer_word = 'Orange'
        print('A citrus fruit and a color')
    elif computer_guess == 5:
        computer_word = 'Elephant'
        print('The largest land animal with big ears and a trunk')
    elif computer_guess == 6:
        computer_word = 'House'
        print('The place where you live')
    elif computer_guess == 7:
        computer_word = 'Hangman'
        print('The name of the game')

