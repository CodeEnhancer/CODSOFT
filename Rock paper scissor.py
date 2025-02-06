import random
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"
while True:
    user_choice = input("Choose any one  Rock, Paper, Scissors: ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        continue
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thanks for playing!")
