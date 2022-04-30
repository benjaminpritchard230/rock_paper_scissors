def decide_winner(player, computer):
    """Returns the winner."""
    if player == computer:
        return 'Draw'
    elif player == 'rock':
        if computer == 'paper':
            return 'Computer wins'
        else:
            return 'Player wins'
    elif player == 'paper':
        if computer == 'scissors':
            return 'Computer wins'
        else:
            return 'Player wins'
    elif player == 'scissors':
        if computer == 'rock':
            return 'Computer wins'
        else:
            return 'Player wins'

def player_choice():
    """Returns the player's choice"""
    acceptable_inputs = ['rock', 'paper', 'scissors']
    while True:
        while True:
            try:
                player = str(input('Select rock, paper or scissors:'))
            except ValueError:
                print('Please enter a valid input.')
                continue
            break
        if player not in acceptable_inputs:
            print('Please enter a valid input.')
            continue
        else:
            break
    return player

def computer_choice():
    """Returns a random computer choice."""
    import random
    computer_choices = ['rock', 'paper', 'scissors']
    computer = random.choice(computer_choices)
    return computer