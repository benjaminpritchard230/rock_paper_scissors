from functions import decide_winner, player_choice, computer_choice

player_score = 0
computer_score = 0
games_played = 0
acceptable_inputs = ['rock', 'paper', 'scissors']

while games_played < 3    :
    player = player_choice()
    computer = computer_choice()
    print(f'Player has chosen: {player}. \nComputer has chosen: {computer}.')
    
    if decide_winner(player, computer) == 'Player wins':
        print('Player wins')
        player_score += 1
    elif decide_winner(player, computer) == 'Computer wins':
        print('Computer wins')
        computer_score += 1
    else:
        pass
    
    games_played += 1
    print(f'Games played: {games_played} of 3')
    print(f'Player score: {player_score}, Computer score: {computer_score}')

if player_score > computer_score:
    print('Game over. Player wins overall.')
else:
    print('Game over. Computer wins overall.')

