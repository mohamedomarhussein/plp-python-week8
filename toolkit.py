import random

# --- Tool 1: Number Guessing Game ---
def guessing_game():
    """A simple number guessing game with a while loop."""
    print("\n--- Number Guessing Game ---")
    secret = random.randint(1, 50)
    attempts = 0
    while True:
        try:
            guess = int(input("Guess a number between 1 and 50: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        attempts += 1
        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break

# --- Tool 2: To-Do List ---
def todo_list():
    """A simple to-do list using a list that changes while running."""
    print("\n--- To-Do List ---")
    tasks = []
    while True:
        print("\n1. Add task\n2. View tasks\n3. Remove task\n4. Back to main menu")
        choice = input("Choose an option: ")
        
        if choice == "1":
            task = input("Enter a new task: ")
            tasks.append(task)
            print(f"Task '{task}' added.")
        elif choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("Your tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
        elif choice == "3":
            if not tasks:
                print("Nothing to remove.")
            else:
                task = input("Enter task to remove: ")
                if task in tasks:
                    tasks.remove(task)
                    print(f"Task '{task}' removed.")
                else:
                    print("That task is not in your list.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

# --- Tool 3: Simple Calculator ---
def calculator():
    """A simple calculator using conditionals."""
    print("\n--- Simple Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number entered.")
        return

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator.")
        return

    print(f"Result: {num1} {op} {num2} = {result}")

# --- Main Menu Loop ---
def main():
    print("Welcome to Your Personal Mini-Toolkit! 🧰")
    while True:
        print("\n--- Main Menu ---")
        print("1. Guess the Number")
        print("2. To-Do List")
        print("3. Simple Calculator")
        print("4. Quit")
        choice = input("Choose a tool (1-4): ")

        if choice == "1":
            guessing_game()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            calculator()
        elif choice == "4":
            print("Goodbye! Thanks for using the toolkit. 👋")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

# Run the program
if __name__ == "__main__":
    main()