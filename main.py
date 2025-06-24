import random

PAPER      = 'paper'
ROCK       = 'rock'
SCISSORS   = 'scissors'
CHOICES    = (PAPER, ROCK, SCISSORS)
WIN_CASES  = { (PAPER, ROCK), (ROCK, SCISSORS), (SCISSORS, PAPER) }

RESULT_TEXT = {
    0: 'It\'s draw ;)',
    1: 'You win!',
    2: 'You lose!'
}

def get_enemy_choice():
    return random.choice(CHOICES)

def get_player_choice():
    while True:
        player_choice = input('Choose paper, rock or scissors: ').lower()
        if player_choice in CHOICES:
            return player_choice

        print('Incorrect choice!')

def determine_winner(player_choice, enemy_choice):
    if player_choice == enemy_choice:
        return 0
    elif (player_choice, enemy_choice) in WIN_CASES:
        return 1
    else:
        return 2

# Main game function
def play_game():
    print('Hello, this is Paper-Rock-Scissors Game!!!')

    while True:
        player_choice = get_player_choice()
        enemy_choice  = get_enemy_choice()
        print(f'Your choice: {player_choice}')
        print(f'Enemy choice: {enemy_choice}')

        win_state = determine_winner(player_choice, enemy_choice)
        # If it's draw 
        if win_state == 0:
            continue

        break

    print(RESULT_TEXT[win_state])

if __name__ == "__main__":
    play_game()
