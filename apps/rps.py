import random

# INITIALIZE THE STATS
ties = 0
wins = 0
losses = 0
games = 0
keep_playing = True
print(f'Hello Steve! Welcome to Rock, Paper, Scissors!')
print("-------------------------------------------------------")
while keep_playing:
# USER INPUT
    while True:
        choices = ['ROCK', 'PAPER', 'SCISSORS']
        user_choice = input(f'Please choose an option {choices}:').upper()
    # VALIDATE THE INPUT
        if user_choice in choices:
            break
        else:
            print('Please select a valid option.')

# COMPUTER SELECTION
    computer_choice = random.choice(choices)

# SHOW SELECTIONS
    print(f'You chose {user_choice} and the computer chose {computer_choice}')


# WINNER DETERMINATION

    if user_choice ==  computer_choice:
        print('The game ended in a tie.')
        print("-----------------------------------------------------------------")
        ties += 1
        games += 1
    elif (user_choice == 'ROCK' and computer_choice == 'SCISSORS') or (user_choice == 'PAPER' and computer_choice == 'ROCK') or (user_choice == 'SCISSORS' and computer_choice == 'PAPER'):
        print('You won!')
        print("-----------------------------------------------------------------")
        wins += 1
        games += 1
    else:
        print('You lost.')
        print("-----------------------------------------------------------------")
        losses += 1
        games += 1


    # KEEP PLAYING

    while True:
        answer = input("Would you like to play again? (yes/no)").upper()
        if answer == 'NO':
            keep_playing = False
            break
        elif answer == 'YES':
            break
        else:
            print("Please enter yes or no!")

    # STATS
    if games >0:
        win_percentage = round((wins/games)*100,2)
        print(f'Wins: {wins} / Losses: {losses} / Ties: {ties}')
        print(f'Win Percentage: {win_percentage} %')
        print("Thanks for playing!")
        print("--------------------------------------")

