import random

def is_valid_number(num_str):
    """ Check if the input is a valid multi-digit number """
    return num_str.isdigit() and len(num_str) > 1

def get_correct_digits(secret_num, guess):
    """ Compare the secret number with the guess and return correct digits """
    return [secret_num[i] for i in range(len(secret_num)) if secret_num[i] == guess[i]]

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("Player 1 will set a number, and Player 2 will guess.")
    print("Then roles will switch. Let's start!\n")

    player1_wins = 0
    player2_wins = 0

    while True:
        # Player 1's turn to set the number
        print("Player 1's turn to set the number.")
        while True:
            secret_num_player1 = input("Player 1, enter a multi-digit number (at least 2 digits): ")
            if is_valid_number(secret_num_player1):
                break
            else:
                print("Invalid input. Please enter a valid multi-digit number.")

        print("\nPlayer 1 has set the number. Player 2, start guessing!\n")
        attempts_player2 = 0

        while True:
            guess_player2 = input("Player 2, enter your guess: ")
            if is_valid_number(guess_player2):
                attempts_player2 += 1
                if guess_player2 == secret_num_player1:
                    print(f"Congratulations! Player 2 guessed the number {secret_num_player1} correctly in {attempts_player2} attempts!")
                    player2_wins += 1
                    break
                else:
                    correct_digits = get_correct_digits(secret_num_player1, guess_player2)
                    print(f"Player 2, you got {len(correct_digits)} correct digit(s) in the correct position.")

        print(f"\nPlayer 2 wins: {player2_wins}, Player 1 wins: {player1_wins}\n")

        # Player 2's turn to set the number
        print("Player 2's turn to set the number.")
        while True:
            secret_num_player2 = input("Player 2, enter a multi-digit number (at least 2 digits): ")
            if is_valid_number(secret_num_player2):
                break
            else:
                print("Invalid input. Please enter a valid multi-digit number.")

        print("\nPlayer 2 has set the number. Player 1, start guessing!\n")
        attempts_player1 = 0

        while True:
            guess_player1 = input("Player 1, enter your guess: ")
            if is_valid_number(guess_player1):
                attempts_player1 += 1
                if guess_player1 == secret_num_player2:
                    print(f"Congratulations! Player 1 guessed the number {secret_num_player2} correctly in {attempts_player1} attempts!")
                    player1_wins += 1
                    break
                else:
                    correct_digits = get_correct_digits(secret_num_player2, guess_player1)
                    print(f"Player 1, you got {len(correct_digits)} correct digit(s) in the correct position.")

        print(f"\nPlayer 2 wins: {player2_wins}, Player 1 wins: {player1_wins}\n")

        # Determine the winner of this round
        if attempts_player1 < attempts_player2:
            print("Player 1 is crowned Mastermind!")
        elif attempts_player2 < attempts_player1:
            print("Player 2 is crowned Mastermind!")
        else:
            print("It's a draw in this round!")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nGame ended. Final results:")
            print(f"Player 2 wins: {player2_wins}, Player 1 wins: {player1_wins}")
            break

    print("Thank you for playing!")

play_game()
