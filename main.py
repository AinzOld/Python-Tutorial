import random

def roll_dice():
    """Simulate rolling a six-sided die."""
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Simulator!")

    while True:
        input("Press Enter to roll the die. Press 'q' to quit.")
        
        # Get a random number to simulate rolling a die
        result = roll_dice()

        print(f"You rolled: {result}")

        if input("Roll again? (y/n): ").lower() != 'y':
            print("Thanks for using the Dice Simulator. Goodbye!")
            break

if __name__ == "__main__":
    main()
