import random


def determine_winner(user, computer):
    if user == computer:
        return 'It\'s a tie'
    elif (user == 'rock' and computer == 'paper') or (user == 'rock' and computer == 'scissors') or (
            user == 'paper' and computer == 'scissors'):
        return 'You won!'
    else:
        return 'You lost!'


def play_game():
    while True:
        user = input("Enter your choice (rock, paper, scissors): ")
        computer = random.choice(['rock', 'paper', 'scissors'])
        result = determine_winner(user, computer)
        print(result)
        response = input("DO you want to continue ? (yes/no):")
        if response.lower() != 'yes':
            print("Thanks for playing :)")
            break


play_game()
