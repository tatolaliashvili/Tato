import random, sys

print('🎲 Hello to Dice world! Higher roller will win! 🎲')

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins,losses,ties))
    while True:
        print('If you want to roll type yes or y. To quit type quit or q')
        playermove = input('> ')
        if playermove == 'quit' or playermove == 'q':
            print('Thank you for playing. See you next time!')
            sys.exit()
        if playermove == 'yes' or playermove == 'y':
            break
        print('Invalid input.')

    playerdice = random.randint(1, 12)
    if playermove == 'yes' or playermove == 'y':
        print('You have rolled ... 🎲 ' + str(playerdice))

    computerdice = random.randint(1, 12)
    print('Computer rolled ... 🎲 ' + str(computerdice))

    if playerdice == computerdice:
        print('It is a tie! 🤝')
        ties = ties + 1
    elif playerdice > computerdice:
        print('You rolled higher! 🔥')
        wins = wins + 1
    elif playerdice < computerdice:
        print('Computer rolled higher! 😢')
        losses = losses + 1

    if wins == 10:
        print('Congratulations! You have won! 🏆')
        break
    elif losses == 10:
        print('You have lost, good luck next time! 😢')
        break
    elif ties == 6:
        print('It is a tie, try again! 🤝')     
        break