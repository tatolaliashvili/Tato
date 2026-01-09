import random, sys

print('ROCK, PAPER, SCISSORS')
wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins,losses,ties))
    while True:
        print('First who reaches 10 wins is the WINNER!\nEnter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input('> ')
        if player_move == 'q':
            print('Thank you for playing. See you next time!')
            sys.exit()
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break
        # if player_move != 'r' or 'p' or 's' or 'q':
        print('Invalid input.')
            
    if player_move == 'r':
        print('✊ \nversus ... ')
    elif player_move == 'p':
        print('📃 \nversus ... ')
    elif player_move == 's':
        print('✂️ \nversus ... ')
    
    move_number = random.randint(1,3)
    if move_number == 1:
        computer_move = 'r'
        print('✊')
    elif move_number == 2:
        computer_move = 'p'
        print('📃')
    elif move_number == 3:
        computer_move = 's'
        print('✂️')

    if player_move == computer_move:
        print('🤝 It is a tie! 🤝')
        ties = ties + 1
    elif player_move == 'r' and computer_move == 's':
        print('🔥 You win! 🔥')
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print('🔥 You win! 🔥')
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print('🔥 You win! 🔥')
        wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
        print('😢 You lose! 😢')
        losses = losses + 1
    elif player_move == 'p' and computer_move == 's':
        print('😢 You lose! 😢')
        losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
        print('😢 You lose! 😢')
        losses = losses + 1

    if wins == 10:
        print('🏆 Congratulation you have won! 🏆')
        break
    elif losses == 10:
        print('😢 Unfortunately you have lost! 😢')
        break
    elif ties == 6:
        print('🤝 Good job, it is a tie overall! 🤝')
        break