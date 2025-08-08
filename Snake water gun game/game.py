import random

def snake_water_gun():
    print("Welcome to Snake Water Gun!")
    print("Rules:\nSnake drinks Water\nWater drowns Gun\nGun shoots Snake")
    
    choices = ['snake', 'water', 'gun']
    user_score = 0
    computer_score = 0
    rounds = 0
    
    while True:
        print("\nRound", rounds + 1)
        print(f"Score - You: {user_score} | Computer: {computer_score}")
        
        # User input with validation
        while True:
            user_choice = input("Choose (snake/water/gun) or 'quit' to exit: ").lower()
            if user_choice in choices or user_choice == 'quit':
                break
            print("Invalid choice! Please enter snake, water, or gun.")
        
        if user_choice == 'quit':
            print("\nFinal Score - You:", user_score, "| Computer:", computer_score)
            if user_score > computer_score:
                print("You win the game! 🎉")
            elif user_score < computer_score:
                print("Computer wins the game! 💻")
            else:
                print("It's a tie game! 🤝")
            break
            
        computer_choice = random.choice(choices)
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie this round!")
        elif (
            (user_choice == 'snake' and computer_choice == 'water') or
            (user_choice == 'water' and computer_choice == 'gun') or
            (user_choice == 'gun' and computer_choice == 'snake')
        ):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
            
        rounds += 1

# Start the game
snake_water_gun()