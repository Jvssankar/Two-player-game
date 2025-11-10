import random

# Function to decide winner between two choices
def decide_winner(choice1, choice2):
    if choice1 == choice2:
        return "tie"
    elif (choice1 == "rock" and choice2 == "scissors") or \
         (choice1 == "paper" and choice2 == "rock") or \
         (choice1 == "scissors" and choice2 == "paper"):
        return "player1"
    else:
        return "player2"

# Main game function
def play_game():
    print("Welcome to the Rock–Paper–Scissors Challenge")
    print("1. Single Player (Play vs Computer)")
    print("2. Two Players (Play with a Friend)")
    
    mode = input("Choose your mode (1 or 2): ")

    if mode == "1":
        player1 = input("\nEnter your name: ")
        player2 = "Computer"
    elif mode == "2":
        player1 = input("\nEnter Player 1 name: ")
        player2 = input("Enter Player 2 name: ")
    else:
        print("Invalid mode! Please restart and choose 1 or 2.")
        return

    rounds = int(input("\nHow many rounds do you want to play? "))
    choices = ["rock", "paper", "scissors"]
    score1 = 0
    score2 = 0

    for round_no in range(1, rounds + 1):
        print(f"\n----- Round {round_no} -----")
        choice1 = input(f"{player1}, enter your choice (rock/paper/scissors): ").lower()

        if choice1 not in choices:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue

        # For single-player mode, computer chooses randomly
        if mode == "1":
            choice2 = random.choice(choices)
            print(f"{player2} chose: {choice2}")
        else:
            # Hide 2nd player's input visually by clearing screen alternative
            print("\n" * 50)  # push the previous choice off the screen
            choice2 = input(f"{player2}, enter your choice (rock/paper/scissors): ").lower()

        if choice2 not in choices:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue

        winner = decide_winner(choice1, choice2)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "player1":
            print(f"{player1} wins this round!")
            score1 += 1
        else:
            print(f"{player2} wins this round!")
            score2 += 1

        print(f"Current Score -> {player1}: {score1} | {player2}: {score2}")

    # Final results
    print("\n===== Final Results =====")
    print(f"{player1}: {score1} | {player2}: {score2}")

    if score1 > score2:
        print(f"{player1} is the overall winner!")
    elif score2 > score1:
        print(f"{player2} is the overall winner!")
    else:
        print("It's a draw! Great match!")

    print("\nThanks for playing!")

# Run the game
if __name__ == "__main__":
    play_game()
