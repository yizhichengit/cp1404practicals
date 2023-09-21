def main():
    # Get inputs for x and y
    x = int(input("Enter the value for x: "))
    y = int(input("Enter the value for y: "))

    # Display the menu and get the choice from the user
    choice = display_menu()

    while choice != 4:  # Continue until user selects "Exit the program"
        if choice == 1:
            # Display even numbers from x to y
            print("Even numbers from {} to {}:".format(x, y))
            for i in range(x, y + 1):
                if i % 2 == 0:
                    print(i, end=' ')
            print()

        elif choice == 2:
            # Display odd numbers from x to y
            print("Odd numbers from {} to {}:".format(x, y))
            for i in range(x, y + 1):
                if i % 2 != 0:
                    print(i, end=' ')
            print()

        elif choice == 3:
            # Display squares of numbers from x to y
            print("Squares from {} to {}:".format(x, y))
            for i in range(x, y + 1):
                print(i**2, end=' ')
            print()

        else:
            print("Invalid choice!")

        # Re-display the menu and get the next choice from the user
        choice = display_menu()

    print("Thank you! Goodbye!")


def display_menu():
    """Display the menu and return the user's choice."""
    print("\nMenu:")
    print("1. Show the even numbers from x to y")
    print("2. Show the odd numbers from x to y")
    print("3. Show the squares of the numbers from x to y")
    print("4. Exit the program")
    return int(input("Enter your choice: "))


if __name__ == "__main__":
    main()
