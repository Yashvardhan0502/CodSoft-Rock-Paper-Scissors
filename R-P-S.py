import random

game_rules = {
    1: {"beats": 3, "loses_to": 2},
    2: {"beats": 1, "loses_to": 3},
    3: {"beats": 2, "loses_to": 1}
}

user_score = 0
computer_score = 0

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "***It is a tie***"
    elif computer_choice == game_rules[user_choice]["beats"]:
        return "***You win***"
    else:
        return "***Computer wins***"

def display_score():
    print(f"Your Score = {user_score}\tComputer Score = {computer_score}")

def main():
    global user_score, computer_score

    print("\n*********Welcome to Rock, Paper, Scissors Game!*********\n")

    while True:
        print("Choose:\n1- Rock\n2- Paper\n3- Scissors\n")

        user_choice = int(input("Enter the number of your choice: "))
        if user_choice not in game_rules:
            print("Invalid input. Please select a number between 1 to 3.")
            continue

        computer_choice = random.choice(list(game_rules.keys()))
        result = winner(user_choice, computer_choice)
        
        print(f"Your choice = {user_choice}\nComputer choice = {computer_choice}\n\n")
        print(result)
        
        if result == "***You win***":
            user_score += 1
        elif result == "***Computer wins***":
            computer_score += 1
        
        display_score()

        play_again = input("\nDo you want to continue? (y/n)").lower()
        if play_again != 'y':
            print("Thanks for playing.......!")
            break  # Exit the loop when play_again is not 'y'

if __name__ == "__main__":
    main()
